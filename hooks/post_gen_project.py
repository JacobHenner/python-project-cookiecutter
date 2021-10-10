#!/usr/bin/env python3

import subprocess

# Init git repository (needed for pre-commit)
subprocess.check_call(["git", "init"])

# Install dependencies into virtualenv
subprocess.check_call(["poetry", "install"])

# Install pre-commit hooks
subprocess.check_call(["poetry", "run", "pre-commit", "install"])
