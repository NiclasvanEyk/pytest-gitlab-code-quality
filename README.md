# GitLab Code Quality for Pytest

![current package version](https://img.shields.io/pypi/v/pytest-gitlab-code-quality)
![supported Python versions](https://img.shields.io/pypi/pyversions/pytest-gitlab-code-quality)
![github sponsors](https://img.shields.io/github/sponsors/NiclasvanEyk)
![license](https://img.shields.io/github/license/NiclasvanEyk/pytest-gitlab-code-quality)

Enables GitLab to collect and show warnings emitted during your test runs through their [code quality report].

| Terminal | GitLab |
|----------|--------|
| ![Pytest warnings in the terminal](https://github.com/NiclasvanEyk/pytest-gitlab-code-quality/blob/main/.github/images/terminal.png?raw=true) | ![Pytest warnings in the GitLab merge request widget](https://github.com/NiclasvanEyk/pytest-gitlab-code-quality/blob/main/.github/images/gitlab.png?raw=true) |

If you run GitLab Premium or Ultimate, you should even see the warnings [right next to the code](https://docs.gitlab.com/ee/ci/testing/code_quality.html#merge-request-changes-view) in the diff view of merge requests.
The [official documentation](https://docs.gitlab.com/ee/ci/testing/code_quality.html) contains more information and screenshots.

## Getting Started

Install the plugin using a package manager of your choice

```shell
pip install pytest-gitlab-code-quality
```

then specify the output location for the report using the `--gitlab-code-quality-report` option

```shell
pytest --gitlab-code-quality-report=pytest-warnings.json
```

In GitLab CI, this will look similar to this:

```yaml
# .gitlab-ci.yml
pytest:
  stage: test
  image: python
  script:
    - pip install -r requirements.txt # Or however you install your dependencies
    - python -m pytest --gitlab-code-quality-report=pytest-warnings.json

  # The three lines below are required in order for the warnings to show up!
  artifacts:
    reports:
      codequality: pytest-warnings.json
```

## Motivation

Some warnings are only surfaced during runtime, so static analyzers do not always catch them.
The screenshots at the top of this document contain the example of a questionably configured SQLAlchemy model.
Tests are a cheap way to surface such issues.

While you may run the tests locally and see these warnings there, you also might overlook them or don't know whether they were introduced by your changes or were already present before.
Either way, I think it makes sense to explicitly surface and track them during code review instead of burying them in the CI logs that nobody looks at when the tests pass.
And that is exactly why this plugin was created.
