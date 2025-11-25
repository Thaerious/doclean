. PyPI upload guide (drop into e.g. PUBLISHING.md)
# Publishing pyclean to PyPI

This guide assumes:

- `pyproject.toml` is configured for setuptools
- You have a PyPI account at https://pypi.org
- You have `build` and `twine` installed

---

## 1. Install tools

```bash
python -m pip install --upgrade pip
python -m pip install build twine

2. Build the distributions

From the project root (where pyproject.toml lives):

python -m build


This creates:

dist/pyclean-<version>.tar.gz (sdist)

dist/pyclean-<version>-py3-none-any.whl (wheel)

3. Test upload to TestPyPI (recommended)

Create an account at https://test.pypi.org

Create an API token there

Upload to TestPyPI:

python -m twine upload \
  --repository testpypi \
  dist/*


You’ll be prompted for:

username: __token__

password: <your TestPyPI token>

Then install from TestPyPI in a fresh virtualenv:

python -m venv .venv-test
source .venv-test/bin/activate  # Windows: .venv-test\Scripts\activate

python -m pip install --index-url https://test.pypi.org/simple/ \
                      --extra-index-url https://pypi.org/simple \
                      pyclean

pyclean --version


If that works, you’re ready for real PyPI.

4. Upload to real PyPI

Create an account at https://pypi.org

Create an API token (Project-scoped or Account-scoped)

Upload:

python -m twine upload dist/*


Again:

username: __token__

password: <your PyPI token>

After that, users can install with:

pip install pyclean

5. Optional: .pypirc configuration

To avoid retyping repository URLs, create ~/.pypirc:

[distutils]
index-servers =
    pypi
    testpypi

[pypi]
  repository = https://upload.pypi.org/legacy/
  username = __token__

[testpypi]
  repository = https://test.pypi.org/legacy/
  username = __token__


Then twine upload -r testpypi dist/* or -r pypi will use these settings.

6. Release checklist

Before each release:

Update version in pyproject.toml

Update CHANGELOG.md

Commit and tag (optional):

git commit -am "Release x.y.z"
git tag -a vx.y.z -m "Release x.y.z"
git push --tags


Rebuild and upload:

rm -rf dist/
python -m build
python -m twine upload dist/*


If you want, next step could be a tiny `tests/` package with a couple of smoke tests CI can run.
::contentReference[oaicite:0]{index=0}