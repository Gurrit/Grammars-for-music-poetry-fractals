// paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function f() {
  log.history = log.history || [];
  log.history.push(arguments);
  if (this.console) {
    let args = arguments,
      newarr;
    args.callee = args.callee.caller;
    newarr = [].slice.call(args);
    if (typeof console.log === "object")
      log.apply.call(console.log, console, newarr);
    else console.log.apply(console, newarr);
  }
};
// make it safe to use console.log always
(function(a) {
  function b() {}
  for (
    let c = "assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profileEnd,time,timeEnd,trace,warn".split(
        ","
      ),
      d;
    !!(d = c.pop());

  ) {
    a[d] = a[d] || b;
  }
})(
  (function() {
    try {
      console.log();
      return window.console;
    } catch (a) {
      return (window.console = {});
    }
  })()
);

/*! Copyright (c) 2013 - Peter Coles (mrcoles.com)
 *  Licensed under the MIT license: http://mrcoles.com/media/mit-license.txt
 */
(function() {
  // test if we can use blobs
  let canBlob = false;
  if (window.webkitURL && window.Blob) {
    try {
      new Blob();
      canBlob = true;
    } catch (e) {}
  }

  function asBytes(value, bytes) {
    // Convert value into little endian hex bytes
    // value - the number as a decimal integer (representing bytes)
    // bytes - the number of bytes that this value takes up in a string

    // Example:
    // asBytes(2835, 4)
    // > '\x13\x0b\x00\x00'
    let result = [];
    for (; bytes > 0; bytes--) {
      result.push(String.fromCharCode(value & 255));
      value >>= 8;
    }
    return result.join("");
  }

  function attack(i) {
    return i < 200 ? i / 200 : 1;
  }

  let DataGenerator = $.extend(
    function(styleFn, volumeFn, cfg) {
      cfg = $.extend(
        {
          freq: 440,
          volume: 32767,
          sampleRate: 11025, // Hz
          seconds: 0.5,
          channels: 1
        },
        cfg
      );

      let data = [];
      let maxI = cfg.sampleRate * cfg.seconds;
      for (let i = 0; i < maxI; i++) {
        for (let j = 0; j < cfg.channels; j++) {
          data.push(
            asBytes(
              volumeFn(
                styleFn(
                  cfg.freq,
                  cfg.volume,
                  i,
                  cfg.sampleRate,
                  cfg.seconds,
                  maxI
                ),
                cfg.freq,
                cfg.volume,
                i,
                cfg.sampleRate,
                cfg.seconds,
                maxI
              ) * attack(i),
              2
            )
          );
        }
      }
      return data;
    },
    {
      style: {
        wave: function(freq, volume, i, sampleRate, seconds) {
          // wave
          // i = 0 -> 0
          // i = (sampleRate/freq)/4 -> 1
          // i = (sampleRate/freq)/2 -> 0
          // i = (sampleRate/freq)*3/4 -> -1
          // i = (sampleRate/freq) -> 0
          return Math.sin(2 * Math.PI * (i / sampleRate) * freq);
        }},
      volume: {
        linearFade: function(data, freq, volume, i, sampleRate, seconds, maxI) {
          return volume * ((maxI - i) / maxI) * data;
        }}
    }
  );
  DataGenerator.style.default = DataGenerator.style.wave;
  DataGenerator.volume.default = DataGenerator.volume.linearFade;

  function toDataURI(cfg) {
    cfg = $.extend(
      {
        channels: 1,
        sampleRate: 11025, // Hz
        bitDepth: 16, // bits/sample
        seconds: 0.5,
        volume: 20000, //32767,
        freq: 440
      },
      cfg
    );

    //
    // Format Sub-Chunk
    //

    let fmtChunk = [
      "fmt ", // sub-chunk identifier
      asBytes(16, 4), // chunk-length
      asBytes(1, 2), // audio format (1 is linear quantization)
      asBytes(cfg.channels, 2),
      asBytes(cfg.sampleRate, 4),
      asBytes((cfg.sampleRate * cfg.channels * cfg.bitDepth) / 8, 4), // byte rate
      asBytes((cfg.channels * cfg.bitDepth) / 8, 2),
      asBytes(cfg.bitDepth, 2)
    ].join("");

    //
    // Data Sub-Chunk
    //

    let sampleData = DataGenerator(
      cfg.styleFn || DataGenerator.style.default,
      cfg.volumeFn || DataGenerator.volume.default,
      cfg
    );
    let samples = sampleData.length;

    let dataChunk = [
      "data", // sub-chunk identifier
      asBytes((samples * cfg.channels * cfg.bitDepth) / 8, 4), // chunk length
      sampleData.join("")
    ].join("");

    //
    // Header + Sub-Chunks
    //

    let data = [
      "RIFF",
      asBytes(4 + (8 + fmtChunk.length) + (8 + dataChunk.length), 4),
      "WAVE",
      fmtChunk,
      dataChunk
    ].join("");

    if (canBlob) {
      // so chrome was blowing up, because it just blows up sometimes
      // if you make dataURIs that are too large, but it lets you make
      // really large blobs...
      let view = new Uint8Array(data.length);
      for (var i = 0; i < view.length; i++) {
        view[i] = data.charCodeAt(i);
      }
      let blob = new Blob([view], { type: "audio/wav" });
      return window.webkitURL.createObjectURL(blob);
    } else {
      return "data:audio/wav;base64," + btoa(data);
    }
  }

  function noteToFreq(stepsFromMiddleC) {
    return 440 * Math.pow(2, (stepsFromMiddleC + 3) / 12);
  }

  let Notes = {
    sounds: {},
    getDataURI: function(n, cfg) {
      cfg = cfg || {};
      cfg.freq = noteToFreq(n);
      return toDataURI(cfg);
    }};

  window.DataGenerator = DataGenerator;
  window.Notes = Notes;
})();
