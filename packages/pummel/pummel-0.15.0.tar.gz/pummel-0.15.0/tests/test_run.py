import io
import pathlib

import pytest

import pummel


def test_ko_script_not_found(server, tmp_path):
    server.data = {}

    with pytest.raises(LookupError) as excinfo:
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert str(excinfo.value) == "key 'script' not found"


KO_INCLUDE_NOT_FOUND = """
---
- include: huhu
""".lstrip()


def test_ko_include_not_found(server, tmp_path):
    server.data = {"script": KO_INCLUDE_NOT_FOUND}

    with pytest.raises(LookupError) as excinfo:
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert str(excinfo.value) == "key 'huhu' not found"


def test_ko_not_a_script(server, tmp_path):
    server.data = {"script": "not a script"}

    with pytest.raises(ValueError) as excinfo:
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert str(excinfo.value) == "key 'script' is not a proper yaml or json list"


KO_MALFORMED_TASK_DICT = """
---
- yin: yang
""".lstrip()


def test_ko_malformed_task_dict(server, tmp_path):
    server.data = {"script": KO_MALFORMED_TASK_DICT}

    with pytest.raises(ValueError) as excinfo:
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert str(excinfo.value) == 'malformed task, unknown keys: {"yin": "yang"}'


KO_MALFORMED_TASK_LIST = """
---
- - lorem
  - ipsum
""".lstrip()


def test_ko_malformed_task_list(server, tmp_path):
    server.data = {"script": KO_MALFORMED_TASK_LIST}

    with pytest.raises(ValueError) as excinfo:
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert str(excinfo.value) == 'malformed task, must be a string or a dictionary: ["lorem", "ipsum"]'


OK_SCRIPT = """
---
- echo ok
- echo ok
- include: subscript
- command: echo ok
  variant: variant
""".lstrip()

OK_SUBSCRIPT = """
---
- key: config
  target: {0}/config
- content: |
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  target: {0}/content
""".lstrip()

OK_CONTENT = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
""".lstrip()

OK_OUTPUT_1 = """
fetching script 'script' from server http://localhost:8000 with levels []
pending: "echo ok"
ignored: "echo ok"
pending: copy contents of kivalu key "config" to "{0}/config"
pending: copy "Lorem ipsum dolor sit amet, consectetur adipisc..." to "{0}/content"
pending: "echo ok" (variant)

executing: "echo ok".... success!
executing: copy contents of kivalu key "config" to "{0}/config"... success!
executing: copy "Lorem ipsum dolor sit amet, consectetur adipisc..." to "{0}/content"... success!
executing: "echo ok" (variant).... success!
""".lstrip()

OK_REPORT = """
{
  "entry": {
    "command": "echo ok",
    "variant": ""
  },
  "status": "success",
  "output": [
    "ok"
  ]
}
""".strip()

OK_OUTPUT_2 = """
fetching script 'script' from server http://localhost:8000 with levels []
success: "echo ok"
ignored: "echo ok"
success: copy contents of kivalu key "config" to "{0}/config"
success: copy "Lorem ipsum dolor sit amet, consectetur adipisc..." to "{0}/content"
success: "echo ok" (variant)

no pending or failed task to run
""".lstrip()


def test_ok(server, tmp_path, capsys):
    server.data = {
        "script": OK_SCRIPT,
        "subscript": OK_SUBSCRIPT.format(tmp_path),
        "config": "key=value"
    }

    pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert capsys.readouterr().out == OK_OUTPUT_1.format(tmp_path)
    assert tmp_path.joinpath("config").read_text() == "key=value"
    assert tmp_path.joinpath("content").read_text() == OK_CONTENT
    assert tmp_path.joinpath("b44c91c1309e327fd1fcf5b8c79e1b85").read_text() == OK_REPORT

    pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script")

    assert capsys.readouterr().out == OK_OUTPUT_2.format(tmp_path)


KO_SCRIPT = """
---
- echo 'first line' && echo 'second line' && /bin/false
- echo ok
""".lstrip()

KO_OUTPUT_1 = """
fetching script 'script' from server http://localhost:8000 with levels []
pending: "echo 'first line' && echo 'second line' && /bin/false"
pending: "echo ok"

executing: "echo 'first line' && echo 'second line' && /bin/false"..... error, will try again in 0.1 seconds (1 attempts remaining)
.. failed!
output: [
  "first line",
  "second line",
  "error, will try again in 0.1 seconds (1 attempts remaining)",
  "first line",
  "second line"
]
""".lstrip()

KO_OUTPUT_2 = """
fetching script 'script' from server http://localhost:8000 with levels []
failure: "echo 'first line' && echo 'second line' && /bin/false"
pending: "echo ok"

executing: "echo 'first line' && echo 'second line' && /bin/false"..... error, will try again in 0.1 seconds (1 attempts remaining)
.. failed!
output: [
  "first line",
  "second line",
  "error, will try again in 0.1 seconds (1 attempts remaining)",
  "first line",
  "second line"
]
""".lstrip()


def test_ko(server, tmp_path, capsys):
    server.data = {"script": KO_SCRIPT}

    with pytest.raises(ChildProcessError):
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script", attempts=2, pause=0.1)

    assert capsys.readouterr().out == KO_OUTPUT_1

    with pytest.raises(ChildProcessError):
        pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script", attempts=2, pause=0.1)

    assert capsys.readouterr().out == KO_OUTPUT_2


INTERACTIVE_SCRIPT = """
---
- echo one
- echo two
- /bin/false
""".lstrip()

INTERACTIVE_OUTPUT_1 = """
fetching script 'script' from server http://localhost:8000 with levels []
pending: "echo one"
pending: "echo two"
pending: "/bin/false"

next: "echo one"
(e)xecute or (s)kip? .... success!
next: "echo two"
(e)xecute or (s)kip? skipped
next: "/bin/false"
(e)xecute or (s)kip? skipped
""".lstrip()

INTERACTIVE_OUTPUT_2 = """
fetching script 'script' from server http://localhost:8000 with levels []
success: "echo one"
pending: "echo two"
pending: "/bin/false"

next: "echo two"
(e)xecute or (s)kip? .... success!
next: "/bin/false"
(e)xecute or (s)kip? ... failed!
output: []
""".lstrip()

INTERACTIVE_OUTPUT_3 = """
fetching script 'script' from server http://localhost:8000 with levels []
success: "echo one"
success: "echo two"
failure: "/bin/false"

next: "/bin/false"
(e)xecute or (s)kip? skipped
""".lstrip()


def test_interactive(server, monkeypatch, tmp_path, capsys):
    server.data = {"script": INTERACTIVE_SCRIPT}

    monkeypatch.setattr("sys.stdin", io.StringIO("e\ns\ns\n"))
    pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script", interactive=True)
    assert capsys.readouterr().out == INTERACTIVE_OUTPUT_1

    monkeypatch.setattr("sys.stdin", io.StringIO("e\ne\n"))
    pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script", interactive=True)
    assert capsys.readouterr().out == INTERACTIVE_OUTPUT_2

    monkeypatch.setattr("sys.stdin", io.StringIO("s\n"))
    pummel.run(url="http://localhost:8000", configuration_file=pathlib.Path(""), reports_path=tmp_path, key="script", interactive=True)
    assert capsys.readouterr().out == INTERACTIVE_OUTPUT_3
