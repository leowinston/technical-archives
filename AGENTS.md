# Technical Archives Rules

This is an Obsidian vault of math and CS notes: current courses in `academic/` (`math-212`, `math-315`), independent study in `self-study/` (`probability`, `convex-optimization`, `graph-theory`, `ergodic-theory`), and finished past work in `archive/`, kept as it was turned in. Follow these rules whenever you create or edit notes here.

## Links

- In note bodies, write standard Markdown links with a path relative to the current note and the `.md` extension: `[Condition Number](Topics/Condition%20Number.md)`. Never write `[[wikilinks]]` in a body, because GitHub shows them as plain text.
- Encode spaces in the path as `%20`. Match the file name's exact capitalization, because GitHub paths are case-sensitive.
- Encode only spaces. Write other characters in a file name literally (`=`, `^`, `&`, `+`), never as `%3D` or `%5E`. Obsidian leaves reserved characters such as `%3D` undecoded, so the link looks for a file that doesn't exist and shows "file not created yet".
- After writing links, check that each decoded path (only `%20` turned back into spaces) resolves to a real file.
- Link to a heading with GitHub's anchor form: lowercase, punctuation dropped, spaces turned into `-` (`#2--rejection-sampling-keeps-only-instructive-instances`).
- Embed images and PDFs as `![file.png](../Assets/file.png)`.
- Frontmatter properties such as `topics:` stay as quoted `"[[wikilinks]]"`, because Obsidian links properties only in that form.
- Why: Markdown links work as note links in Obsidian and as clickable links in the GitHub code view.

## Index links

- Write the "Back to" line as `Back to [Index](../Index.md)`, using the relative path to the note's own folder's `Index.md`.
- Why: each folder has its own `Index.md`, so the link must be a path, never a bare name.

## Topic note length

- Keep each subsection of a Topics note brief: a one-line lead-in, the key formula or boxed result, and at most a short pseudocode block or a 1–2 line example.
- Aim for the density of the math-212 Topics, about 100–250 words per note. Show only the key steps of a derivation.
- Put long derivations and worked numbers in the Explorations or Workbook notes instead.

## LaTeX macros

- Every custom macro lives in the one `preamble.sty` at the vault root, under its subject's section. Never create a second preamble or define macros inside a note.
- After editing `preamble.sty`, run `python tools/macros.py`. It rewrites the `ALL_MACROS.push(...)` list in `.obsidian/plugins/obsidian-latex-suite/data.json`, which Latex Suite needs so it doesn't split a macro while typing (`\SD` → `\S D`). Never edit that list by hand.
- The site needs no extra step. `.github/site/prepare.py` turns `preamble.sty` into the MathJax macro config on every build, and `.github/site/check_math.js` typesets every formula and warns about any command that is not defined.
- Then tell the user to quit Obsidian fully (Cmd+Q) and reopen it. The preamble loads only at startup, so new macros won't render until then.
- Close inline math tight against its content: `$z =$`, never `$z = $`. A space before the closing `$` leaves the math as plain text on the site.

## Graphs

- Never put a `desmos-graph` block in a note that is published. The block only draws inside Obsidian; GitHub and the site show it as code.
- A graph is a spec file `Assets/<name>.desmos` (same syntax as the Desmos plugin) plus the `Assets/<name>.svg` drawn from it, in the Assets folder of the note's section. The note embeds the SVG: `![Logistic Growth, figure 1](../Assets/logistic-growth-1.svg)`.
- To add or change a graph, edit the `.desmos` file and run `python tools/figures.py`. To convert a note that still has `desmos-graph` blocks, run `python tools/figures.py --convert "<note>"`. Commit the `.desmos` and the `.svg` together.
- `python tools/figures.py --check` draws every spec and every remaining block without writing anything.
- For a plot the spec syntax can't express (data, heatmaps, 3D), write a short matplotlib script, save an SVG into the same Assets folder, and embed it the same way.

## Publishing and the review queue

- The site (GitHub Pages, built by `.github/workflows/pages.yml`) publishes exactly the files git tracks. Tracking a note is publishing it.
- The folders listed under "Review queue" in `.gitignore` are local-only by default. A note in them is published only after the user approves it, with `git add -f "<note>"`. Never force-add a note the user has not approved, and never `git add -A` a folder to get around this.
- `.workspace/Review Queue.md` (local-only) lists what is waiting. When you write or change notes the user hasn't read, add them there instead of publishing them, unless the user asked for them to be published.
- Source documents (handouts, exams, lecture photos, raw transcriptions, chat logs, `.tex`, `.ipynb`) are never committed. Notes may link to them; the site build shows a link to anything unpublished as plain text.
- Each course has a public `Index.md` (published notes only) and a local `Local Index.md` (everything on this machine). Add a note to `Index.md` only when it is published.
- Preview the site with `python .github/site/prepare.py && mkdocs build -f .github/site/mkdocs.yml` (add `--all` to `prepare.py` to preview unpublished notes too).
