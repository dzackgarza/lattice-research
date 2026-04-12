from __future__ import annotations

from collections.abc import Sequence


class DiscriminantGroupHomSpace:
    def __init__(self, domain, codomain):
        self._domain = domain
        self._codomain = codomain
        self._element_cls = DiscriminantGroupMorphism

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def element_from_images(self, images: Sequence):
        image_tuple = tuple(images)
        assert len(image_tuple) == len(self._domain.gens()), (
            "A discriminant-group morphism is determined by images of all generators"
        )
        assert all(image.parent() is self._codomain for image in image_tuple), (
            "Generator images must lie in the codomain"
        )
        sage_images = tuple(image._sage_like() for image in image_tuple)
        sage_morphism = self._domain._sage_like().hom(sage_images, self._codomain._sage_like())
        return self._element_cls(self._domain, self._codomain, sage_morphism)

    def __contains__(self, morphism):
        return isinstance(morphism, DiscriminantGroupMorphism) and morphism.domain() is self._domain and morphism.codomain() is self._codomain


class DiscriminantGroupMorphism:
    def __init__(self, domain, codomain, sage_morphism):
        self._domain = domain
        self._codomain = codomain
        self._sage_morphism = sage_morphism

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def _sage_like(self):
        return self._sage_morphism

    def __call__(self, value):
        from src.lattices.core.discriminant import DiscriminantGroupElement

        element = value if isinstance(value, DiscriminantGroupElement) else self._domain(value)
        return self._codomain(self._sage_morphism(element._sage_like()))

    def image(self):
        return self._codomain._from_sage_like(self._sage_morphism.image(), lattice=self._codomain.lattice())

    def lift(self, value):
        from src.lattices.core.discriminant import DiscriminantGroupElement

        element = value if isinstance(value, DiscriminantGroupElement) else self._codomain(value)
        return self._domain(self._sage_morphism.lift(element._sage_like()))
