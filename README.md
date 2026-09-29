# Technical Archives

Hi! I'm Leo Winston, a sophomore at Emory.

My math and computer science notes, written in plain Markdown: the courses I take, the subjects I teach myself, and the work I want to keep.

I study applied math because it's the major that lets me follow my own interests as far as I want, and it bends around whatever I'm curious about instead of the other way around. Math didn't start as a love for me. It started with the thrill of working through a hard problem, and I kept chasing that feeling until it turned into the reason, so I decided to major in the thing I actually enjoy and keep falling deeper into it.

What keeps me going is the click. I'll be learning something new, go back to a textbook I thought I already understood, and suddenly the two ideas come together and each one makes more sense than it did on its own. That happens all the time now, and every time it does, it shows me a little more clearly what I want to become an expert in. Technical Archives is where I write those connections down so I can find them again and build on them.

## How I work

- **Short topic notes, long explorations.** A topic note holds the definition, the key result, and only the steps that matter. The full derivations and worked numbers go in exploration, workbook, or example notes that link back to it.
- **Math before tools.** When I code the math, I use plain numpy instead of a framework so I can see how it actually works.
- **Keep going after the course ends.** The self-study folders follow whatever a class left me curious about. I started convex optimization because I want to think about problems the way Boyd says the course teaches you to, and graph theory and ergodic theory grew out of it.
- **Link everything.** When one subject explains another, the notes cross-link, so the positive semidefinite matrices in convex optimization point to the graph Laplacian in graph theory, and Huffman coding sits next to the information theory it comes from.
- **My own words.** Proofs and reports in the archive are kept as I wrote them. Only the LaTeX was changed where it had to be.

## What's here

```
├── academic/
│   ├── math-212/               Differential equations: topics and Workbook 1 solutions
│   └── math-315/               Numerical analysis: topics and explorations
├── self-study/
│   ├── probability/            Notes and worked problems
│   ├── convex-optimization/    Boyd & Vandenberghe, Ch. 1 to §4.5, with NumPy and Desmos explorations
│   ├── graph-theory/           Kelly's Cambridge notes through Hall's theorem, plus some curiosities in spectral graph theory
│   └── ergodic-theory/         Measure-theory foundations — Patrick Billingsley's Ergodic Theory and Information
├── archive/
│   ├── proofs/                 Math 250 (Foundations of Math) proof portfolios and my own exploration proofs
│   ├── experiments/            CS 253 experimental analyses with MATLAB plots
│   └── dsa-problem-generator/  Python CLI that turns a seed into a solved CS 253 practice problem in LaTeX/TikZ
└── preamble.sty                Shared LaTeX macros for the whole repo
```

Each folder has an `Index.md` that is the **place to start.**

**`academic/` vs. `archive/`.** As of fall 2026, Math 212 and Math 315 are courses I'm taking right now. For those two courses, as well as the self-study notes, they are built as in-depth exploration tools I study from week to week, so they are constantly moving around as I explore. The archive is different: it holds finished work from past courses, kept as it was turned in.

## Reading this Repo

Everything here is plain Markdown with LaTeX math, so the notes stay portable and readable in any editor, with nothing locked into one app. The notes link to each other with `[[wiki links]]` because that's how the ideas actually connect, and following a link from one subject into another is the whole point.

- **On GitHub**, the notes and most of the math render directly. Wiki links show as plain text, and the custom macros in `preamble.sty` (like `\P`, `\E`, and `\R`) won't render.
- **In a Markdown editor** that supports wiki links and MathJax, the links become clickable and the notes read as a connected graph. [Obsidian](https://obsidian.md) is one example: open the repo root as a vault and turn off Restricted Mode, and the included Desmos, MathJax, and Latex Suite plugins switch on and load the preamble macros. Any similar editor works too.
- **To run the code**, create the virtual environment at the repo root with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`. The notes use NumPy and yfinance, and the DSA problem generator needs only the standard library.
- **Coming later:** I plan to publish this on GitHub Pages and eventually turn it into a real personal website and portfolio. This repository is the foundation for that.

Note-writing rules, including the index-link format, live in [AGENTS.md](AGENTS.md).
