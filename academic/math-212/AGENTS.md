
## Desmos graphs

These apply to `desmos-graph` code blocks (Obsidian Desmos plugin):

- Use `r_0` (and `r_{0}` in expressions) instead of `r` for rate constants. Defining `r=` makes Desmos plot a polar curve instead of defining a variable.
- Write subscripts without braces in restrictions and variable definitions (`t_s`, not `t_{s}`). Otherwise the plugin errors with "subscripts may only contain letters and digits".
- Never use the `|` character inside an expression. The plugin splits every line on `|` into restrictions, so absolute values like `\left|x\right|` break the graph. Rewrite `\ln|x|` as `\frac{1}{2}\ln\left(x^{2}\right)`, or avoid absolute values entirely.
- Never put LaTeX like `\frac{1}{b-1}` inside a `|` restriction; write `1/(b-1)`. LaTeX there throws "Expected '{' to match '}'".
- Don't define helper functions like `F(u)=...`. The plugin plots them as a stray curve y=F(x), so inline the expression instead.