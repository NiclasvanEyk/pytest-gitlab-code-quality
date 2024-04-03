from io import TextIOWrapper
from json import dumps
from dataclasses import asdict

from pytest_gitlab_code_quality.report import Violation


class ViolationRecorder:
    """
    Records violations by streaming them to a file.
    """

    def __init__(self, file: TextIOWrapper) -> None:
        self._file = file
        self._first = True

    def prepare(self) -> None:
        """
        Writes an initial opening array bracket to the file.
        """
        _ = self._file.write("[\n")

    def record(self, violation: Violation) -> None:
        """
        Writes a line containing the violation to the file.
        """
        serialized = dumps(asdict(violation))
        if self._first:
            self._first = False
        else:
            serialized = f",\n{serialized}"

        _ = self._file.write(serialized)

    def close(self) -> None:
        """
        Closes the violation array and the file.
        """
        _ = self._file.write("\n]\n")
        self._file.close()
