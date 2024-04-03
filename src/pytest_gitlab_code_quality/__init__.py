from pathlib import Path

from pytest import Config, Parser, PytestPluginManager

from pytest_gitlab_code_quality.plugin import GitlabCodeQualityReportPlugin
from pytest_gitlab_code_quality.recorder import ViolationRecorder


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager) -> None:
    parser.addoption(
        "--gitlab-code-quality-report",
        default="pytest-warnings.json",
        required=False,
        help="Outputs warnings in GitLabs Code Quality Report file.",
    )


def pytest_configure(config: Config) -> None:
    report_path = config.getoption("gitlab_code_quality_report")
    if report_path is None:
        return

    file = Path(str(report_path)).open("w")  # noqa: SIM115
    recorder = ViolationRecorder(file)
    recorder.prepare()
    plugin = GitlabCodeQualityReportPlugin(recorder, config.rootpath)

    _ = config.pluginmanager.register(plugin, "gitlab_code_quality")
