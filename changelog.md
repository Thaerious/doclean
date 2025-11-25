# Changelog

All notable changes to **pyclean** will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/)
and the project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2025-11-25
### Added
- Initial MVP release of `pyclean`.
- Reads cleanup patterns from `[tool.pyclean]` in `pyproject.toml`.
- Supports globbing (`*`) and recursive globbing (`**/pattern`).
- Searches upward to locate the nearest `pyproject.toml`.
- Safe path validation:
  - Prevent deleting project root
  - Prevent deleting outside project directory
  - Reject symlinks
  - Skip missing paths
- `--dry` mode for previewing deletions.
- `--version` flag.
- Console script: `pyclean`.

---