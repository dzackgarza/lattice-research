Paper: Dutour Sikirić–Hulek, arXiv:2302.01679 'Moduli of polarized Enriques surfaces -- computational aspects'. Relevant for isotropic Gamma-orbits and Sterk cusp counts.

Key facts:
- Section 'The Tits building' identifies 0- and 1-cusps of M_{En,h}=Gamma_h^+\D_N with Gamma_h^+-orbits of isotropic lines and isotropic planes in N=U+U(2)+E8(-2). Source TeX lines 1149-1153.
- For unpolarized Enriques surfaces O^+(N) has two isotropic-line and two isotropic-plane orbits, with explicit reps L1=Ze1, L2=Ze3, P1=Ze1+Ze3, P2=Z(2e1+2e2+w)+Ze3. Source lines 1155-1166.
- For subgroup Gamma_h, orbit splitting is done by double cosets: if xG is an ambient orbit and G_x its stabilizer, then xG decomposes into x_i Gamma_h corresponding to G = union G_x h_i Gamma_h. Source lines 1172-1178.
- They reduce this to a finite computation via U=~O(N) (kernel of discriminant action): because U normal and U subset Gamma_h, double cosets in O(N) reduce to double cosets in O(N)/~O(N) ~= O^+(F_2^10). Source lines 1182-1208.
- Therefore their practical cusp algorithm uses: ambient full-group orbits + stabilizer images in finite quotient + finite double-coset decomposition; not direct generator computation for Gamma_h inside O(N).
- Gamma_h is defined as pi_N^{-1}(pi_M(O(M,h))) and Gamma_h^+=Gamma_h cap O^+(N). Source lines 489-507.
- Table 1 case 1 (degree 2 polarization) has #I_1=5 and #I_2=9. Source lines 707-710 and 1270-1284. They explicitly say Sterk Section 4.4 proves five 0-cusps and nine 1-cusps for this case, agreeing with their Case 1.
- Their general isotropic algorithms are in Section 6: primitive isotropic vectors are handled by Theorem subsection_beta_norm_vectors (beta=0 case) using approximate models and degenerate complement isomorphism lifting, lines 1637-1660. Isotropic k-plane stabilizer/equivalence is Theorem theorem_isotropic_k_planes, lines 1665-1778. Enumeration of isotropic k-plane orbits is by induction, lines 1784-1809.

Implementation implication for repo:
- Existing Dawes backend is non-isotropic only and is not the right engine for Sterk five-cusp claim.
- A correct Sterk/Gamma_{En,2} implementation can likely reuse ambient isotropic-line/plane orbit enumeration and stabilizers from Dutour code, then split orbits to Gamma using finite quotient/discriminant-image data and subgroup membership in the quotient, without needing explicit generators of Gamma_{En,2} as an infinite subgroup of O(L).