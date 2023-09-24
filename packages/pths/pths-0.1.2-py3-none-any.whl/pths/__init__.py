__all__ = (
    "exec_module_from_file",
    "find_file",
    "PTHBuild",
    "PTHDevelop",
    "PTHEasyInstall",
    "PTHInstall",
    "PTHInstallLib",
)

import distutils.command.build
import fnmatch
import importlib.util
import itertools
import os
import sys
import types
from pathlib import Path
from typing import Optional, Union

import setuptools.command.develop
import setuptools.command.easy_install
import setuptools.command.install
import setuptools.command.install_lib
from loguru import logger
from loguru_config import LoguruConfig

_config = {
    "handlers": [
        {
            "sink": "ext://sys.stderr",
            "format": "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                      "<level>{message}</level>: <level>{extra[source]}</level> -> <level>{extra[destination]}</level>",
        },
    ],
    "extra": {
        "source": "source",
        "destination": "destination",
    }
}

LoguruConfig.load(_config)


def exec_module_from_file(file: Union[Path, str]) -> types.ModuleType:
    """
    executes module from file location

    Args:
        file: file location

    Returns:
        Module instance
    """
    file = Path(file)
    spec = importlib.util.spec_from_file_location(file.stem, file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def find_file(pattern, data: Optional[Union[Path, str]] = None) -> list[Path]:
    """
    Find file with pattern"

    Examples:
        >>> from pths import find_file
        >>>
        >>> find_file('*.py', )   # doctest: +ELLIPSIS
        [PosixPath('.../pths/__init__.py')...

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


pth_files = pth if (pth := find_file("*.pth", Path.cwd() / "src")) else None


class PTHBuild(distutils.command.build.build):
    def run(self):
        super().run()
        _copy_pths(self, self.build_lib)


class PTHDevelop(setuptools.command.develop.develop):
    def run(self):
        super().run()
        _copy_pths(self, self.install_dir)


class PTHEasyInstall(setuptools.command.easy_install.easy_install):
    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)
        _copy_pths(self, self.install_dir)


class PTHInstall(setuptools.command.install.install):
    def run(self):
        super().run()
        self.outputs = _copy_pths(self, self.install_lib)
        for file in self.get_outputs():
            file = Path(file)
            if file.name == "install.py":
                exec_module_from_file(file)
                logger.info(self.__class__.__name__, source="executed", destination=file)
        logger.info(self.__class__.__name__, source=self.build_lib, destination=list(self.get_outputs()))

    def get_outputs(self):
        return itertools.chain(setuptools.command.install.install.get_outputs(self), self.outputs)


class PTHInstallLib(setuptools.command.install_lib.install_lib):
    def run(self):
        super().run()
        self.outputs = _copy_pths(self, self.install_dir)
        logger.info(self.__class__.__name__, source="outputs", destination=list(self.get_outputs()))

    def get_outputs(self):
        return itertools.chain(setuptools.command.install_lib.install_lib.get_outputs(self), self.outputs)


def _copy_pths(obj: Union[PTHBuild, PTHDevelop, PTHEasyInstall, PTHInstall, PTHInstallLib],
               directory: str) -> list[str]:
    if pth_files:
        outputs = []
        for item in pth_files:
            source = str(item)
            destination = str(Path(directory, item.name))
            logger.info(obj.__class__.__name__, source=source, destination=destination)
            obj.copy_file(source, destination)
            outputs.append(destination)
        return outputs
    return []
