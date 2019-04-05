/*! Copyright (c) 2013 - Peter Coles (mrcoles.com)
 *  Licensed under the MIT license: http://mrcoles.com/media/mit-license.txt
 */
  var noteArray = [];

(function() {
  //
  // Setup keys!
  //

  var intToNotes = {
      // Low octave
      0 : "c",
      1 : "c#",
      2 : "d",
      3 : "d#",
      4 : "e",
      5 : "f",
      6 : "f#",
      7 : "g",
      8 : "g#",
      9 : "a",
      10 : "a#",
      11 : "b",
      // High octave
      12 : "highc",
      13 : "highc#",
      14 : "highd",
      15 : "highd#",
      16 : "highe",
      17 : "highf",
      18 : "highf#",
      19 : "highg",
      20 : "highg#",
      21 : "higha",
      22 : "higha#",
      23 : "highb",
  };


  var notesOffset = 0;
  var mouseOffset = 12;

  var blackKeys = {
    1: 1,
    3: 3,
    6: 1,
    8: 2,
    10: 3
  };
  $.each(blackKeys, function(k, v) {
    blackKeys[k] = " black black" + v;
  });

  function blackKeyClass(i) {
    return blackKeys[(i % 12) + (i < 0 ? 12 : 0)] || "";
  }

  var $keys = $("<div>", { class: "keys" }).appendTo("#piano");

  var buildingPiano = false;

  var isIos = navigator.userAgent.match(/(iPhone|iPad)/i);

  function buildPiano() {
    if (buildingPiano) return;
    buildingPiano = true;

    $keys.trigger("build-start.piano");
    $keys.empty().off(".play");

    function addKey(i) {
      var dataURI = isIos ? "" : Notes.getDataURI(i);

      // trick to deal with note getting hit multiple times before finishing...
      var sounds = [new Audio(dataURI), new Audio(dataURI), new Audio(dataURI)];
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

        var $k = $keys.find("[data-key=" + i + "]").addClass("pressed");

        $keys.trigger("played-note.piano", [i, $k]);

        // visual feedback
        window.clearTimeout(pressedTimeout);
        pressedTimeout = window.setTimeout(function() {
          $k.removeClass("pressed");
        }, 200);
      }
      $keys.on("note-" + i + ".play", play);
      var $key = $("<div>", {
        class: "key" + blackKeyClass(i),
        "data-key": i,
        mousedown: function(evt) {
          console.log("Key pressed by mouse, index: " + i  + "NOTE: " + intToNotes[i + mouseOffset]);
          noteArray.push(intToNotes[i + mouseOffset]);
          $keys.trigger("note-" + i + ".play");
        }
      }).appendTo($keys);
    }

    // delayed for-loop to stop browser from crashing :'(
    // go slower on Chrome...

    var i = -12,
      max = 12,
      addDelay = /Chrome/i.test(navigator.userAgent) ? 80 : 0;
    (function go() {
      addKey(i + notesOffset);
      if (++i < max) {
        window.setTimeout(go, addDelay);
      } else {
        buildingPiano = false;
        $keys.trigger("build-done.piano");
      }
    })();
  }

  buildPiano();

  //
  // Setup synth controls
  //

  function camelToText(x) {
    x = x.replace(/([A-Z])/g, " $1");
    return x.charAt(0).toUpperCase() + x.substring(1);
  }

  $.each(["volume", "style"], function(i, setting) {
    var $opts = $("<div>", {
      class: "opts",
      html: "<p><strong>" + camelToText(setting) + ":</strong></p>"
    }).appendTo("#synth-settings");

    $.each(DataGenerator[setting], function(name, fn) {
      if (name != "default") {
        $("<p>")
          .append(
            $("<a>", {
              text: camelToText(name),
              href: "#",
              class: fn === DataGenerator[setting].default ? "selected" : "",
              click: function(evt) {
                evt.preventDefault();
                DataGenerator[setting].default = fn;
                buildPiano();
                var $this = $(this);
                $this
                  .closest(".opts")
                  .find(".selected")
                  .removeClass("selected");
                $this.addClass("selected");
              }
            })
          )
          .appendTo($opts);
      }
    });
  });

  //
  // Setup keyboard interaction
  //

  var keyToCodes = {
    // Low octave
    /*z*/ 'z' : 122, // c
    /*s*/ 's' : 115, // c#
    /*x*/ 'x' : 120, // d
    /*d*/ 'd' : 100, // d#
    /*c*/ 'c' : 99, // e
    /*v*/ 'v' : 118, // f
    /*g*/ 'g' : 103, // f#
    /*b*/ 'b' : 98, // g
    /*h*/ 'h' : 104, // g#
    /*n*/ 'n' : 110, // a
    /*j*/ 'j' : 106, // a#
    /*m*/ 'm' : 109, // b
    // High octave
    /*r*/ 'r' : 114, // c
    /*5*/ '5' : 53, // c#
    /*t*/ 't' : 116, // d
    /*6*/ '6' : 54, // d#
    /*y*/ 'y' : 121, // e
    /*u*/ 'u' : 117, // f
    /*8*/ "8" : 56, // f#
    /*i*/ 'i' : 105, // g
    /*9*/ '9' : 57, // g#
    /*o*/ 'o' : 111, // a
    /*0*/ '0' : 48, // a#
    /*p*/ 'p' : 112 // b
  };

  var keyNotes = {
    // Low octave
    /*z*/ 122 : 0, // c
    /*s*/ 115 : 1, // c#
    /*x*/ 120 : 2, // d
    /*d*/ 100 : 3, // d#
    /*c*/ 99 : 4, // e
    /*v*/ 118 : 5, // f
    /*g*/ 103 : 6, // f#
    /*b*/ 98 : 7, // g
    /*h*/ 104 : 8, // g#
    /*n*/ 110 : 9, // a
    /*j*/ 106 : 10, // a#
    /*m*/ 109 : 11, // b
    // High octave
    /*r*/ 114 : 12, // c
    /*5*/ 53 : 13, // c#
    /*t*/ 116 : 14, // d
    /*6*/ 54 : 15, // d#
    /*y*/ 121 : 16, // e
    /*u*/ 117 : 17, // f
    /*8*/ 56 : 18, // f#
    /*i*/ 105 : 19, // g
    /*9*/ 57 : 20, // g#
    /*o*/ 111 : 21, // a
    /*0*/ 48 : 22, // a#
    /*p*/ 112 : 23 // b
  };

  var notesShift = -12;
  var downKeys = {};

  $(window)
      .keydown(function(evt) {
      var keyTone = evt.key;
      var keyCode = keyToCodes[keyTone];
      if (!downKeys[keyCode]) {
        downKeys[keyCode] = 1;
        var key = keyNotes[keyCode];
        // console.log("Trigger     Keyboard: " + evt.key + "     Keycode: " + keyCode + "     key: " + key);
        if (typeof key != "undefined") {
          noteArray.push(intToNotes[key])
          // console.log(noteArray)
          $keys.trigger("note-" + (key + notesShift + notesOffset) + ".play");
          evt.preventDefault();
        } else if (keyCode == 188) {
            notesShift = -12;
        } else if (keyCode == 190) {
            notesShift = 0;
        } else if (keyCode == 37 || keyCode == 39) {
            notesOffset += (keyCode == 37 ? -1 : 1) * 12;
            buildPiano();
        }
      }
    })
    .keyup(function(evt) {
      var keyTone = evt.key;
      var keyCode = keyToCodes[keyTone];
      delete downKeys[keyCode];
    });

  //
  // Help controls
  //

  var $help = $(".help");

  var qTimeout,
    qCanToggle = true;
  $(window).keypress(function(evt) {
    // trigger help when ? is pressed, but make sure it doesn't repeat crazy
    if (evt.which == 63 || evt.which == 48) {
      window.clearTimeout(qTimeout);
      qTimeout = window.setTimeout(function() {
        qCanToggle = true;
      }, 1000);
      if (qCanToggle) {
        qCanToggle = false;
        $help.toggleClass("show");
      }
    }
  });

  window.setTimeout(function() {
    $help.removeClass("show");
  }, 700);

  // prevent quick find...
  $(window).keydown(function(evt) {
    if (evt.target.nodeName != "INPUT" && evt.target.nodeName != "TEXTAREA") {
      if (evt.key == 'single quote') {
        evt.preventDefault();
        return false;
      }
    }
    return true;
  });

})();

function toPianoJson(data,type,mode,iter,step) {
  var string =
    "{" +
    '"data":' +
    '"' +
    data +
    '", ' +
    '"type":' +
    '"' +
    type +
    '", ' +
    '"mode":' +
    '"' +
    mode +
    '", ' +
    '"iteration":' +
    iter +
    ", " +
    '"step":' +
    step +
    "}";
  return string;
}

 function sendNotes() {
    var notes = JSON.stringify(noteArray);
    var pianoJson = toPianoJson(noteArray,"Sierpinski","piano","3","20"); //TODO: select fractal
    console.log(notes);
    sendMessage(pianoJson);
    noteArray = [];
  }
