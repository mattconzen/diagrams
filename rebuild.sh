#!/bin/bash
set -euo pipefail

./autogen.sh

poetry build 

pip3 uninstall -y diagrams
pip3 install dist/*py3*.whl
