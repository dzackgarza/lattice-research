The plan should be definition-first, not automation-first.                                                    
                                                                                                                
  Work order:                                                                                                   
                                                                                                                
  1. Extract vocabulary from the research formulas in use.                                                      
     Start only from objects already demanded by GOAL.md: Pic(S), f^*Pic(S), inclusions into H^2(X,Z), T =      
     (...)^\perp, discriminant forms, embeddings, O(L), stabilizers, centralizers, orbit sets.                  
                                                                                                                
  2. Define the universal category layer needed to state those formulas.                                        
     Sets, Rings, Groups, Hom, End, Aut, subobjects, quotients, finite/generated/presented refinements.         
     No algorithms yet beyond obligations implied by category membership.                                       
                                                                                                                
  3. Define the additive/module layer.                                                                          
     Modules, free finite-rank modules, finitely presented modules, generator-image homomorphisms, kernels/     
     images/cokernels, base change, duals.                                                                      
                                                                                                                
  4. Define formed modules and lattices.                                                                        
     Bilinear/quadratic forms, form-preserving morphisms, metric duals, lattice embeddings, primitive           
     sublattices, orthogonal complements.                                                                       
                                                                                                                
  5. Define finite torsion/discriminant and group-action vocabulary.                                            
     A_L = L#/L, quotient-valued forms, O(A_L,q_L), induced discriminant action, stabilizers, centralizers,     
     orbit sets under stated group categories.                                                                  
                                                                                                                
  6. Only then move to geometry vocabulary.                                                                     
     Schemes/varieties/surfaces/divisors/Picard groups are not “forgotten”; they are downstream of the lattice  
     language unless a current lattice definition needs them.                                                   
                                                                                                                
  Gap visibility should come from the spec itself: if Aut_C(X) is defined and needs Groups, then either Groups  
  exists or the Aut spec is visibly incomplete. If orthogonal_complement is needed, there should be a missing   

  method/stub/example exactly there, not a separate registry claiming to know the whole future vocabulary.


The actual plan should be:                                                                                                                                                                                          21:50:56 [20/970]

  1. Research-Need Extraction
     Start from the live formulas and tasks in GOAL.md: Pic(S), pullbacks, subobjects, orthogonal complements,
     discriminant forms, Aut, O(L), stabilizers, centralizers, orbit sets.
     Output: a bounded list of mathematical expressions the repo must eventually write.

  2. Vocabulary Decomposition
     For each expression, decompose it into required category nouns and operations.
     Example: O(L) requires lattice, formed-module morphism, End, Aut, group, possibly finite/generated/
     presented refinements later.
     This is where “do we even have Groups?” is checked.

  3. Existing Category Tree Check
     For each required noun, inspect whether the project already has the category object, subcategories/
     refinements, Hom/End/Aut hooks, and obligation examples.
     Output is not a meta-registry; it is a decision at the point of work: “this definition can be written now”
     or “this prerequisite category is missing.”

  4. Sage Surface Inventory
     For each missing or incomplete noun, inspect Sage categories, parents/elements, constructors, methods,
     examples, return types, and limitations.
     This decides whether the project aligns with Sage, wraps Sage, or owns a missing semantic layer.

  5. Spec Definition
     Only after the above: define the category/refinement and its obligations.
     Category membership carries computability obligations: group vs finite group vs finitely generated group vs
     finitely presented group vs generated subgroup.

  6. Use-Case Recheck
     Return to the original research expression and ask whether it can now be stated semantically.
     If not, the next missing noun/operation is exposed from the expression itself.

  7. Bounded Finalization
     The list is finalized when every expression required by the current lattice/spec phase can be written using
     defined categories, or is explicitly deferred because it belongs to the later geometry phase. Not before.

  So the next real move is not “implement groups.” It is to take one research expression, probably
  O(L)=Aut_Lattices(L), decompose it, and verify every required category noun exists before editing anything.

