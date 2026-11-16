# Technical Archives Rules

This is an Obsidian vault of math and CS notes, published as a site at https://leowinston.github.io/technical-archives/. Follow these rules whenever you create or edit notes here.

## Layout

- `academic/`: current courses (`math-212`, `math-315`). `self-study/`: independent study (`probability`, `convex-optimization`, `graph-theory`, `ergodic-theory`). `archive/`: finished past work, kept as it was turned in.
- Each section has an `Index.md`, its note folders (`Topics 1/`, `Explorations 2/`, `Theory/`, ...), and an `Assets/` folder for figures.
- `preamble.sty`: every custom LaTeX macro. `tools/`: `figures.py` draws the graphs, `macros.py` syncs the macros, `backup_held.py` snapshots the notes git isn't tracking. `.github/site/`: the MkDocs build.
- `.workspace/`: local-only. `Review Queue.md` there lists the notes waiting for the user's approval.

## Publishing and the review queue

- The site publishes exactly the files git tracks on `main`. Tracking a note is publishing it, so the user decides what gets tracked.
- The folders listed under "Review queue" in `.gitignore` are local-only by default: in `math-212`, every `Topics`, `Workbook`, `Practice Test`, and `Mock Exam` folder; in `math-315`, every `Explorations` folder plus `Practice Test`, `PS5`, the labs, and `Topics 4`; and all of `self-study/probability`. Notes already tracked in them stay tracked, so edits to published notes show up in git as usual.
- A new note the user has not read is not published, wherever it lives. In a review-queue folder it is ignored automatically. Anywhere else (`self-study/`, `math-315/Topics 1` to `3`), leave it unstaged. Either way, add it to `.workspace/Review Queue.md`. The one exception is a note the user asked to have published.
- To publish a note the user approved:
  1. If it has a `desmos-graph` block, run `python tools/figures.py --convert "<note>"`.
  2. `git add -f "<note>"`, plus any new files in `Assets/`. Force-add single files only, never a folder: `git add -f` on a folder also adds everything else git was ignoring in it.
  3. Add the note to its section's `Index.md`.
  4. Take it off `.workspace/Review Queue.md`.
- To un-publish a note, run `git rm --cached "<note>"`, remove it from `Index.md`, and add it to the review queue. The file stays on disk. It also stays in git history, so tell the user that.
- Source documents are never committed: handouts, exams, lecture photos and figures taken from handouts, raw transcriptions, chat logs, `.tex`, `.ipynb`. Notes may link to them.
- Notes that were never committed exist only on this machine. Never delete or overwrite one without asking.
- Git treats ignored files as disposable. Switching to a branch or commit where a held note was tracked overwrites the local copy, and switching back deletes it. This is how Workbook 1 was lost on 2026-11-16 and had to be restored from history. So:
  - Run `python tools/backup_held.py` before un-publishing notes and before any `git checkout`, `git switch`, `git merge`, `git pull`, `git stash`, or `git reset`. It snapshots every untracked note into `.workspace/backups/`.
  - Work on `main`. Do not create a branch for vault work and do not tell the user to switch branches. If a branch is unavoidable, use `git worktree add` in a folder outside the vault so this working copy never changes branch.
  - Never run `git clean`.
- Commit only when asked, and never push without being asked. A push to `main` deploys the site.
- Why: the user wants every published note to be one they have worked through themselves.

## Links

- In note bodies, write standard Markdown links with a path relative to the current note and the `.md` extension: `[Condition Number](Topics%201/Condition%20Number.md)`. Never write `[[wikilinks]]` in a body, because GitHub shows them as plain text.
- Encode spaces in the path as `%20`. Match the file name's exact capitalization, because GitHub paths are case-sensitive.
- Encode only spaces. Write other characters in a file name literally (`=`, `^`, `&`, `+`), never as `%3D` or `%5E`. Obsidian leaves reserved characters such as `%3D` undecoded, so the link looks for a file that doesn't exist and shows "file not created yet".
- After writing links, check that each decoded path (only `%20` turned back into spaces) resolves to a real file.
- A published note may link to an unpublished note or a source document. Keep the link: it works in Obsidian, and the site build turns it into plain text. A list item that is only such a link is dropped from the site.
- Link to a heading with GitHub's anchor form: lowercase, punctuation dropped, spaces turned into `-` (`#2--rejection-sampling-keeps-only-instructive-instances`).
- Embed images as `![file.png](../Assets/file.png)`.
- Frontmatter properties such as `topics:` stay as quoted `"[[wikilinks]]"`, because Obsidian links properties only in that form.
- Why: Markdown links work as note links in Obsidian, as clickable links in the GitHub code view, and on the site.

## Indexes

- Write the "Back to" line as `Back to [Index](../Index.md)`, using the relative path to the note's own section's `Index.md`. Each section has its own `Index.md`, so the link must be a path, never a bare name.
- `Index.md` is public and lists published notes only. A section with nothing published (`probability` right now) has no public index at all: its `Index.md` is held with the notes. Add a note to it when the note is published, not before.
- `math-212` and `math-315` also have a `Local Index.md`, which is git-ignored and lists everything on this machine. Add every new note there, published or not.

## Topic note length

- Keep each subsection of a Topics note brief: a one-line lead-in, the key formula or boxed result, and at most a short pseudocode block or a 1–2 line example.
- Aim for the density of the math-212 Topics, about 100–250 words per note. Show only the key steps of a derivation.
- Put long derivations and worked numbers in the Explorations or Workbook notes instead.

## LaTeX

- Every custom macro lives in the one `preamble.sty` at the vault root, under its subject's section. Never create a second preamble or define macros inside a note.
- After editing `preamble.sty`, run `python tools/macros.py`. It rewrites the `ALL_MACROS.push(...)` list in `.obsidian/plugins/obsidian-latex-suite/data.json`, which Latex Suite needs so it doesn't split a macro while typing (`\SD` → `\S D`). Never edit that list by hand.
- Then tell the user to quit Obsidian fully (Cmd+Q) and reopen it. The preamble loads only at startup, so new macros won't render until then.
- The site needs no extra step: the build turns `preamble.sty` into the MathJax macro config every time.
- Close inline math tight against its content: `$z =$`, never `$z = $`. A space before the closing `$` leaves the math as plain text on the site.
- GitHub's own Markdown view does not load `preamble.sty`, so custom macros show as errors there. That is expected. The site is the place where everything renders.

## Graphs

- Never put a `desmos-graph` block in a published note. The block draws only inside Obsidian; GitHub and the site show it as code. Notes that are still local may keep their blocks until they are approved.
- A graph is a spec file `Assets/<name>.desmos` (the Desmos plugin's syntax) plus the `Assets/<name>.svg` drawn from it, in the Assets folder of the note's section. The note embeds the SVG: `![Logistic Growth, figure 1](../Assets/logistic-growth-1.svg)`.
- To add or change a graph, edit the `.desmos` file and run `python tools/figures.py`. To convert a note that still has blocks, run `python tools/figures.py --convert "<note>"`. Commit the `.desmos` and the `.svg` together.
- A spec line is one of: `y=f(x)`, `x=g(y)` or `x=c`, an implicit `F(x,y)=G(x,y)`, a point `(a,b)`, a shaded `y\ge f(x)`, or a parameter (`K=4`, or `y_{0}=[1,2,3]` for one curve per value). After the expression, separated by `|`: restrictions (`x>=0`), `dashed`, `dotted`, `open`, and a `#rrggbb` colour.
- The spec pitfalls in `academic/math-212/AGENTS.md` apply to every spec in the vault: no `|` inside an expression, no helper functions like `F(u)=...`, and `r_0` instead of `r`.
- For a plot the spec syntax can't express (data, heatmaps, 3D), write a short matplotlib script, save an SVG into the same Assets folder, and embed it the same way.
- Look at the SVG after drawing it. A spec that parses can still draw the wrong picture.

## Checks before committing

- `python tools/figures.py --check` draws every spec and every remaining block and reports the ones that fail.
- `python tools/macros.py --check` fails if the Latex Suite list is out of step with `preamble.sty`.
- To preview the site and test every formula:
  ```
  pip install -r .github/site/requirements.txt && npm ci --prefix .github/site
  python .github/site/prepare.py && mkdocs build -f .github/site/mkdocs.yml
  node .github/site/check_math.js
  ```
  `prepare.py` stages tracked files only; add `--all` to preview unpublished notes too. `check_math.js` reports every formula that fails to typeset or uses an undefined command. The same check runs on every push and shows problems as warnings on the workflow run.
- Run `git status` before committing and confirm nothing from a review-queue folder, `node_modules`, or `.workspace/` is staged unless the user approved it.
