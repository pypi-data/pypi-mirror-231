__all__ = (
    "find_file",
    "PTHBuild",
    "PTHDevelop",
    "PTHEasyInstall",
    "PTHInstall",
    "PTHInstallLib",
)

import distutils.command.build
import fnmatch
import itertools
import os
from pathlib import Path
from typing import Optional, Union

import setuptools.command.develop
import setuptools.command.easy_install
import setuptools.command.install
import setuptools.command.install_lib


def find_file(pattern, data: Optional[Union[Path, str]] = None) -> list[Path]:
    """
    Find file with pattern"

    Examples:
        >>> from pths import find_file
        >>>
        >>> find_file('*.py', )   # doctest: +ELLIPSIS
        [PosixPath('.../pths/__init__.py'), ...

    Args:
        pattern:
        data: default cwd

    Returns:
        list of files found
    """
    result = []
    for root, _, files in os.walk(data or Path.cwd()):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(Path(os.path.join(root, name)))
    return result


pth_file: Optional[Union[Path, list[Path]]] = pth[0] \
    if (pth := find_file("*.pth", Path.cwd() / "src")) else None


class PTHBuild(distutils.command.build.build):
    def run(self):
        super().run()
        print(f"PTHBuild: {pth_file}")
        if pth_file:
            self.copy_file(str(pth_file), str(Path(self.build_lib, pth_file.name)))


class PTHDevelop(setuptools.command.develop.develop):
    def run(self):
        super().run()
        print(f"PTHDevelop: {pth_file}")
        if pth_file:
            self.copy_file(str(pth_file), str(Path(self.install_dir, pth_file.name)))


class PTHEasyInstall(setuptools.command.easy_install.easy_install):
    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)
        print(f"PTHEasyInstall: {pth_file}")
        if pth_file:
            self.copy_file(str(pth_file), str(Path(self.install_dir, pth_file.name)))


class PTHInstall(setuptools.command.install.install):
    def run(self):
        super().run()
        print(f"PTHInstall: {pth_file}")
        if pth_file:
            self.copy_file(str(pth_file), str(Path(self.install_lib, pth_file.name)))


class PTHInstallLib(setuptools.command.install_lib.install_lib):
    def run(self):
        super().run()
        print(f"PTHInstallLib: {pth_file}")
        if pth_file:
            dest = str(Path(self.install_dir, pth_file.name))
            self.copy_file(str(pth_file), dest)
            self.outputs = [dest]

    def get_outputs(self):
        return itertools.chain(setuptools.command.install_lib.install_lib.get_outputs(self), self.outputs)
