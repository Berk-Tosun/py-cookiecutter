# ruff: noqa: S602
# ruff: noqa: S603
# ruff: noqa: S607

import subprocess

subprocess.run(
    [r"{{ cookiecutter.path_to_python_exe_for_venv }}", "-m", "venv", "venv"],
    # check=True
)

#############################################################################

subprocess.run(
    ["git", "init"],
    check=True,
)

#############################################################################

subprocess.run(
    ["make", "update"],
    # shell=True,
    check=True
)

##############################################################################

subprocess.run(
    ["git", "add", "--all"],
    check=True,
)
subprocess.run(
    [
        # fmt: off
        "git", "commit", "--message", "build: initialized from template",
        # fmt: on
    ],
    # check=True
)
subprocess.run(["git", "branch", "-M", "main"])
