import threading
import time

from pummel.classes import Command, Status


def test_ok(capsys):
    assert Command("echo one && echo two").execute() == (Status.SUCCESS, ["one", "two"])
    assert capsys.readouterr().out == ".."


KO_OUTPUT = """
. error, will try again in 0.1 seconds (2 attempts remaining)
. error, will try again in 0.1 seconds (1 attempts remaining)
.""".lstrip()

KO_OUTPUT_ARRAY = ["ko",
                   "error, will try again in 0.1 seconds (2 attempts remaining)",
                   "ko",
                   "error, will try again in 0.1 seconds (1 attempts remaining)",
                   "ko"]


def test_ko(capsys):
    assert Command("echo ko && false").execute(attempts=3, pause=0.1) == (Status.FAILURE, KO_OUTPUT_ARRAY)
    assert capsys.readouterr().out == KO_OUTPUT


def test_ko_then_ok(tmp_path, capsys):
    assert Command(f"test -f {tmp_path}/file || ! touch {tmp_path}/file").execute(pause=0.1) == (Status.SUCCESS, ["error, will try again in 0.1 seconds (3 attempts remaining)"])
    assert capsys.readouterr().out.strip() == "error, will try again in 0.1 seconds (3 attempts remaining)"


def test_wrong_attempts(capsys):
    assert Command("echo ko && false").execute(attempts=0) == (Status.FAILURE, ["ko"])
    assert capsys.readouterr().out.strip() == "."


def test_progress_bar(capsys):
    def execute():
        Command("echo one && sleep 1 && echo two").execute()

    thread = threading.Thread(target=execute)
    thread.start()
    time.sleep(0.5)
    assert capsys.readouterr().out == "."
    thread.join()
    assert capsys.readouterr().out == "."
