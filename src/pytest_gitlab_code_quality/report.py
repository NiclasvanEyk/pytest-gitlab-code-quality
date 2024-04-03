from dataclasses import dataclass


@dataclass
class Lines:
    begin: int
    """The line on which the code quality violation occurred."""


@dataclass
class Location:
    path: str
    """The relative path to the file containing the code quality violation."""

    lines: Lines


@dataclass
class Violation:
    """
    A code quality violation / warning emitted during the test run.

    See https://docs.gitlab.com/ee/ci/testing/code_quality.html#implement-a-custom-tool
    """

    description: str
    """A description of the code quality violation."""

    check_name: str
    """A unique name representing the static analysis check that emitted this issue."""

    fingerprint: str
    """A unique fingerprint to identify the code quality violation. For example, an MD5 hash."""

    severity: str
    """A severity string (can be info, minor, major, critical, or blocker)."""

    location: Location
