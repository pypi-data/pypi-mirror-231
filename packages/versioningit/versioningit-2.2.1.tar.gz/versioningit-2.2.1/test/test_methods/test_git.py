from __future__ import annotations
from datetime import datetime, timezone
import logging
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any
import pytest
from versioningit.core import VCSDescription
from versioningit.errors import ConfigError, NoTagError, NotVCSError
from versioningit.git import GitRepo, describe_git, describe_git_archive

needs_git = pytest.mark.skipif(shutil.which("git") is None, reason="Git not installed")

BUILD_DATE = datetime(2038, 1, 19, 3, 14, 7, tzinfo=timezone.utc)

DATA_DIR = Path(__file__).parent.with_name("data")


@needs_git
@pytest.mark.parametrize(
    "repo,params,description",
    [
        (
            "exact",
            {},
            VCSDescription(
                tag="v0.1.0",
                state="exact",
                branch="master",
                fields={
                    "distance": 0,
                    "rev": "002a8cf",
                    "revision": "002a8cf62e16f1b22c5869479a5ba7cac7c19fbc",
                    "author_date": datetime(2021, 7, 4, 4, 8, 20, tzinfo=timezone.utc),
                    "committer_date": datetime(
                        2021, 7, 4, 4, 9, 33, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "distance",
            {},
            VCSDescription(
                tag="v0.1.0",
                state="distance",
                branch="master",
                fields={
                    "distance": 1,
                    "rev": "d735ad7",
                    "revision": "d735ad70269a40b26c56eea540a9e4a50c48b36a",
                    "author_date": datetime(2021, 7, 4, 4, 11, 57, tzinfo=timezone.utc),
                    "committer_date": datetime(
                        2021, 7, 4, 4, 11, 57, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "distance-dirty",
            {},
            VCSDescription(
                tag="v0.1.0",
                state="distance-dirty",
                branch="master",
                fields={
                    "distance": 1,
                    "rev": "d735ad7",
                    "revision": "d735ad70269a40b26c56eea540a9e4a50c48b36a",
                    "author_date": datetime(2021, 7, 4, 4, 11, 57, tzinfo=timezone.utc),
                    "committer_date": datetime(
                        2021, 7, 4, 4, 11, 57, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "default-tag",
            {"default-tag": "v0.0.0"},
            VCSDescription(
                tag="v0.0.0",
                state="distance",
                branch="master",
                fields={
                    "distance": 2,
                    "rev": "2b9cc67",
                    "revision": "2b9cc67944ff8e70163441a55be4596147f82df7",
                    "author_date": datetime(
                        2021, 7, 5, 23, 32, 45, tzinfo=timezone.utc
                    ),
                    "committer_date": datetime(
                        2021, 7, 5, 23, 32, 45, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "match",
            {"match": ["v*"]},
            VCSDescription(
                tag="v0.1.0",
                state="distance",
                branch="master",
                fields={
                    "distance": 2,
                    "rev": "56fd4b6",
                    "revision": "56fd4b64151218b0339fcf0f5ffca4f5cbfd64b3",
                    "author_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "committer_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "match",
            {},
            VCSDescription(
                tag="0.2.0",
                state="exact",
                branch="master",
                fields={
                    "distance": 0,
                    "rev": "56fd4b6",
                    "revision": "56fd4b64151218b0339fcf0f5ffca4f5cbfd64b3",
                    "author_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "committer_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        pytest.param(
            "exclude",
            {"exclude": ["v*"]},
            VCSDescription(
                tag="0.1.0",
                state="distance",
                branch="master",
                fields={
                    "distance": 2,
                    "rev": "f0e0d90",
                    "revision": "f0e0d900fdd146d6c1c5ec202eebe37cd8f3d000",
                    "author_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "committer_date": datetime(
                        2021, 7, 6, 16, 29, 54, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
            marks=pytest.mark.describe_exclude,
        ),
        (
            "exclude",
            {},
            VCSDescription(
                tag="v0.2.0",
                state="exact",
                branch="master",
                fields={
                    "distance": 0,
                    "rev": "f0e0d90",
                    "revision": "f0e0d900fdd146d6c1c5ec202eebe37cd8f3d000",
                    "author_date": datetime(
                        2021, 7, 6, 16, 27, 48, tzinfo=timezone.utc
                    ),
                    "committer_date": datetime(
                        2021, 7, 6, 16, 29, 54, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
        (
            "detached-exact",
            {},
            VCSDescription(
                tag="v0.1.0",
                state="exact",
                branch=None,
                fields={
                    "distance": 0,
                    "rev": "002a8cf",
                    "revision": "002a8cf62e16f1b22c5869479a5ba7cac7c19fbc",
                    "author_date": datetime(2021, 7, 4, 4, 8, 20, tzinfo=timezone.utc),
                    "committer_date": datetime(
                        2021, 7, 4, 4, 9, 33, tzinfo=timezone.utc
                    ),
                    "build_date": BUILD_DATE,
                    "vcs": "g",
                    "vcs_name": "git",
                },
            ),
        ),
    ],
)
def test_describe_git(
    repo: str, params: dict[str, Any], description: VCSDescription, tmp_path: Path
) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / f"{repo}.zip"), str(tmp_path)
    )
    desc = describe_git(project_dir=tmp_path, params=params)
    assert desc == description
    for date in ["author_date", "committer_date", "build_date"]:
        assert desc.fields[date].tzinfo is timezone.utc


@needs_git
def test_describe_git_no_tag(tmp_path: Path) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / "default-tag.zip"), str(tmp_path)
    )
    with pytest.raises(NoTagError) as excinfo:
        describe_git(project_dir=tmp_path, params={})
    assert str(excinfo.value) == "`git describe` could not find a tag"


@needs_git
def test_describe_git_no_repo(tmp_path: Path) -> None:
    with pytest.raises(NotVCSError) as excinfo:
        describe_git(project_dir=tmp_path, params={})
    assert str(excinfo.value) == f"{tmp_path} is not in a Git repository"


@needs_git
@pytest.mark.parametrize("params", [{}, {"default-tag": "0.0.0"}])
def test_describe_git_no_commits(tmp_path: Path, params: dict[str, Any]) -> None:
    subprocess.run(["git", "init"], check=True, cwd=str(tmp_path))
    with pytest.raises(NotVCSError) as excinfo:
        describe_git(project_dir=tmp_path, params=params)
    assert str(excinfo.value) == f"{tmp_path} is not tracked by Git"


@needs_git
def test_describe_git_added_no_commits(tmp_path: Path) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / "added-no-commits-default-tag.zip"),
        str(tmp_path),
    )
    with pytest.raises(NoTagError, match=r"^`git describe` command failed: "):
        describe_git(project_dir=tmp_path, params={})


@needs_git
def test_describe_git_no_clamp_dates(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "1234567890")
    shutil.unpack_archive(str(DATA_DIR / "repos" / "git" / "exact.zip"), str(tmp_path))
    assert describe_git(project_dir=tmp_path, params={}) == VCSDescription(
        tag="v0.1.0",
        state="exact",
        branch="master",
        fields={
            "distance": 0,
            "rev": "002a8cf",
            "revision": "002a8cf62e16f1b22c5869479a5ba7cac7c19fbc",
            "author_date": datetime(2021, 7, 4, 4, 8, 20, tzinfo=timezone.utc),
            "committer_date": datetime(2021, 7, 4, 4, 9, 33, tzinfo=timezone.utc),
            "build_date": datetime(2009, 2, 13, 23, 31, 30, tzinfo=timezone.utc),
            "vcs": "g",
            "vcs_name": "git",
        },
    )


def test_describe_git_archive_no_describe_subst(tmp_path: Path) -> None:
    with pytest.raises(ConfigError) as excinfo:
        describe_git_archive(project_dir=tmp_path, params={})
    assert (
        str(excinfo.value)
        == "tool.versioningit.vcs.describe-subst must be set to a string"
    )


def test_describe_git_archive_empty_describe_subst(tmp_path: Path) -> None:
    with pytest.raises(NoTagError) as excinfo:
        describe_git_archive(project_dir=tmp_path, params={"describe-subst": ""})
    assert str(excinfo.value) == (
        "tool.versioningit.vcs.describe-subst is empty in Git archive"
    )


@pytest.mark.parametrize("init", [False, pytest.param(True, marks=needs_git)])
def test_describe_git_archive_unexpanded_describe_subst(
    init: bool, tmp_path: Path
) -> None:
    if init:
        subprocess.run(["git", "init"], check=True, cwd=str(tmp_path))
    with pytest.raises(NoTagError) as excinfo:
        describe_git_archive(
            project_dir=tmp_path, params={"describe-subst": "$Format:%(describe)$"}
        )
    assert str(excinfo.value) == (
        "tool.versioningit.vcs.describe-subst not expanded in Git archive"
    )


@pytest.mark.parametrize("init", [False, pytest.param(True, marks=needs_git)])
@pytest.mark.parametrize("describe_subst", ["%(describe)", "%(describe:unknown=value)"])
def test_describe_git_archive_bad_expanded_describe_subst(
    init: bool, describe_subst: str, tmp_path: Path
) -> None:
    if init:
        subprocess.run(["git", "init"], check=True, cwd=str(tmp_path))
    with pytest.raises(NoTagError) as excinfo:
        describe_git_archive(
            project_dir=tmp_path, params={"describe-subst": describe_subst}
        )
    assert str(excinfo.value) == (
        "tool.versioningit.vcs.describe-subst format was invalid, expanded to"
        f" {describe_subst!r}"
    )


def test_describe_git_archive_repo_unset_describe_subst(tmp_path: Path) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / "exact-annotated.zip"), str(tmp_path)
    )
    with pytest.raises(ConfigError) as excinfo:
        describe_git_archive(project_dir=tmp_path, params={})
    assert (
        str(excinfo.value)
        == "tool.versioningit.vcs.describe-subst must be set to a string"
    )


@needs_git
def test_describe_git_archive_repo_bad_describe_subst(tmp_path: Path) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / "exact-annotated.zip"), str(tmp_path)
    )
    with pytest.raises(ConfigError) as excinfo:
        describe_git_archive(
            project_dir=tmp_path, params={"describe-subst": "%(describe)"}
        )
    assert str(excinfo.value) == (
        "Invalid tool.versioningit.vcs.describe-subst value: Expected string in"
        " format '$Format:%(describe[:options])$', got '%(describe)'"
    )


@needs_git
def test_describe_git_archive_added_no_commits_default_tag(
    caplog: pytest.LogCaptureFixture, tmp_path: Path
) -> None:
    shutil.unpack_archive(
        str(DATA_DIR / "repos" / "git" / "added-no-commits-default-tag.zip"),
        str(tmp_path),
    )
    assert describe_git_archive(
        project_dir=tmp_path,
        params={"default-tag": "0.0.0", "describe-subst": "$Format:%(describe)$"},
    ) == VCSDescription(
        tag="0.0.0",
        state="dirty",
        branch="master",
        fields={
            "distance": 0,
            "rev": "0000000",
            "build_date": BUILD_DATE,
            "vcs": "g",
            "vcs_name": "git",
        },
    )
    assert any(
        logger == "versioningit"
        and level == logging.ERROR
        and re.match("^`git describe` command failed: ", msg)
        for logger, level, msg in caplog.record_tuples
    )
    assert (
        "versioningit",
        logging.INFO,
        "Falling back to default tag '0.0.0'",
    ) in caplog.record_tuples


@needs_git
def test_describe_git_archive_lightweight_only(tmp_path: Path) -> None:
    shutil.unpack_archive(str(DATA_DIR / "repos" / "git" / "exact.zip"), str(tmp_path))
    with pytest.raises(NoTagError) as excinfo:
        describe_git_archive(
            project_dir=tmp_path,
            params={"describe-subst": "$Format:%(describe)$"},
        )
    assert str(excinfo.value) == "`git describe` could not find a tag"


@needs_git
def test_describe_git_archive_lightweight_only_default_tag(
    caplog: pytest.LogCaptureFixture, tmp_path: Path
) -> None:
    shutil.unpack_archive(str(DATA_DIR / "repos" / "git" / "exact.zip"), str(tmp_path))
    assert describe_git_archive(
        project_dir=tmp_path,
        params={"default-tag": "0.0.0", "describe-subst": "$Format:%(describe)$"},
    ) == VCSDescription(
        tag="0.0.0",
        state="distance",
        branch="master",
        fields={
            "distance": 1,
            "rev": "002a8cf",
            "build_date": BUILD_DATE,
            "vcs": "g",
            "vcs_name": "git",
        },
    )
    assert (
        "versioningit",
        logging.INFO,
        "`git describe` returned a hash instead of a tag; falling back to"
        " default tag '0.0.0'",
    ) in caplog.record_tuples


@needs_git
def test_ensure_is_repo_not_tracked(tmp_path: Path) -> None:
    shutil.unpack_archive(str(DATA_DIR / "repos" / "git" / "exact.zip"), str(tmp_path))
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file.txt").touch()
    with pytest.raises(NotVCSError) as excinfo:
        GitRepo(tmp_path / "subdir").ensure_is_repo()
    assert str(excinfo.value) == f"{tmp_path / 'subdir'} is not tracked by Git"


@needs_git
def test_ensure_is_repo_dot_git_dir(tmp_path: Path) -> None:
    subprocess.run(["git", "init"], check=True, cwd=str(tmp_path))
    with pytest.raises(NotVCSError) as excinfo:
        GitRepo(tmp_path / ".git").ensure_is_repo()
    assert str(excinfo.value) == f"{tmp_path / '.git'} is not in a Git working tree"


@pytest.mark.skipif(shutil.which("git") is not None, reason="Git must not be installed")
def test_ensure_is_repo_git_not_installed(tmp_path: Path) -> None:
    with pytest.raises(NotVCSError) as excinfo:
        GitRepo(tmp_path).ensure_is_repo()
    assert (
        str(excinfo.value) == "Git not installed; assuming this isn't a Git repository"
    )
