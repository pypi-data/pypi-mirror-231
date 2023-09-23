import contextlib
import sys
from typing import Any, Callable, Generator
import typing


@contextlib.contextmanager
def frict() -> Generator[Callable[[Any, str, str, typing.IO[str], bool], None], None, None]:
    previous_lines = 0

    def _frict(
        *obj: Any,
        sep: str = '',
        end: str = '\n',
        file: typing.IO[str] = sys.stdout,
        flush: bool = False,
    ) -> None:
        nonlocal previous_lines

        if previous_lines:
            print(f'\033[{previous_lines}A\033[J', end='', file=file, flush=True)

        previous_lines = sum((str(elm) + end).count('\n') for elm in obj)
        print(*obj, sep=sep, end=end, file=file, flush=flush)

    yield _frict
