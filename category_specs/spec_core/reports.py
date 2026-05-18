"""Minimal typed report kernel for category specification obligations."""

from __future__ import annotations

from collections.abc import Sequence
from functools import cached_property
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator


class SpecObligation(BaseModel):
    """A requirement inherited from a declared category or construction."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    source: str = Field(min_length=1)
    description: str = ""


class SpecProvider(BaseModel):
    """A declared provider that directly satisfies obligations."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(min_length=1)
    category: str = Field(min_length=1)
    provides: tuple[str, ...] = ()
    source: str = Field(min_length=1)
    description: str = ""


class ConstructionWitness(BaseModel):
    """Evidence that a construction satisfies obligations for a target object."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(min_length=1)
    construction: str = Field(min_length=1)
    source_category: str = Field(min_length=1)
    target_category: str = Field(min_length=1)
    provides: tuple[str, ...] = ()
    source: str = Field(min_length=1)
    description: str = ""


class ComputedValue(BaseModel):
    """A report value computed by a provider or construction witness."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(min_length=1)
    value: str = Field(min_length=1)
    source: str = Field(min_length=1)


class SpecCheckResult(BaseModel):
    """One obligation classified by the report kernel."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    status: Literal["satisfied_by_provider", "satisfied_by_witness", "missing"]
    obligation: SpecObligation
    provider: SpecProvider | None = None
    witness: ConstructionWitness | None = None

    @model_validator(mode="after")
    def provider_witness_matches_status(self) -> Self:
        if self.status == "satisfied_by_provider":
            if self.provider is None or self.witness is not None:
                raise ValueError("provider result requires exactly one provider")
        elif self.status == "satisfied_by_witness":
            if self.witness is None or self.provider is not None:
                raise ValueError("witness result requires exactly one witness")
        elif self.provider is not None or self.witness is not None:
            raise ValueError("missing result cannot include provider or witness")
        return self


class SpecReport(BaseModel):
    """A categorized report for inherited obligations on one subject."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    subject: str = Field(min_length=1)
    declared_category: str = Field(min_length=1)
    inherited_obligations: tuple[SpecObligation, ...] = ()
    satisfied_by_provider: tuple[SpecCheckResult, ...] = ()
    satisfied_by_witness: tuple[SpecCheckResult, ...] = ()
    computed_values: tuple[ComputedValue, ...] = ()
    missing_obligations: tuple[SpecCheckResult, ...] = ()

    def all_results(self) -> tuple[SpecCheckResult, ...]:
        return (
            *self.satisfied_by_provider,
            *self.satisfied_by_witness,
            *self.missing_obligations,
        )

    def is_complete(self) -> bool:
        return not self.missing_obligations


class SpecRegistry(BaseModel):
    """Registry that resolves inherited obligations into report buckets."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    obligations: tuple[SpecObligation, ...] = ()
    providers: tuple[SpecProvider, ...] = ()
    witnesses: tuple[ConstructionWitness, ...] = ()

    @cached_property
    def obligations_by_id(self) -> dict[str, SpecObligation]:
        return _obligations_by_id(self.obligations)

    @cached_property
    def providers_by_obligation(self) -> dict[str, SpecProvider]:
        return _providers_by_obligation(self.providers)

    @cached_property
    def witnesses_by_obligation(self) -> dict[str, ConstructionWitness]:
        return _witnesses_by_obligation(self.witnesses)

    def report(
        self,
        *,
        subject: str,
        declared_category: str,
        inherited_obligation_ids: Sequence[str],
        computed_values: Sequence[ComputedValue] = (),
    ) -> SpecReport:
        inherited_obligations = self._inherited_obligations(inherited_obligation_ids)
        satisfied_by_provider: list[SpecCheckResult] = []
        satisfied_by_witness: list[SpecCheckResult] = []
        missing_obligations: list[SpecCheckResult] = []

        for obligation in inherited_obligations:
            provider = self.providers_by_obligation.get(obligation.id)
            if provider is not None:
                satisfied_by_provider.append(
                    SpecCheckResult(
                        status="satisfied_by_provider",
                        obligation=obligation,
                        provider=provider,
                    )
                )
                continue

            witness = self.witnesses_by_obligation.get(obligation.id)
            if witness is not None:
                satisfied_by_witness.append(
                    SpecCheckResult(
                        status="satisfied_by_witness",
                        obligation=obligation,
                        witness=witness,
                    )
                )
                continue

            missing_obligations.append(
                SpecCheckResult(status="missing", obligation=obligation)
            )

        return SpecReport(
            subject=subject,
            declared_category=declared_category,
            inherited_obligations=inherited_obligations,
            satisfied_by_provider=tuple(satisfied_by_provider),
            satisfied_by_witness=tuple(satisfied_by_witness),
            computed_values=tuple(computed_values),
            missing_obligations=tuple(missing_obligations),
        )

    def _inherited_obligations(
        self, inherited_obligation_ids: Sequence[str]
    ) -> tuple[SpecObligation, ...]:
        obligations: list[SpecObligation] = []
        for obligation_id in inherited_obligation_ids:
            obligation = self.obligations_by_id.get(obligation_id)
            if obligation is None:
                raise ValueError(f"unknown inherited obligation id: {obligation_id}")
            obligations.append(obligation)
        return tuple(obligations)


def _obligations_by_id(
    obligations: Sequence[SpecObligation],
) -> dict[str, SpecObligation]:
    indexed: dict[str, SpecObligation] = {}
    for obligation in obligations:
        if obligation.id in indexed:
            raise ValueError(f"duplicate obligation id: {obligation.id}")
        indexed[obligation.id] = obligation
    return indexed


def _providers_by_obligation(
    providers: Sequence[SpecProvider],
) -> dict[str, SpecProvider]:
    indexed: dict[str, SpecProvider] = {}
    for provider in providers:
        for obligation_id in provider.provides:
            if obligation_id in indexed:
                raise ValueError(f"duplicate provider for obligation: {obligation_id}")
            indexed[obligation_id] = provider
    return indexed


def _witnesses_by_obligation(
    witnesses: Sequence[ConstructionWitness],
) -> dict[str, ConstructionWitness]:
    indexed: dict[str, ConstructionWitness] = {}
    for witness in witnesses:
        for obligation_id in witness.provides:
            if obligation_id in indexed:
                raise ValueError(f"duplicate witness for obligation: {obligation_id}")
            indexed[obligation_id] = witness
    return indexed
