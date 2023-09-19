import os
from typing import List, Union
from contextlib import contextmanager
from pathlib import Path
import sys
import shutil
from shshsh import Sh
from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry.factory import Factory
from cleo.io.inputs.option import Option
from poetry_plugin_export.exporter import Exporter
from setuptools import setup, find_packages


@contextmanager
def _temp_argv(argv: List[str]):
    old_argv = sys.argv
    sys.argv = argv
    try:
        yield
    except Exception as e:
        raise e
    finally:
        sys.argv = old_argv


@contextmanager
def _temp_cwd(cwd: Union[Path, str]):
    old_cwd = os.getcwd()
    os.chdir(str(cwd))
    try:
        yield
    except Exception as e:
        raise e
    finally:
        os.chdir(old_cwd)


def _copy_to_inner_dir(src: Union[Path, str], dst: Union[Path, str], excludes: List[str]):
    dst_path = Path(dst)
    for each in os.listdir(src):
        each_path = Path(each)
        if each_path.absolute() == dst_path.absolute():
            continue

        if each_path.is_dir():
            shutil.copytree(src=each, dst=dst_path / each, symlinks=True, ignore=shutil.ignore_patterns(*excludes))
        else:
            shutil.copy(src=each, dst=dst)


class AssemblyCmd(Command):
    name = "assembly"
    options = [
        Option("poetry-assembly-tmp", default="./.poetry-assembly", flag=False),
        Option("yes", shortcut="y"),
        Option("excludes", is_list=True, flag=False, default=[]),
    ]

    def handle(self) -> int:
        project_path = Path(self.option("poetry-assembly-tmp"))
        if len(os.listdir(project_path)) and not self.option("yes"):
            self.line_error("temp directory is not empty")
            if not input("do you want to delete it? [y/N] ").lower() == "y":
                return 1

        shutil.rmtree(project_path, ignore_errors=True)
        project_path.mkdir(parents=True)
        _copy_to_inner_dir(".", project_path, self.option("excludes"))

        poetry = Factory().create_poetry(project_path)

        exporter = Exporter(poetry, self.io)
        exporter.with_hashes(False)
        exporter.with_urls(False)
        exporter.with_credentials(False)
        exporter.export("requirements.txt", project_path, "requirements.txt")

        self.line("installing deps...")

        for line in Sh("pip install -r #{requirements_path} -t #{target_path}")(
            requirements_path=str(project_path / "requirements.txt"), target_path=str(project_path)
        ):
            self.line(line)

        pkg_name = poetry.pyproject.data.get("tool").get("poetry").get("name")  # type: ignore

        self.line("creating egg...")
        with _temp_argv(["assembly", "bdist_egg"]), _temp_cwd(project_path):
            setup(
                name=pkg_name,
                version="0.0.1",
                description="Assembly",
                packages=find_packages(),
                package_dir={"": "."},
                install_requires=[Path("requirements.txt").read_text()],
                zip_safe=False,
            )

        egg_path = list((project_path / "dist").glob("*.egg"))
        dist_path = Path("dist")
        dist_path.mkdir(exist_ok=True, parents=True)
        for egg in egg_path:
            shutil.move(str(egg.absolute()), dist_path / egg.name)

        return 0


class Assembly(ApplicationPlugin):
    def activate(self, application):
        application.add(AssemblyCmd())
