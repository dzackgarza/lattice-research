"""Minimal typed report kernel for category specification obligations."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


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

    def report(
        self,
        *,
        subject: str,
        declared_category: str,
        inherited_obligation_ids: Sequence[str],
        computed_values: Sequence[ComputedValue] = (),
    ) -> SpecReport:
        obligations_by_id = _obligations_by_id(self.obligations)
        providers_by_obligation = _providers_by_obligation(self.providers)
        witnesses_by_obligation = _witnesses_by_obligation(self.witnesses)

        inherited_obligations = tuple(
            obligations_by_id[obligation_id]
            for obligation_id in inherited_obligation_ids
        )
        satisfied_by_provider: list[SpecCheckResult] = []
        satisfied_by_witness: list[SpecCheckResult] = []
        missing_obligations: list[SpecCheckResult] = []

        for obligation in inherited_obligations:
            provider = providers_by_obligation.get(obligation.id)
            if provider is not None:
                satisfied_by_provider.append(
                    SpecCheckResult(
                        status="satisfied_by_provider",
                        obligation=obligation,
                        provider=provider,
                    )
                )
                continue

            witness = witnesses_by_obligation.get(obligation.id)
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
            indexed.setdefault(obligation_id, provider)
    return indexed


def _witnesses_by_obligation(
    witnesses: Sequence[ConstructionWitness],
) -> dict[str, ConstructionWitness]:
    indexed: dict[str, ConstructionWitness] = {}
    for witness in witnesses:
        for obligation_id in witness.provides:
            indexed.setdefault(obligation_id, witness)
    return indexed
