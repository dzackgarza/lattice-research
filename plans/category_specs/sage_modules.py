from sage.categoriesObimodules import Bimodules
from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homset import Hom
from sage.categories.homsets import HomsetsCategory
from sage.categories.morphism import SetMorphism
from sage.categories.quotients import QuotientsCategory
from sage.categories.sets_cat import Sets
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.tensor import TensorProductFunctor, TensorProductsCategory, tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.dual import DualObjectsCategory
from .sage_module_morphism import RModuleHomsets, _RModMorphisms


# TODO: _cwa.all_axioms += ....
from sage.categories.category_singleton import Category_singleton  
from sage.categories.category import Category  
from sage.categories.objects import Objects  


# TODO: types
# Matrix
# vector
# Category
# RMod = Modules category class
# RModule = object M in RMod
# RModuleElement = element in some M
# RModHomset = Hom_R(M, N) for some M, N
# RModMorphism = element in some Hom_R(M, N)
# RModEndset = End_R(M) for some M
# RModEndomorphism = element in some End_R(M)
# RModAutset = Aut_R(M) for some M
# RModAutomorphism = element in some Aut_R(M)
# SubModule = element in RMod.Subobjects
# QuotientModule = element in RMod.Quotients
# RModTwistedForms = Category of twisted forms 
# TwistedForm = Object in RModTwistedForms
# RModDual = Modules dual category, equals linear twisted forms
# DualRModule = M^* for some RModule M, objects in RModDual
# Rings = promoted category of rings
# Ring = object in Rings
# Ideals = promoted category of ideals of R as a subcategory of Modules(R).Subobjects()
# Ideal = object in Ideals
# RingMorphism = morphism in Rings
# RingEndomorphism = endomorphism in Rings
# RingAutomorphism = automorphism in Rings

FinSet = Sets().Finite()
Cardinality = Integer | InfinityElement
ModuleStructure = Callable[Tuple[RingElement, RModuleElement], RModuleElement] | Callable[RingElement, RingEndomorphism]

class Categories(Category_singleton):  
    r"""
    A shim to define an infty-category of (sage) categories.
    """
    def super_categories(self):  
        return [Objects()]  
  
    @classmethod
    def __contains__(self, C: Any) -> bool:  
        return isinstance(C, Category)

    @classmethod
    def is_over_a_ring(self, C: Category) -> bool:
        assert C in Categories(), f"Object is not a category: {C}"

    @classmethod
    def base_ring(self, C: Category) -> Ring:
        base_ring_cat = next(D in C.super_categories() if hasattr(D, "base_ring"))
        assert base_ring_cat is not None, f"No super category of {C} is a category over a base ring."
        return base_ring_cat.base_ring()

class Modules(Category_module):

    def super_categories(self):
        R = self.base_ring()
        return [Bimodules(R, R)]

    def additional_structure(self):
        r"""
        Return None if this is a full subcategory of self.super_categories()
        Return self if this is a non-full subcategory.
        Here, R-Mod morphisms are exactly (R,R)-biMod morphisms.
        """
        return None

    # Constructors
    def zero_module(self) -> RModule: 
        ...
    def R(self) -> FreeModule:
        r"""Return R as a rank 1 free R-module."""
        ...
    def torsion_module(self, r: RingElement) -> TorsionModule: 
        r"""
        Return R/r. Assert R != 0.
        """
        ...

    def free_module(self, n: int) -> FreeModule:
        assert n in NN, f"Negative integers are not well-defined ranks: {n}"
        match n:
            case n == 0:
                return self.zero_module()
            case n >= 1:
                return sum(n*[self.R()])

    def from_ring_elements(self, elts: Sequence[RingElement]) -> RModule:
        r"""
        Given an ordered subset {r_1, ..., r_n} of R, return
        M := R/r_1 \oplus ... \oplus R/r_n, where R/0 := R.
        """
        if not elts: return self.zero_module()
        assert len(elts) > 0, f"Coding error."
        assert all(r.parent() in Rings for r in elts), f"All elements must be rings: {elts}"
        R = elts[0].parent()
        assert all(r.parent() is R for r in elts), f"Elements must be in a common ring: {(r.parent() for r in elts)}"
        zs, rs = partition_list(elts, lambda x: x.is_zero())
        F = self.free_module(len(zs))
        T = sum(self.torsion_module(r) for r in elts)
        return F + T

    def from_invariant_factors(self, elts: Sequence[RingElement]) -> RModule:
        return self.from_ring_elements(elts)

    def from_matrix(self, M: Matrix) -> RModule:
        r"""
        Interpret a matrix as a representation of a morphism f: R^n->R^n
        and return M := coker(f).
        """
        match M:
            case hasattr(M, "elementary_divisors"):
                return self.from_ring_elements(M.elementary_divisors())
            case hasattr(M, "smith_form"):
                D, _, _ = M.smith_form()
                return self.from_ring_elements(M.diagonal())
            case _:
                assert False, f"The matrix {M} over {R} does not appear to support elementary divisors or Smith normal form."
        

    class SubcategoryMethods:
        r"""
        Methods available on every subcategory, not just Modules(R).
        """
        @cached_method
        def base_ring(self) -> Ring:
            return Categories.base_ring(self)

        # Axiomatic subcategories

        ## Ring properties
        # TODO: attach axiom automatically based on R in init.

        @cached_method
        def OverIntegralDomain(self):
            return self._with_axiom("OverIntegralDomain")

        @cached_method
        def OverDedekindDomain(self):
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        def OverPID(self):
            return self._with_axiom("OverPID")

        @cached_method
        def OverCommutativeRing(self):
            return self._with_axiom("OverCommutativeRing")

        @cached_method
        def OverField(self):
            return self._with_axiom("OverField")

        @cached_method
        def OverLocalRing(self):
            return self._with_axiom("OverLocalRing")

        @cached_method
        def OverCompleteRing(self):
            return self._with_axiom("OverCompleteRing")

        ## Homological properties
        @cached_method
        def Free(self):
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
        return self._with_axiom("Torsion")
        
        @cached_method
        def Torsionfree(self):
            return self._with_axiom("Torsionfree")

        @cached_method
        def Projective(self):
            return self._with_axiom("Projective")

        ## Generation properties
        @cached_method
        def WithOrderedGeneratingSet(self):
            return self._with_axiom("WithOrderedGeneratingSet")

        @cached_method
        def FinitelyGenerated(self):
            return self._with_axiom("FinitelyGenerated")

        @cached_method
        def FinitelyPresented(self):
            return self._with_axiom("FinitelyPresented")

        # Functorial constructions
        @cached_method
        def Subobjects(self):
            return SubobjectsCategory.category_of(self)

        @cached_method
        def Quotients(self):
            return QuotientsCategory.category_of(self)

        @cached_method
        def TensorProducts(self):
            return TensorProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            return DualObjectsCategory.category_of(self)
        dual = DualObjects # Convenience

        ## Extra structure
        @cached_method
        def Filtered(self):
            return FilteredModulesCategory.category_of(self)

        @cached_method
        def Graded(self):
            return GradedModulesCategory.category_of(self)

        @cached_method
        def Super(self):
            return SuperModulesCategory.category_of(self)

        # Axiomatic extra structure
        def WithForm(self):
            return self._with_axiom("WithForm")

    ParentMethods = _RModObjects
    ElementMethods = _RModElements
    MorphismMethods = _RModMorphisms
    Homsets = RModuleHomsets
    
    # Named subcategories
    RIdeals = _RIdeals

    # Axiomatic subcategories
    Free = _Free
    Torsion = _Torsion
    Torsionfree = _Torsionfree
    Projective = _Projective
    
    ## Generation properties
    WithOrderedGeneratingSet = _WithOrderedGeneratingSet
    FinitelyGenerated = _FinitelyGenerated
    FinitelyPresented = _FinitelyPresented

    # Functorial constructions
    Subobjects = _Subobjects
    SubModules = Subobjects
    Quotients = _Quotients
    TensorProducts = _TensorProducts
    CartesianProducts = _CartesianProducts
    DualObjects = _DualObjects

    ## Extra structure
    Filtered = LazyImport('sage.categories.filtered_modules', 'FilteredModules')
    Graded = LazyImport('sage.categories.graded_modules', 'GradedModules')
    Super = LazyImport('sage.categories.super_modules', 'SuperModules')

    ##
    WithForms = _WithForms # Non-full subcategory of pairs (M, f)
    # Bilinear modules: (M, b) with b: M\otimes_R M -> S, may be degenerate.
    Bilinear = self.WithForms().Bilinear() 
    # Quadratic modules: (M, q): with q: M -> S^\sigma, may be degenerate.
    Quadratic = self.WithForms().Integral().Quadratic() 
    # Lattices: (M,b) with M a f.g. torsionfree R-module over a domain
    # and b a symmetric nondegenerate integral bilinear form.


Lattices = Modules(IntegralDomains()).FinitelyGenerated().TorsionFree().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
# Rational lattices: lattices where b is K-valued.
RationalLattices = Modules(IntegralDomains()).FinitelyGenerated().TorsionFree().OverIntegralDomain().WithForms().Bilinear().Symmetric().Nondegenerate().Rational()
# TODO: immediately restrict to Dedekind domains, then to PIDs
# So we need bilinear/quadratic modules and (rational) lattices over PIDs,
# which are thus free of finite rank


class _WithForms:
    class ParentMethods:
        def form(self) -> RModuleMorphism: ...

class _BilinearModules:
    class ParentMethods:
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v,w)

class _QuadraticModules:
    class ParentMethods:
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.form().q(v)
    
class _RModObjects: ...
    # linear_combination(...) not needed if elements are implemented properly
    
    @cached_method
    def tensor_square(self):
        return self.tensor_power(2)
    
    def tensor_power(self, n: int):
        match n:
            case n == 0:
                return self.base_ring()
            case n >= 1:
                return tensor(n*[self])
            case n <= -1:
                return tensor((-n)*[self.dual()])
            case _:
                assert_never()

    def tensor_module(self, p: int, q: int):
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        return tensor([self.tensor_power(p), self.dual().tensor_power(q)])

    def quotient(self, N: SubModule) -> QuotientModule:
        return N.inclusion().cokernel()

    @abstractmethod
    def annihilator(self) -> Ideal: ...

    def __truediv__(self, N: SubModule) -> QuotientModule:
        return self.quotient(N)

    def torsion_submodule(self) -> SubModule:
        r"""
        M_tors := <{m in M | r*m = 0 for some R in R}> = <{m\in M | Ann_R(m) != 0}>
        """
        ...

    def tensor_algebra(self) -> RModule:
        r"""
        Return T_R(M) := \bigoplus_{n} \bigoplus_{p+q=n} T_R(M)[p, q] as above.
        """
        ...

    def base_change(self, S: Ring) -> RModule: 
        r"""
        Return a representation of M_S := M \otimes_R S in S-Mod.
        """
        ...

    def module_structure(self) -> ModuleStructure:
        r"""
        The map \sigma: RxM->M such that r.m := sigma(r, m).
        Could also interpret as a ring morphism \sigma: R -> End_R(M) where
        r.m := \sigma(r)(m).
        This must be made explicit, so M can be twisted.
        """
        ...

    def modify_module_structure(self, sigma: ModuleStructure):
        r"""
        Define a new module structure \sigma': R -> End_R(M)
        so that r.m = \sigma'(r)(m) and not the existing \sigma(r)(m).
        """
        ...

    def symmetric_algebra(self) -> RModule: ...
    def alternating_algebra(self) -> RModule: ...
    def dual(self) -> DualRModule: ...
    def Hom(self, N: RModule) -> RModuleHomset: ...
    def End(self) -> RModuleEndSet: ...
    def Aut(self) -> RModuleAutSet: ...
    def determinant_module(self) -> RModule: 
        r"""
        Return \Lambda^n_R(M), the top exterior power of M.
        """
        ...

    def __contains__(self, data: RModuleElement | SubModule) -> bool:
        match data:
            case RModuleElement():
                return data.parent() is self
            case SubModule():
                return data.inclusion().codomain() is self
            case _:
                # Log issue.
                return false

    def cardinality(self) -> Cardinality: ...
    def is_finite(self) -> bool: ...
    def is_free(self) -> bool: ...
    def is_torsion(self) -> bool: ...
    def is_torsionfree(self) -> bool: ...
    def is_projective(self) -> bool: ...
    def is_isomorphic_to(self, other: RModule) -> bool: ...
    def is_submodule_of(self, other: RModule) -> bool: ...

    def direct_sum(self, other: RModule | Sequence[RModule]) -> RModule: ...
    def tensor(self, other: RModule | Sequence[RModule]) -> RModule: ...
    def span(self, elts: RModuleElement | Sequence[RModuleElement]): ...

    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)
    def __mul__(self, other: RingElement | RModule) -> RModule:
        match other:
            case RingElement():
                r"""r*M := the submodule spanned by {r*m | m in M}"""
                return self.span(other)
            case RModule():
                r"""N*M := the tensor product"""
                return self.tensor(other)
            case _:
                assert_never()

    # Do not define:
    # submodule(), _mul_, _rmul_, _lmul_
    def natural_pairing(self) -> RModuleForm:
        r"""
        The (1,1) form b: M\otimes_R M^* -> R defined by b(v,w^*) := w^*(v).
        """
        ...
    
class _RModElements:

    def span(self) -> SubModule: 
        return self.parent().span([self])

    def inclusion(self) -> RModMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    def annihilator(self) -> Ideal:
        return self.span().annihilator()

    def cyclic_submodule(self) -> SubModule: ...
    def is_primitive(self) -> bool:
        return self.span().inclusion().is_primitive()

    def __add__(self, m: RModuleElement) -> RModuleElement: ...
    def __mul__(self, r: RingElement) -> RModuleElement: ...
    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return R(-1) * self

    def _lmul_(self, r: RingElement) -> RModuleElement: ...
    def _rmul_(self, r: RingElement) -> RModuleElement: ...

    # TODO: define R*m := m.span() when R == m.base_ring(), or base-change.

# Functorial Constructions

class _DualObjects(DualObjectsCategory):
    _base_category_class = (Modules,)

    def extra_super_categories(self):
        r"""
        The dual M^* = Hom_R(M, R) of an R-module is a linear integral form,
        i.e. an element of Hom_R(M, R) = Modules(R).Homsets().Forms().Linear().Integral().
        """
        return [self.base_category().Homsets().Forms().Linear().Integral()]

class _Subobjects(SubobjectsCategory):
    r"""
    Extends RegressiveCovariantConstructionCategory, so C.Subobjects()
    will always be a subcategory of C.
    # TODO: what methods are already provided...?
    """

    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""
        Regard M is a submodule of itself via the identity.
        """
        ...

    class ParentMethods:
        def parent(self) -> RModule: ...

        @abstract_method
        def inclusion(self): ...

        @abstractmethod
        def intersect(self, N: SubModule) -> SubModule: ...

        def __and__(self, N: SubModule) -> SubModule: 
            return self.intersect(N)

        def index(self) -> Cardinality:
            return self.inclusion().index()
        
        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        def saturation(self) -> SubModule: ...

        def __leq__(self, other: RModule) -> bool: ...

        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()

class _Quotients(QuotientsCategory):
    r"""
    Extends RegressiveCovariantConstructionCategory, so C.Quotients()
    will always be a subcategory of C.
    # TODO: what methods are already provided...?
    """

    class ParentMethods:
        @abstract_method
        def projection(self): ...

    class ElementMethods:
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)

class _TensorProducts(TensorProductsCategory):
    r"""
    TODO: does r*(m_1 \otimes .... m_n) = (r*m_1 \otimes ... m_n) = (m_1 \otimes .... r*m_n) work and hold true...?
    """
    @cached_method
    def extra_super_categories(self):
        r"""
        Declare that M\otimes_R N is again an R-module.
        """
        return [self.base_category()]

    class ParentMethods:
        def construction(self):
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""
            Given an ordered set {m_1, ..., m_n} with m_i in M_i, where this module
            is M = M_1 \otimes_R ... \otimes_R M_n, lift the product element
            (m_1, ..., m_n) to m_1\otimes ... \otimes m_n.
            """
            ...

class _CartesianProducts(CartesianProductsCategory):
    def extra_super_categories(self):
        r"""
        Declare that MxN is again an R-module.
        """
        return [self.base_category()]

    class ParentMethods:
        def __init_extra__(self):
            factors = self._sets
            assert len(factors) > 0, f"No factors found in {self}: {factors}"
            R = factors[0].base_ring()
            assert all(Mi.base_ring() is R for Mi in factors)
            self._base = R

    class ElementMethods:
        def _lmul_(self, x: Any):
            return self.parent()._cartesian_product_of_elements(
                x * y for y in self.cartesian_factors()
            )

# Axiomatic subcategories 

class _Free(CategoryWithAxiom_over_base_ring):
    r"""
    Does not assume finitely generated or finitely presented.
    E.g. \bigoplus_{z\in CC} CC is a free CC-module.
    """

    def extra_super_categories(self):
        r"""
        Every free R-module is projective.
        """
        return [self.base_category().Projective()]

    class SubcategoryMethods:
        @cached_method
        def FiniteRank(self):
            r"""
            Rank is only well-defined for free modules.
            This is the subcategory where the rank is finite, so M \cong R^n for 
            some n < \infty.
            """
            return self._with_axiom("FiniteRank")
    
    FiniteRank = _FreeFiniteRank

    class ParentMethods:
        @abstract_method
        def rank(self) -> Cardinality:
            r"""
            Rank is only well-defined for free R-modules, and is the
            cardinality of any generating set (which may be infinite).
            """
            return self.gens().cardinality()

class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        r"""
        A finite rank free module is exactly a finitely generated
        free module.
        TODO: Should handle the fact that a finite rank
        free module over a finite ring is finite.
        TODO: need to externalize this category entirely.
        """
        # free module
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

class _Torsion(CategoryWithAxiom_over_base_ring):
    r"""
    TODO: a torsion module over a finite ring is finite.
    """
    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

class _Torsionfree(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        # override
        def annihilator(self) -> Ideal:
            r"""
            Ann_R(M) = <0>, the zero ideal of R regarded as an R-submodule of R.
            """
            R = self.base_ring()
            return R.ideal(R.zero())
    class ElementMethods: ...
    class MorphismMethods: ...

class _Projective(CategoryWithAxiom_over_base_ring): 
    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

## Generation properties 
class _WithOrderedGeneratingSet(CategoryWithAxiom_over_base_ring):
    r"""
    There exists an ordered set S = {s_1 <= s_2 <= ....} and a surjection
    f: R^S \cong R[s_1] \oplus R[s_2] \oplus .... -> M where the direct sum
    is ordered. S need not be finite.
    """

    class ParentMethods:
        @abstractmethod
        def gens(self) -> OrderedSet: ...

        @final
        def ngens(self) -> Cardinality: 
            return self.gens().cardinality()

        @final
        def gen(self, i):
            return self.gens()[i]

    class Homsets(HomsetsCategory):
        class ParentMethods:
            @abstractmethod
            def from_function(self, f: Callable[Any, Any]):
                r"""
                A morphism f: M_1 -> M_2 can be defined from a set-theoretic 
                function f: S_1 -> S_2 on the generating sets.
                """
                ...
    class ElementMethods: 
    class MorphismMethods: 
        def to_function(self) -> Callable[RModuleElement, RModuleElement]: ...
            
class _FinitelyGenerated(CategoryWithAxiom_over_base_ring):
    r"""
    Modules M which admit a surjection f: R^n -> M for some n < infty.
    This implies there is a preferred choice of a generating set.
    This does not imply M is finitely presented: ker(f) may not
    be finitely generated. See e.g. any ideal I in a non-Noetherian ring.
    """
    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

class _FinitelyPresented(CategoryWithAxiom_over_base_ring):
    r"""
    Modules M that can be written as <S|R> where S \subseteq M is a finite
    generating set and R is a finite set of relations.
    All such modules can be written as M := coker_R(f: R^n -> R^n) for some n.
    All finitely presented modules are finitely generated: finitely generated
    means there exists a surjection f: R^n -> R for some n, but finitely
    presented means ker(f) is finitely generated. A counterexample that 
    shows strict implication: if R is non-Noetherian, then there is an ideal
    I which is not finitely generated. Then R/I is not finitely presented,
    since the presentation is 0 -> I -> R -> R/I -> 0.
    """
    def extra_super_categories(self):
        r"""
        Finitely presented means there is a preferred finite presentation.
        """
        result = [self.base_category().FinitelyGenerated()]
        match R := self.base_ring():
            case isinstance(R, Category) and R.is_subcategory(FinSet):
                r"""
                Modules(PrincipalIdealDomains()) makes sense, so "base_ring"
                may actually be a category of rings.
                If this is a subcategory of finite rings, then we encode 
                that a finitely presented module over a finite ring is finite.
                """
                result += [FinSet]
            case R in FinSet:
                r"""
                Similarly, if R is a finite ring, finitely presented R-modules
                are finite.
                """
                result += [FinSet]
        return result



# TODO: on specific subcategory:
# to_matrix
# identify when Hom_R(M, N) is a matrix algebra
# identify when End_R(M) is a matrix algebra
# identify when Aut_R(M) is a subgroup of (GL_n(R), *)
# iteration on countable objects
# __contains__ methods
# to/from_X for X = dict, images, matrix, function
