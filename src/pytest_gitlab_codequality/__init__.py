from pytest import Config, Parser, PytestPluginManager

from pytest_gitlab_codequality.plugin import GitlabCodequalityReportPlugin
from pytest_gitlab_codequality.recorder import ViolationRecorder


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    parser.addoption(
        "--gitlab-codequality-report",
        default="pytest-warnings.json",
        required=False,
        help="Outputs warnings in GitLabs Code Quality Report file.",
    )


def pytest_configure(config: Config):
    report_path = config.getoption("gitlab_codequality_report")
    if report_path is None:
        return

    file = open(str(report_path), "w")
    recorder = ViolationRecorder(file)
    recorder.prepare()
    plugin = GitlabCodequalityReportPlugin(recorder, config.rootpath)

    _ = config.pluginmanager.register(plugin, "gitlab_codequality")
