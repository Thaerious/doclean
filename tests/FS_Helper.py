from pathlib import Path
import pytest

class Helper:
    def __init__(self, root: Path):
        self.root = root

    def make(self, relative_path: str, contents: str = ""):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents)
        return path

    def link_dir(self, link_path: str, target_path: str):
        link = self.root / link_path
        target = self.root / target_path
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target, target_is_directory=target.is_dir())
        return link

    def link_file(self, link_path: str, target_path: str):
        link = self.root / link_path
        target = self.root / target_path
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target)
        return link

@pytest.fixture
def helper(tmp_path):
    return Helper(tmp_path)