import importlib.metadata

import {{ cookiecutter.project_slug }} as m


def test_version():
    assert importlib.metadata.version("{{ cookiecutter.project_slug }}") == m.__version__
