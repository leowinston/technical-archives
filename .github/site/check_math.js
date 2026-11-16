// Typeset every formula on the built site with the same MathJax and the same
// preamble macros the browser uses, and report the ones that fail.
//
//   node .github/site/check_math.js            (after mkdocs build)
//
// Exits 1 if any formula has an error or an undefined command, so a macro that
// was used in a note but never added to preamble.sty is caught before it ships.
const fs = require("fs");
const path = require("path");
const { mathjax } = require("mathjax-full/js/mathjax.js");
const { TeX } = require("mathjax-full/js/input/tex.js");
const { SVG } = require("mathjax-full/js/output/svg.js");
const { liteAdaptor } = require("mathjax-full/js/adaptors/liteAdaptor.js");
const { RegisterHTMLHandler } = require("mathjax-full/js/handlers/html.js");
const { AllPackages } = require("mathjax-full/js/input/tex/AllPackages.js");

const root = path.resolve(__dirname, "../..");
const site = path.join(root, "_site");
const config = fs.readFileSync(path.join(site, "javascripts/mathjax.js"), "utf8");
const macros = JSON.parse(config.match(/macros: (\{[\s\S]*?\n\})/)[1]);

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
// `noundefined` would turn unknown commands into red text; leaving it out makes them errors.
const packages = AllPackages.filter((p) => p !== "noundefined" && p !== "physics");
const doc = mathjax.document("", { InputJax: new TeX({ packages, macros }), OutputJax: new SVG({ fontCache: "none" }) });

const unescape = (s) =>
  s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&");

function* pages(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) yield* pages(p);
    else if (e.name.endsWith(".html")) yield p;
  }
}

let total = 0;
const failures = [];
for (const page of pages(site)) {
  const html = fs.readFileSync(page, "utf8");
  for (const m of html.matchAll(/<(span|div) class="arithmatex">([\s\S]*?)<\/\1>/g)) {
    const src = unescape(m[2]).trim();
    const display = src.startsWith("\\[");
    total++;
    let error = null;
    try {
      const out = adaptor.outerHTML(doc.convert(src.slice(2, -2), { display }));
      const hit = out.match(/data-mjx-error="([^"]*)"/);
      if (hit) error = hit[1];
    } catch (e) {
      error = e.message;
    }
    if (error) failures.push({ page: path.relative(site, path.dirname(page)), error, src: src.slice(2, 120).replace(/\s+/g, " ") });
  }
  // inline math the Markdown step never recognised, e.g. `$z = $` with a space before the closing $
  const article = (html.match(/<article[\s\S]*?<\/article>/) || [""])[0]
    .replace(/<(span|div) class="arithmatex">[\s\S]*?<\/\1>/g, "")
    .replace(/<pre[\s\S]*?<\/pre>/g, "")
    .replace(/<code[\s\S]*?<\/code>/g, "")
    .replace(/<[^>]+>/g, "");
  for (const line of article.split("\n")) {
    if (/\$[^$\n]*\\[A-Za-z]+|\$[^$\n]{1,60}\$/.test(line))
      failures.push({ page: path.relative(site, path.dirname(page)), error: "math left as plain text", src: unescape(line).trim().slice(0, 120) });
  }
}

for (const f of failures) {
  console.log(`::warning title=Math error::${f.page}: ${f.error}: ${f.src}`);
}
console.log(`${total} formulas checked, ${failures.length} problem(s)`);
process.exit(failures.length ? 1 : 0);
