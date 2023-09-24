__all__ = (
    "exec_module_from_file",
    "PostInstall",
    "PTHBuildPy",
    "PTHDevelop",
    "PTHEasyInstall",
    "PTHInstallLib",
)

import importlib.util
import itertools
import sys
import types
from pathlib import Path
from typing import Union

import setuptools.command.build_py
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
            "format": "<level>{level: <8}</level> <red>|</red> "
                      "<cyan>{name}</cyan> <red>|</red> "
                      "<blue><level>{message}</level></blue><red>:</red> <level>{extra[source]}</level> "
                      "<red>-></red> <level>{extra[destination]}</level>",
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

    Examples:
        >>> import pths
        >>> m = pths.exec_module_from_file(pths.__file__)
        >>> assert m.__name__ == pths.__name__

    Args:
        file: file location

    Returns:
        Module instance
    """
    file = Path(file)
    spec = importlib.util.spec_from_file_location(file.parent.name if file.name == "__init__.py" else file.stem, file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PostInstall(setuptools.command.install.install):
    """Runs "post_install.py" after install"""

    def run(self):
        super().run()
        # self.build_lib = build/lib
        # self.get_outputs() = ['build/bdist.macosx-12-x86_64/wheel/huti/functions.py'...
        for file in self.get_outputs():
            file = Path(file)
            if file.name in ["_post_install.py", "post_install.py"]:
                exec_module_from_file(file)
                logger.info(self.__class__.__name__, source="executed", destination=file)


class PTHBuildPy(setuptools.command.build_py.build_py):
    """Build py with pth files installed"""

    def run(self):
        super().run()
        self.outputs = []
        self.outputs = _copy_pths(self, self.build_lib)

    def get_outputs(self, include_bytecode=1):
        return itertools.chain(setuptools.command.build_py.build_py.get_outputs(self, 0), self.outputs)


class PTHDevelop(setuptools.command.develop.develop):
    def run(self):
        super().run()
        _copy_pths(self, self.install_dir)


class PTHEasyInstall(setuptools.command.easy_install.easy_install):
    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)
        _copy_pths(self, self.install_dir)


class PTHInstallLib(setuptools.command.install_lib.install_lib):
    def run(self):
        super().run()
        self.outputs = []
        self.outputs = _copy_pths(self, self.install_dir)

    def get_outputs(self):
        return itertools.chain(setuptools.command.install_lib.install_lib.get_outputs(self), self.outputs)


def _copy_pths(obj: Union[PTHBuildPy, PTHDevelop, PTHEasyInstall, PTHInstallLib],
               directory: str) -> list[str]:
    outputs = []
    data = obj.get_outputs() if isinstance(obj, (PTHBuildPy, PTHInstallLib)) else obj.outputs
    for source in data:
        if source.endswith(".pth"):
            destination = str(Path(directory, Path(source).name))
            logger.info(obj.__class__.__name__, source=source, destination=destination)
            obj.copy_file(source, destination)
            outputs.append(destination)
    return outputs


setuptools.command.build_py._IncludePackageDataAbuse = lambda x: None
