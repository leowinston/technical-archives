# Technical Archives Rules

This is an Obsidian vault of math and CS notes: current courses in `academic/` (`math-212`, `math-315`), independent study in `self-study/` (`probability`, `convex-optimization`, `graph-theory`, `ergodic-theory`), and finished past work in `archive/`, kept as it was turned in. Follow these rules whenever you create or edit notes here.

## Links

- In note bodies, write standard Markdown links with a path relative to the current note and the `.md` extension: `[Condition Number](Topics/Condition%20Number.md)`. Never write `[[wikilinks]]` in a body, because GitHub shows them as plain text.
- Encode spaces in the path as `%20`. Match the file name's exact capitalization, because GitHub paths are case-sensitive.
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
- When you add a macro, also add its name to the `ALL_MACROS.push(...)` list at the top of the `snippets` string in `.obsidian/plugins/obsidian-latex-suite/data.json`. Otherwise Latex Suite splits it while typing (`\SD` → `\S D`).
- After editing either file, tell the user to quit Obsidian fully (Cmd+Q) and reopen it. The preamble loads only at startup, so new macros won't render until then.
