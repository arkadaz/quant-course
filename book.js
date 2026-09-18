/* Quant Masterclass: one script shared by every page.
 *
 * 1. Draws the LaTeX written in each page with MathJax.  Formulas are text in
 *    the HTML: fix a formula by editing its LaTeX, nothing else.
 * 2. Adds the small visual aids that follow from the text, so the HTML never
 *    has to carry them: a colour for each formula's role, step badges for
 *    "ขั้นที่ N —" headings, labels on worked-example beats, and the
 *    formula/figure counter at the top of a topic.
 */
(function () {
  'use strict';

  // MathJax 4 (it can break a long formula onto several lines on a phone) is
  // shipped inside the book, in mathjax/, so the book works offline and from a
  // zip.  Its location is worked out from where this script was loaded.
  var BASE = (document.currentScript && document.currentScript.src || '').replace(/[^\/]*$/, '');
  var MATHJAX_URL = BASE + 'mathjax/tex-mml-chtml.js';

  var ROLE_LABELS = {
    input: 'ของที่ใส่เข้าไป',
    condition: 'เงื่อนไข / น้ำหนัก',
    result: 'คำตอบ',
    risk: 'ความเสี่ยง / ขอบเขต'
  };
  var RESULT = ['\\boxed', '\\therefore', '\\rightarrow', 'คำตอบ', 'ผลลัพธ์', 'สรุป', 'result', 'conclusion', 'final'];
  var RISK = ['\\operatorname{var}', '\\mathrm{var}', 'var', 'cvar', 'variance', 'volatility', 'drawdown', 'loss', 'risk', 'constraint', 'ความเสี่ยง', 'ขาดทุน', 'ข้อจำกัด'];
  var CONDITION = ['\\mid', '\\mathbb{p}', '\\pr', 'probability', 'likelihood', 'posterior', 'condition', 'weight', 'เงื่อนไข', 'ความน่าจะเป็น', 'น้ำหนัก'];
  var ACTION = ['คำนวณ', 'แทนค่า', 'รวม', 'บวก', 'ลบ', 'คูณ', 'หาร', 'แก้หา', 'หา ', 'ยุบ', 'แปลง', 'ตรวจ', 'derive', 'calculate', 'solve'];

  function any(probe, tokens) {
    for (var i = 0; i < tokens.length; i++) {
      if (probe.indexOf(tokens[i]) >= 0) return true;
    }
    return false;
  }

  function roleOf(tex, heading) {
    var probe = (heading + ' ' + tex).toLowerCase();
    if (any(probe, RESULT)) return 'result';
    if (any(probe, RISK)) return 'risk';
    if (any(probe, CONDITION)) return 'condition';
    if (any(probe, ACTION)) return 'result';
    return 'input';
  }

  function firstText(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    var node = walker.nextNode();
    while (node && !node.nodeValue.trim()) node = walker.nextNode();
    return node;
  }

  var STEP = /^\s*(?:ขั้นที่|ขั้น|step)\s*(\d+)\s*(?:[—–:-]\s*)?/i;

  function decorateFormula(section) {
    var heading = section.querySelector(':scope > h4');
    var math = section.querySelector(':scope > .math');
    var role = roleOf(math ? math.textContent : '', heading ? heading.textContent : '');
    section.classList.add('role-' + role);

    var key = document.createElement('div');
    key.className = 'formula-role-key';
    key.innerHTML = '<span aria-hidden="true"></span>';
    key.appendChild(document.createTextNode(ROLE_LABELS[role]));
    section.insertBefore(key, section.firstChild);

    if (!heading) return;
    var text = firstText(heading);
    var match = text && STEP.exec(text.nodeValue);
    if (!match) return;
    text.nodeValue = text.nodeValue.slice(match[0].length);
    var wrap = document.createElement('div');
    wrap.className = 'step-heading';
    var badge = document.createElement('span');
    badge.className = 'step-number';
    badge.setAttribute('aria-label', 'ขั้นที่ ' + match[1]);
    badge.textContent = match[1];
    heading.parentNode.insertBefore(wrap, heading);
    wrap.appendChild(badge);
    wrap.appendChild(heading);
  }

  var BEATS = [
    ['โจทย์ให้อะไรมาบ้าง:', 'example-givens', 'ของที่โจทย์ให้'],
    ['ของที่มี:', 'example-givens', 'ของที่โจทย์ให้'],
    ['คำถาม:', 'example-question', 'ลองตอบก่อน'],
    ['ถามว่า', 'example-question', 'ลองตอบก่อน'],
    ['ถาม:', 'example-question', 'ลองตอบก่อน'],
    ['คำตอบและความหมาย:', 'example-answer-line', 'คำตอบ'],
    ['คำตอบ:', 'example-answer-line', 'คำตอบ'],
    ['ตรวจเองใน 10 วินาที:', 'example-self-check', 'ตรวจเองใน 10 วินาที'],
    ['ตรวจคำตอบใน 10 วินาที:', 'example-self-check', 'ตรวจเองใน 10 วินาที'],
    ['เอาไปใช้จริง:', 'example-meaning', 'เอาไปใช้จริง'],
    ['แปลว่าอะไร:', 'example-meaning', 'แปลว่าอะไร']
  ];

  function labelBeats(section) {
    var paragraphs = section.querySelectorAll(':scope > p');
    for (var i = 0; i < paragraphs.length; i++) {
      var p = paragraphs[i];
      var text = firstText(p);
      if (!text) continue;
      var value = text.nodeValue.replace(/^\s+/, '');
      for (var j = 0; j < BEATS.length; j++) {
        if (value.indexOf(BEATS[j][0]) !== 0) continue;
        text.nodeValue = value.slice(BEATS[j][0].length).replace(/^\s+/, '');
        p.classList.add(BEATS[j][1]);
        var label = document.createElement('span');
        label.className = 'teaching-label';
        label.textContent = BEATS[j][2];
        p.insertBefore(label, p.firstChild);
        break;
      }
    }
  }

  var INTRO = ['worked example', 'โจทย์', 'คำถามที่เรากำลังตอบ', 'เริ่มจาก', 'เริ่มที่', 'เริ่มด้วย'];
  var ANSWER = ['คำตอบ', 'answer', 'ตรวจเอง', 'เช็กคำตอบ'];

  function enhance() {
    var i;
    var formulas = document.querySelectorAll('section.formula');
    for (i = 0; i < formulas.length; i++) decorateFormula(formulas[i]);

    var examples = document.querySelectorAll('section.example');
    for (i = 0; i < examples.length; i++) {
      var h = examples[i].querySelector(':scope > h4');
      if (h && any(h.textContent.toLowerCase(), ANSWER)) examples[i].classList.add('answer');
      labelBeats(examples[i]);
    }

    var prose = document.querySelectorAll('section.prose');
    for (i = 0; i < prose.length; i++) {
      var ph = prose[i].querySelector(':scope > h4');
      if (ph && any(ph.textContent.toLowerCase(), INTRO)) {
        prose[i].classList.add('worked-intro');
        labelBeats(prose[i]);
      }
    }

    var topic = document.querySelector('article.topic');
    var takeaways = topic && topic.querySelector('section.takeaways');
    if (topic && takeaways) {
      var id = 't' + (topic.getAttribute('data-number') || '').replace('.', '-') + '-summary';
      takeaways.id = id;
      var tools = document.createElement('nav');
      tools.className = 'topic-tools';
      tools.setAttribute('aria-label', 'ทางลัดในหัวข้อนี้');
      tools.innerHTML = '<span>' + topic.querySelectorAll('.math').length + ' สูตร · ' +
        topic.querySelectorAll('figure.plot').length + ' รูป</span><a href="#' + id + '">ดูสรุปก่อน ↓</a>';
      var anchor = topic.querySelector(':scope > .hook') || topic.querySelector(':scope > header');
      anchor.parentNode.insertBefore(tools, anchor.nextSibling);
    }
  }

  // A formula that still does not fit gets a fade at its right edge, so the
  // reader can see there is more to swipe to.
  function markScrollingFormulas() {
    var boxes = document.querySelectorAll('.math');
    for (var i = 0; i < boxes.length; i++) {
      boxes[i].classList.toggle('scrolls', boxes[i].scrollWidth > boxes[i].clientWidth + 12);
    }
  }

  window.bookMathErrors = [];
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$']],
      displayMath: [['\\[', '\\]']],
      processEscapes: true,
      // An undefined command must show as an error, not quietly as red text.
      packages: { '[-]': ['noundefined'] },
      formatError: function (jax, err) {
        window.bookMathErrors.push(err.message);
        return jax.formatError(err);
      }
    },
    output: {
      // A formula wider than a phone breaks onto more lines instead of
      // running off the edge.  ('scale' was tried: it shrank formulas until
      // they were hard to read and still clipped them.)
      displayOverflow: 'linebreak',
      linebreaks: { inline: true, width: '85%' },
      // MathJax normally enlarges formulas to match the Thai font's x-height,
      // but then breaks lines as if they were unenlarged, so wide formulas
      // never wrapped on a desktop.  A fixed scale keeps the two in step.
      matchFontHeight: false,
      scale: 1.15
    },
    loader: {
      paths: { mathjax: BASE + 'mathjax', fonts: BASE + 'mathjax/fonts' }
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
      // These need a Web Worker, which a page opened from disk may not start.
      enableEnrichment: false,
      enableSpeech: false,
      enableBraille: false,
      enableComplexity: false,
      enableExplorer: false,
      menuOptions: {
        settings: { enrich: false, speech: false, braille: false, collapsible: false, assistiveMml: true }
      }
    },
    startup: {
      pageReady: function () {
        try { enhance(); } catch (e) { window.bookMathErrors.push('enhance: ' + e.message); }
        return window.MathJax.startup.defaultPageReady().then(function () {
          markScrollingFormulas();
          window.addEventListener('resize', markScrollingFormulas);
          document.documentElement.setAttribute('data-math', 'ready');
        });
      }
    }
  };

  var script = document.createElement('script');
  script.src = MATHJAX_URL;
  script.async = true;
  document.head.appendChild(script);
})();
