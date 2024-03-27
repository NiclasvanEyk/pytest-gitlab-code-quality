from pytest import Config
from pathlib import Path
from warnings import WarningMessage

from pytest_gitlab_codequality.report import Lines, Location, Violation
from pytest_gitlab_codequality.recorder import ViolationRecorder


class GitlabCodequalityReportPlugin:
    """
    Orchestrates the test warnings to be recorded.
    """

    def __init__(  # type: ignore[ignoreMissingSuperCall]
        self,
        recorder: ViolationRecorder,
        root: Path,
    ) -> None:
        self._recorder = recorder
        self._root = root

    def pytest_warning_recorded(
        self,
        warning_message: WarningMessage,
        when: str,
        nodeid: str,
        location: tuple[str, int, str] | None,
    ):
        path = warning_message.filename.replace(str(self._root), "")
        if path.startswith("/"):
            path = path.removeprefix("/")

        # TODO: Utilize location
        message = warning_message.message
        print(location)
        print(warning_message)

        violation = Violation(
            description=str(message),
            check_name=f"Pytest{warning_message.category.__name__}",
            fingerprint=str(hash(f"{nodeid}::{warning_message.lineno}::{message}")),
            severity="minor",
            location=Location(
                path=path,
                lines=Lines(
                    begin=warning_message.lineno,
                ),
            ),
        )

        self._recorder.record(violation)

    def pytest_unconfigure(self, config: Config):
        self._recorder.close()
