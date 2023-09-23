import enum
import hashlib
import json
import subprocess
import time
from dataclasses import dataclass, asdict, field
from functools import cached_property
from pathlib import Path
from typing import Tuple, List

import kivalu

from .constants import ENCODING, ATTEMPTS_DEFAULT, PAUSE_DEFAULT, VARIANT_DEFAULT


class Status(str, enum.Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"
    IGNORED = "ignored"


@dataclass
class _Entry:  # abstract
    @cached_property
    def md5(self) -> str:
        return hashlib.md5(json.dumps(asdict(self)).encode(ENCODING)).hexdigest()

    def execute(self, **_) -> Tuple[Status, List[str]]:
        raise NotImplementedError()


@dataclass
class Command(_Entry):
    command: str
    variant: str = VARIANT_DEFAULT

    def execute(self, attempts: int = ATTEMPTS_DEFAULT, pause: float = PAUSE_DEFAULT, **_) -> Tuple[Status, List[str]]:
        output = []
        while True:
            sp = subprocess.Popen(["/bin/bash", "-l", "-c", self.command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding=ENCODING)
            attempts -= 1

            for line in sp.stdout:
                print(".", end="")  # progress bar: each stdout line prints a dot
                output.append(line.rstrip())

            if sp.wait() == 0:  # wait() returns the exit code
                return Status.SUCCESS, output
            elif attempts > 0:
                error = f"error, will try again in {pause} seconds ({attempts} attempts remaining)"
                print(" " + error)
                output.append(error)
                time.sleep(pause)
            else:
                return Status.FAILURE, output

    def __str__(self):
        return '"' + self.command + '"' + (" (" + self.variant + ")" if self.variant else "")


@dataclass
class KeyToTarget(_Entry):
    key: str
    target: str

    def execute(self, client: kivalu.Client, **_) -> Tuple[Status, List[str]]:
        if not (value := client.get(self.key, strip=False)):
            return Status.FAILURE, [f"key '{self.key}' not found on server {client.url}"]

        try:
            target_path = Path(self.target)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(value, encoding=ENCODING)
            return Status.SUCCESS, []
        except OSError as error:
            return Status.FAILURE, str(error).splitlines()

    def __str__(self):
        return 'copy contents of kivalu key "' + self.key + '" to "' + self.target + '"'


@dataclass
class ContentToTarget(_Entry):
    content: str
    target: str

    def execute(self, **_) -> Tuple[Status, List[str]]:
        try:
            target_path = Path(self.target)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(self.content, encoding=ENCODING)
            return Status.SUCCESS, []
        except OSError as error:
            return Status.FAILURE, str(error).splitlines()

    def __str__(self):
        inline = self.content.replace("\n", " ").strip()
        return 'copy "' + (inline[:47] + "..." if len(inline) > 50 else inline) + '" to "' + self.target + '"'


@dataclass
class Task:
    entry: _Entry
    status: Status
    output: List[str] = field(init=False)

    def execute(self, **kwargs) -> None:
        self.status, self.output = self.entry.execute(**kwargs)

    def write_report(self, reports_path: Path) -> None:
        reports_path.joinpath(self.entry.md5).write_text(json.dumps(asdict(self), indent=2), encoding=ENCODING)
