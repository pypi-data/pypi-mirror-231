from pummel.classes import Status, KeyToTarget


def test_ok(server, client, tmp_path):
    server.data = {"dummy.conf": "yin: yang\n"}
    target = tmp_path.joinpath("parent/directory/file")

    assert KeyToTarget("dummy.conf", str(target)).execute(client) == (Status.SUCCESS, [])
    assert target.read_text() == "yin: yang\n"


def test_ko_key_not_found(server, client, tmp_path):
    server.data = {}
    target = tmp_path.joinpath("file")

    assert KeyToTarget("dummy.conf", str(target)).execute(client) == (Status.FAILURE, ["key 'dummy.conf' not found on server http://localhost:8000"])
    assert not target.exists()


def test_ko_oserror(server, client):
    server.data = {"dummy.conf": "yin: yang\n"}

    assert KeyToTarget("dummy.conf", "").execute(client) == (Status.FAILURE, ["[Errno 21] Is a directory: '.'"])
