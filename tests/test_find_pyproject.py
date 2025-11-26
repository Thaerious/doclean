
from pyclean.cli import find_pyproject
from pathlib import Path
import pytest
import os

def build_pyproject(root, monkeypatch):
    project_root = root / "my_project"
    pyproject_path = project_root / "pyproject.toml"    
    pyproject_path.parent.mkdir()
    src_path = project_root / "src"
    src_path.mkdir()
    deep_path = src_path / "deep" / "deeper" / "deepest"
    deep_path.mkdir(parents=True)
    outside_path = root / "outside_project"
    outside_path.mkdir()

    link = root / "link_to_project"
    link.symlink_to(project_root, target_is_directory=True)

    pyproject_path.write_text('''
        [tool.pyclean]
        paths = [
            "build",
            "dist",
            "**/__pycache__",
            ".pytest_cache"
        ]
    ''')

    monkeypatch.chdir(project_root)
    return project_root


def test_no_pyproject_exception(tmp_path):
    """Test that get_pyproject raises exception when no pyproject.toml file exists."""
    
    with pytest.raises(Exception):    
        find_pyproject(tmp_path)


def test_pyproject_exists(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    pyproject = find_pyproject()


def test_pyproject_exists_in_parent(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    monkeypatch.chdir("src")
    pyproject = find_pyproject()


def test_pyproject_exists_in_parent_pass_in_path(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    monkeypatch.chdir("..")
    pyproject = find_pyproject(Path("./my_project/src"))


def test_start_in_linked_dir(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    pyproject = find_pyproject(Path("../link_to_project"))


def test_pyproject_in_grandparent(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    monkeypatch.chdir("src/deep/deeper/deepest")
    pyproject = find_pyproject()

    print("\n")
    print("cwd:", os.getcwd())   
    print("pyproject:", pyproject)        


def test_pyproject_in_wrong_dir(tmp_path, monkeypatch):
    build_pyproject(tmp_path, monkeypatch)
    monkeypatch.chdir("../outside_project")
    
    with pytest.raises(Exception): 
        pyproject = find_pyproject()
