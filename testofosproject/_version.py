def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import testofosproject

    testofosproject_path = Path(testofosproject.__file__).parent
    return versioningit.get_version(project_dir=testofosproject_path.parent)


__version__ = _get_version()
