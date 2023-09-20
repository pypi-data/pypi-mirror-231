# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

from pathlib import Path

# noinspection PyPackageRequirements
from setuptools import setup


def get_msgpack(pkg_dir: Path):
    if not pkg_dir.is_dir():
        raise NotImplementedError()


def get_package_data(pkg_dir: Path):
    data = {}
    for child in pkg_dir.rglob("*"):
        rel_child = child.relative_to(pkg_dir)
        root_parent = rel_child.parents[-1]
        if "msgpack-cxx" in str(root_parent) or "msgpack-cxx" in str(root_parent):
            # filter out any generated cache locations
            continue

        parent_pkg = ".".join(str(parent.name) for parent in reversed(rel_child.parents[:-1]))
        if parent_pkg in data:
            data[parent_pkg].append(str(child.name))
        else:
            data[parent_pkg] = [str(child.name)]
    return data


def prepare_pkg(setup_file: Path) -> dict:
    """

    Args:
        setup_file:
    Returns:

    """
    print(f"Build wheel from {setup_file}")
    pkg_dir = setup_file.parent
    return {
        "packages": '',
        "package_data": get_package_data(pkg_dir)
    }


setup(
    **prepare_pkg(setup_file=Path(__file__).resolve()),
)
