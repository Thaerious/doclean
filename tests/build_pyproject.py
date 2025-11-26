
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