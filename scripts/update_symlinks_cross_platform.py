#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""
This script will update the symlinks of the project, cross-platform compatible.
"""
import inspect
import os
import subprocess
from functools import reduce
from pathlib import Path
from typing import List, Tuple

SCRIPTS_PATH = Path(os.path.dirname(inspect.getfile(inspect.currentframe())))  # type: ignore
ROOT_PATH = SCRIPTS_PATH.parent
TEST_DATA = ROOT_PATH / "tests" / "data"
TEST_DUMMY_AEA_DIR = TEST_DATA / "dummy_aea"
FETCHAI_PACKAGES = ROOT_PATH / "packages" / "fetchai"

SYMLINKS = [
    (TEST_DUMMY_AEA_DIR / "skills" / "dummy", TEST_DATA / "dummy_skill"),
    (
        TEST_DUMMY_AEA_DIR / "vendor" / "fetchai" / "protocols" / "default",
        ROOT_PATH / "aea" / "protocols" / "default",
    ),
    (
        TEST_DUMMY_AEA_DIR / "vendor" / "fetchai" / "protocols" / "fipa",
        FETCHAI_PACKAGES / "protocols" / "fipa",
    ),
    (
        TEST_DUMMY_AEA_DIR / "vendor" / "fetchai" / "connections" / "local",
        FETCHAI_PACKAGES / "connections" / "local",
    ),
    (
        TEST_DUMMY_AEA_DIR / "vendor" / "fetchai" / "contracts" / "erc1155",
        FETCHAI_PACKAGES / "contracts" / "erc1155",
    ),
    (
        TEST_DUMMY_AEA_DIR / "vendor" / "fetchai" / "skills" / "error",
        ROOT_PATH / "aea" / "skills" / "error",
    ),
]  # type: List[Tuple[Path, Path]]
"""A list of pairs: (link_path, target_path)"""


def do_symlink(link_path: Path, target_path: Path):
    """
    Change directory and call the cross-platform script.

    The working directory must be the parent of the symbolic link name
    when executing 'create_symlink_crossplatform.sh'. Hence, we
    need to translate target_path into the relatve path from the
    symbolic link directory to the target directory.

    So:
    1) from link_path, extract the number of jumps to the parent directory
      in order to reach the repository root directory, and chain many "../" paths.
    2) from target_path, compute the relative path to the root
    3) relative_target_path is just the concatenation of the results from step (1) and (2).


    For instance, given
    - link_path: './directory_1//symbolic_link
    - target_path: './directory_2/target_path

    we want to compute:
    - link_path: 'symbolic_link' (just the last bit)
    - relative_target_path: '../../directory_1/target_path'

    The resulting command on UNIX systems will be:

        cd directory_1 && ln -s ../../directory_1/target_path symbolic_link

    """
    working_directory = link_path.parent
    target_relative_to_root = target_path.relative_to(ROOT_PATH)
    cwd_relative_to_root = working_directory.relative_to(ROOT_PATH)
    nb_parents = len(cwd_relative_to_root.parents)
    root_relative_to_cwd = reduce(
        lambda x, y: x / y, [Path("../")] * nb_parents, Path(".")
    )

    link_name = link_path.name
    target = root_relative_to_cwd / target_relative_to_root
    args = [
        "bash",
        str(ROOT_PATH / "scripts" / "create_symlink_crossplatform.sh"),
        str(link_name),
        str(target),
    ]
    print("Calling '{}'".format(" ".join(args)))
    subprocess.call(args, cwd=str(working_directory.absolute()))


if __name__ == "__main__":
    for link_name, target in SYMLINKS:
        print("Linking {} to {}".format(link_name, target))
        try:
            link_name.unlink()
        except FileNotFoundError:
            pass
        do_symlink(link_name, target)
