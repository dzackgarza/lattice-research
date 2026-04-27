import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.topological_spaces import TopologicalSpaces


T = TopologicalSpaces()
assert T.Constructors() is not None
assert T.Metric() is not None
