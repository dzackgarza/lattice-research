On 2026-04-10, tested ore_algebra against /home/dzack/miniforge3/envs/sage (conda-forge Sage 10.7, Python 3.12.13, libflint 3.3.1) while researching repo need for ore_algebra-based monodromy/Picard-Fuchs work.

Findings:
- Current ore_algebra master resolved by pip to commit 2904d75321ef50f5b02b5e8bc355c7d9d74a484f and fails to build on this env in src/ore_algebra/analytic/dac_sum_c.c because _fmpq_poly_interpolate_fmpq_vec is undeclared; local Sage/conda headers expose only _fmpq_poly_interpolate_fmpz_vec in include/flint/fmpq_poly.h.
- Upstream issue #155 (2026-04-01) matches this exact failure and proposes the fmpq->fmpz patch in dac_sum_c.pyx. A temporary checkout with that patch built and imported successfully on this env.
- The immediate parent commit before the March 8 2026 Flint change, afbe4dad50bd63f5b2ce112193555d6f9740e0d3, also builds and imports successfully here.
- Tagged release 0.5 is not a clean fallback on this env: metadata generation failed before compilation because its older setup.py uses broad sage.env.cython_aliases() and raised pkgconfig PackageNotFoundError for fflas-ffpack.
- Even when build/import succeeds with either the Flint patch or pre-regression commit, analytic runtime on conda Sage 10.7 is still broken: a monodromy_matrices() probe on the Legendre operator failed with TypeError 'C variable sage.rings.integer._small_primes_table has wrong signature'. This reproduces upstream issue #150 behavior.
- Upstream issue #150 comments indicate this _small_primes_table problem was seen on conda/prebuilt Sage builds; reporter eventually said installing ore_algebra with passagemath instead of sagemath avoided the issue.
- Most useful local workaround: force ore_algebra setup.py to disable Cython extensions entirely (pure-Python install path). A temporary master checkout patched to set extensions=[] via the existing old-Sage fallback logic built as a pure Python wheel, imported, and successfully ran monodromy_matrices() for the Legendre example on this exact env. Warnings reported slower Python fallbacks in local_solutions.py and naive_sum.py, but the analytic API worked.

Practical guidance:
- For immediate use on this machine, prefer a no-Cython ore_algebra install over trying to fix the Cython extensions under conda Sage. It avoids both the Flint 3 build break and the _small_primes_table analytic runtime break.
- If performance of analytic routines becomes unacceptable, next candidates are: (1) a separate passagemath-based environment, or (2) deeper Sage/ore_algebra ABI work; a full source-built Sage replacement is higher effort and had mixed upstream reports in issue #150, so it should not be first-line.
- If only symbolic/non-analytic ore_algebra features are needed, patched master or afbe4dad are viable on this env.