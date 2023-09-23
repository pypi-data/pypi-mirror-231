import datetime
import io

import pytest

import pummel

OK_SCRIPT = """
---
- /bin/true
""".lstrip()

OK_OUTPUT_FIRST_LOG = """
no report found
""".lstrip()

OK_OUTPUT_RUN_DRY = """
fetching script 'script' from server http://localhost:8000 with levels ['lorem', 'ipsum']
pending: "/bin/true"
""".lstrip()

OK_OUTPUT_RUN_INTERACTIVE = """
fetching script 'script' from server http://localhost:8000 with levels ['lorem', 'ipsum']
pending: "/bin/true"

next: "/bin/true"
(e)xecute or (s)kip? skipped
""".lstrip()

OK_OUTPUT_RUN = """
fetching script 'script' from server http://localhost:8000 with levels ['lorem', 'ipsum']
pending: "/bin/true"

executing: "/bin/true"... success!
""".lstrip()

OK_OUTPUT_SECOND_LOG = """
e16c54885f5c659d190ab89b989f99e6 {} success {{"command": "/bin/true", "variant": ""}}
""".lstrip()  # .format() means json's {} have to be escaped as {{}}

OK_OUTPUT_SECOND_LOG_MD5 = """
{
  "entry": {
    "command": "/bin/true",
    "variant": ""
  },
  "status": "success",
  "output": []
}
""".lstrip()


def test_ok(server, tmp_path, capsys, monkeypatch):
    server.data = {"script": OK_SCRIPT}

    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} log".split())
    assert capsys.readouterr().out == OK_OUTPUT_FIRST_LOG

    with pytest.raises(FileNotFoundError):
        pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} log e16c54885f5c659d190ab89b989f99e6".split())

    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} run --dry".split())
    assert capsys.readouterr().out == OK_OUTPUT_RUN_DRY

    monkeypatch.setattr("sys.stdin", io.StringIO("s\n"))
    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} run --interactive".split())
    assert capsys.readouterr().out == OK_OUTPUT_RUN_INTERACTIVE

    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} run".split())
    assert capsys.readouterr().out == OK_OUTPUT_RUN

    mtime = datetime.datetime.fromtimestamp(tmp_path.joinpath("e16c54885f5c659d190ab89b989f99e6").stat().st_mtime).strftime("%c")

    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} log".split())
    assert capsys.readouterr().out == OK_OUTPUT_SECOND_LOG.format(mtime)

    pummel.main(f"-u http://localhost:8000 -l lorem -l ipsum -r {tmp_path} log e16c54885f5c659d190ab89b989f99e6".split())
    assert capsys.readouterr().out == OK_OUTPUT_SECOND_LOG_MD5
