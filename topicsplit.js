(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.TopicSplit = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // Stop words
  var STOP = new Set(("a an the and or but if then of to in on at by for with as is are was were be been being this that these those it its he she they we you i me my your our their from into about over under between which who what when where why how not no do does did have has had will would can could should may might must also than so such only own same each more most other some any all both few many one two three first second").split(" "));

  function sentences(text) {
    return text.replace(/s+/g, " ").match(/[^.!?]+[.!?]+|S[^.!?]*$/g).map(function (s) { return s.trim(); }).filter(Boolean);
  }

  function words(s) {
    return s.toLowerCase().replace(/[^a-z0-9s]/g, " ").split(/s+/).filter(function (w) { return w.length > 3 && !STOP.has(w); });
  }

  function overlap(a, b) {
    if (!a.length || !b.length) return 0;
    var sa = new Set(a), sb = new Set(b);
    var inter = 0;
    sa.forEach(function (w) { if (sb.has(w)) inter++; });
    return inter / (Math.sqrt(sa.size * sb.size) || 1);
  }

  function splitText(text, sens, skipTiny) {
    var sents = sentences(text);
    if (sents.length < 2) return sents;
    var ws = sents.map(words);
    var coh = [];
    for (var i = 0; i < sents.length - 1; i++) coh.push(overlap(ws[i], ws[i + 1]));
    var mean = coh.reduce(function (a, b) { return a + b; }, 0) / coh.length;
    var sd = Math.sqrt(coh.reduce(function (a, b) { return a + (b - mean) * (b - mean); }, 0) / coh.length);
    var thr = Math.max(0, mean - (sens / 100) * (mean + sd));
    var segs = [];
    var cur = [sents[0]];
    for (var j = 0; j < coh.length; j++) {
      if (coh[j] < thr) { segs.push(cur.join(" ")); cur = [sents[j + 1]]; }
      else cur.push(sents[j + 1]);
    }
    segs.push(cur.join(" "));
    if (skipTiny) {
      var out = [];
      for (var k = 0; k < segs.length; k++) {
        if (segs[k].split(/s+/).length < 6 && out.length) { out[out.length - 1] += " " + segs[k]; }
        else out.push(segs[k]);
      }
      return out;
    }
    return segs;
  }

  function renderMarkdown(segs) {
    return segs.map(function (g, i) { return "### Topic " + (i + 1) + "
" + g; }).join("

");
  }

  // Mount function for full UI
  function mount(element, options) {
    options = options || {};
    var sensitivity = options.sensitivity || 55;
    var skipTiny = options.skipTiny !== false;
    var showSample = options.showSample !== false;
    var showDigest = options.showDigest !== false;
    var showShare = options.showShare !== false;
    var showChallenge = options.showChallenge !== false;
    var showTipBar = options.showTipBar !== false;
    var theme = options.theme || 'dark';
    
    // ... (UI mounting logic would go here)
    element.innerHTML = '<p>TopicSplit mounted. Use splitText() and renderMarkdown() for programmatic access.</p>';
  }

  return {
    sentences: sentences,
    words: words,
    overlap: overlap,
    splitText: splitText,
    renderMarkdown: renderMarkdown,
    mount: mount,
    version: '1.6.0'
  };
}));
