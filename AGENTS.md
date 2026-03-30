`sage` is on the path at /home/dzack/miniforge3/envs/sage/bin/sage

Do not install system packages, use a uv venv

Use a justfile to encode common functionality or hard-won or error-prone workflows

Your work in this repo is completely autonomous.

Do NOT use any tools that block progress entirely, like ask_question or submit_plan,
unless the user specifically asks you.

Before every Aristotle use, first review the `aristotle` skill.

Any Aristotle formalization attempt must begin by checking whether the target result
already exists upstream in mathlib or other imported dependencies.
Do not spend Aristotle budget reproving upstream results when the correct action is to
find and reuse the existing theorem.

Computational validation must prefer exact arithmetic throughout whenever Sage can
support it. Prefer integral or rational coefficients, exact polynomial/system solving,
and small or minimal examples that avoid coefficient blowup.
Do not treat floating-point approximations as acceptable audit evidence when exact
algebraic data is available.
When singular points or other solutions are algebraic but not rational, base change to a
natural number field or exact algebraic extension and continue exact work there rather
than deduplicating or validating numerically.

For arXiv papers, always prefer the arXiv LaTeX/source payload over PDF OCR whenever the
source is available.
Use OCR only for non-source papers, scanned sources, or figures that the source does not
capture.

For lattice computations, note that CARAT may be useful when an exact computation of
integral orthogonal groups, normalizers, or orbit/stabilizer data is needed.
In particular, review `Aut_grp`, `Normalizer`, and `Orbit` before building custom search
code for finite positive-definite cases.
