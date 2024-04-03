from json import loads

from pytest import ExitCode, Pytester


def test_throws_if_called_without_file_path(pytester: Pytester) -> None:
    result = pytester.runpytest("--gitlab-code-quality-report")
    assert "argument --gitlab-code-quality-report: expected one argument" in str(
        result.stderr
    )


def test_works_for_empty_tests(pytester: Pytester) -> None:
    result = pytester.runpytest("--gitlab-code-quality-report", "pytest-warnings.json")
    assert result.ret == ExitCode.NO_TESTS_COLLECTED

    report_file = pytester.path / "pytest-warnings.json"
    assert report_file.exists()
    assert loads(report_file.read_text()) == []


def test_works_for_manually_emitted_warning(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import warnings

        def test_no_warning():
            assert 1 == 1

        def test_has_warning():
            warnings.warn("beware!")
    """)
    result = pytester.runpytest("--gitlab-code-quality-report", "pytest-warnings.json")
    assert result.ret == 0

    report_file = pytester.path / "pytest-warnings.json"
    assert report_file.exists()

    warnings = loads(report_file.read_text())
    assert len(warnings) == 1
    assert warnings[0]["description"] == "beware!"
    assert warnings[0]["check_name"] == "PytestUserWarning"
    assert (
        warnings[0]["location"]["path"] == "test_works_for_manually_emitted_warning.py"
    )
    assert warnings[0]["location"]["lines"]["begin"] == 7
