# Bilinear Form Category Semantics

Trigger: designing or reviewing modules with forms, lattice/module morphisms, dual maps, discriminant forms, cokernels of form-bearing objects, or category specs involving bilinear forms.

Owner note: `theory/foundations/bilinear-forms-duals-morphisms.md`.

Rules:

- Define the adjoint map abstractly first: `ad_beta(v) = beta(v, -)` as an element of the dual module. Matrix conventions come after the dual-basis expansion, not before.
- With basis `e_j` of `L` and dual basis `e_i^*`, `ad_beta(e_j) = sum_i beta(e_j, e_i) e_i^*`. A Gram matrix convention determines whether the representing matrix is `G` or `G^t`.
- For objects over a base algebra `S`, the form object is not just an `R`-module with an `R`-bilinear map. It is an `S`-module `L` with an `S`-bilinear form `b : Sym^2_S(L) -> M` or `L tensor_S L -> S/M` as specified.
- For a ring map `g : S_1 -> S_2`, morphisms should be formulated after base change to the target fiber: `S_2 tensor_{S_1} L_1 -> L_2` in `S_2`-modules, with the form diagram commuting there.
- The triple-morphism definition uses maps `(f, g, h)` where `g` is the algebra map and `f, h` are target-fiber maps after base change.
- Cokernels of form-bearing triple morphisms are not just cokernels of the underlying module maps. First compute the target-fiber cokernels, then quotient the coefficient cokernel by the images of cross-terms `beta_2(E * L_2)` where `E = im(f_{S_2})`.
- Recovering discriminant forms is not the specialization `S_1 = ZZ`, `S_2 = QQ`; the dual lattice `L#` is generally a `ZZ`-module, not a `QQ`-module.

Verification: category-spec or lattice work should be able to state the fiber, base-change functor, coefficient module, and descended form before introducing matrices.
