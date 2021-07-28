__version__ = "0.1.0"

import pytest

# https://docs.pytest.org/en/stable/writing_plugins.html#assertion-rewriting
pytest.register_assert_rewrite("nuts_experiments")
