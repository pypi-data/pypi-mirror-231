from pummel.classes import Status, ContentToTarget

OK_CONTENT = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
""".lstrip()


def test_ok(tmp_path):
    target = tmp_path.joinpath("parent/directory/file")

    assert ContentToTarget(OK_CONTENT, str(target)).execute() == (Status.SUCCESS, [])
    assert target.read_text() == OK_CONTENT


def test_ko_oserror():
    assert ContentToTarget("dummy text", "").execute() == (Status.FAILURE, ["[Errno 21] Is a directory: '.'"])
