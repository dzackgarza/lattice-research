r"""Smoke surface for the generic homsets subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.homsets import Homsets


failures = []

Homsets()
Homsets().Endset()
Homsets().Autset()

assert not failures, "\n".join(failures)
