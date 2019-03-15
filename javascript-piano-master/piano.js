/*! Copyright (c) 2013 - Peter Coles (mrcoles.com)
 *  Licensed under the MIT license: http://mrcoles.com/media/mit-license.txt
 */

(function() {

    //
    // Setup keys!
    //

    var notesOffset = 0;

    var blackKeys = {
        1: 1,
        3: 3,
        6: 1,
        8: 2,
        10: 3
    };
    $.each(blackKeys, function(k, v) {
        blackKeys[k] = ' black black'+v;;
    });

    function blackKeyClass(i) {
        return blackKeys[(i % 12) + (i < 0 ? 12 : 0)] || '';
    }

    var $keys = $('<div>', {'class': 'keys'}).appendTo('#piano');

    var buildingPiano = false;

    var isIos = navigator.userAgent.match(/(iPhone|iPad)/i);

    function buildPiano() {
        if (buildingPiano) return;
        buildingPiano = true;

        $keys.trigger('build-start.piano');
        $keys.empty().off('.play');

        function addKey(i) {
            var dataURI = isIos ? '' : Notes.getDataURI(i);

            // trick to deal with note getting hit multiple times before finishing...
            var sounds = [
                new Audio(dataURI),
                new Audio(dataURI),
                new Audio(dataURI)
            ];
            var curSound = 0;
            var pressedTimeout;
            dataURI = null;
            function play(evt) {
                // sound
                sounds[curSound].pause();
                try {
                    sounds[curSound].currentTime = 0.001; //HACK - was for mobile safari, but sort of doesn't matter...
                } catch (x) {
                    console.log(x);
                }
                sounds[curSound].play();
                curSound = ++curSound % sounds.length;

                var $k = $keys.find('[data-key='+i+']').addClass('pressed');

                //TODO - it'd be nice to have a single event for triggering and reading
                $keys.trigger('played-note.piano', [i, $k]);

                // visual feedback
                window.clearTimeout(pressedTimeout);
                pressedTimeout = window.setTimeout(function() {
                    $k.removeClass('pressed');
                }, 200);
            }
            $keys.on('note-'+i+'.play', play);
            var $key = $('<div>', {
                'class': 'key' + blackKeyClass(i),
                'data-key': i,
                mousedown: function(evt) { $keys.trigger('note-'+i+'.play'); }
            }).appendTo($keys);
        }

        // delayed for-loop to stop browser from crashing :'(
        // go slower on Chrome...
        var i = -12, max = 14, addDelay = /Chrome/i.test(navigator.userAgent) ? 80 : 0;
        (function go() {
            addKey(i + notesOffset);
            if (++i < max) {
                window.setTimeout(go, addDelay);
            } else {
                buildingPiano = false;
                $keys.trigger('build-done.piano');
            }
        })();
    }

    buildPiano();


    //
    // Setup synth controls
    //

    function camelToText(x) {
        x = x.replace(/([A-Z])/g, ' $1');
        return x.charAt(0).toUpperCase() + x.substring(1);
    }

    $.each(['volume', 'style'], function(i, setting) {
        var $opts = $('<div>', {
            'class': 'opts',
            html: '<p><strong>' + camelToText(setting) + ':</strong></p>'
        }).appendTo('#synth-settings');

        $.each(DataGenerator[setting], function(name, fn) {
            if (name != 'default') {
                $('<p>')
                    .append($('<a>', {
                        text: camelToText(name),
                        href: '#',
                        'class': fn === DataGenerator[setting].default ? 'selected' : '',
                        click: function(evt) {
                            evt.preventDefault();
                            DataGenerator[setting].default = fn;
                            buildPiano();
                            var $this = $(this);
                            $this.closest('.opts').find('.selected').removeClass('selected');
                            $this.addClass('selected');
                        }
                    }))
                    .appendTo($opts);
            }
        });
    });


    //
    // Setup keyboard interaction
    //

    var keyNotes = {
        /*a*/ 65: 0, // c
        /*w*/ 87: 1, // c#
        /*s*/ 83: 2, // d
        /*e*/ 69: 3, // d#
        /*d*/ 68: 4, // e
        /*f*/ 70: 5, // f
        /*t*/ 84: 6, // f#
        /*g*/ 71: 7, // g
        /*y*/ 89: 8, // g#
        /*h*/ 72: 9, // a
        /*u*/ 85: 10, // a#
        /*j*/ 74: 11, // b
        /*k*/ 75: 12, // c
        /*o*/ 79: 13, // c#
        /*l*/ 76: 14, // d
        /*p*/ 80: 15, // d#
        /*ö*/ 186: 16, // e
        /*ö*/ 59: 16, // e ... gotta figure out why it's sometimes 186 and sometimes 59
        /*ä*/ 222: 17, // f
        /*¨*/ 221: 18, // f#
        /*enter*/ 13: 19 // g
    };
    var notesShift = -12;
    var downKeys = {};
    var keyCodes = {};

    $(window).keydown(function(evt) {
        var keyCode = evt.keyCode;
        keyCodes = 
        // prevent repeating keys
        if (!downKeys[keyCode]) {
            downKeys[keyCode] = 1;
            var key = keyNotes[keyCode];
            if (typeof key != 'undefined') {
                $keys.trigger('note-'+(key+notesShift+notesOffset)+'.play');
                evt.preventDefault();
            }
        }
    }).keyup(function(evt) {
        delete downKeys[evt.keyCode];
    });

    //
    // Help controls
    //

    var $help = $('.help');

    var qTimeout, qCanToggle = true;;
    $(window).keypress(function(evt) {
        // trigger help when ? is pressed, but make sure it doesn't repeat crazy
        if (evt.which == 63 || evt.which == 48) {
            window.clearTimeout(qTimeout);
            qTimeout = window.setTimeout(function() {
                qCanToggle = true;
            }, 1000);
            if (qCanToggle) {
                qCanToggle = false;
                $help.toggleClass('show');
            }
        }
    });

    window.setTimeout(function() {
        $help.removeClass('show');
    }, 700);

    // prevent quick find...
    $(window).keydown(function(evt) {
        if (evt.target.nodeName != 'INPUT' && evt.target.nodeName != 'TEXTAREA') {
            if (evt.keyCode == 222) {
                evt.preventDefault();
                return false;
            }
        }
        return true;
    });

})();
