import collections
import functools
import operator
import sys
import types
from typing import Any, Counter, Final

TOOL: Final[int] = 2
PY_CALLABLES: Final[tuple] = (types.FunctionType, types.MethodType)
MONITOR = sys.monitoring  # type:ignore

EVENTS = MONITOR.events
TRACKED_EVENTS: tuple[tuple[int, str], ...] = (
    (EVENTS.PY_START, "PY_START"),
    (EVENTS.PY_RESUME, "RESUME"),
    (EVENTS.PY_THROW, "THROW"),
    (EVENTS.PY_RETURN, "PY_RETURN"),
    (EVENTS.PY_YIELD, "YIELD"),
    (EVENTS.PY_UNWIND, "UNWIND"),
    (EVENTS.C_RAISE, "C_RAISE"),
    (EVENTS.C_RETURN, "C_RETURN"),
    (EVENTS.EXCEPTION_HANDLED, "EXCEPTION_HANDLED"),
    (EVENTS.STOP_ITERATION, "STOP ITERATION"),
)
EVENT_SET: int = (
    functools.reduce(operator.or_, [ev for (ev, _) in TRACKED_EVENTS], 0) | EVENTS.CALL
)


class Akarsu:
    def __init__(self, code: str, file_name: str) -> None:
        self.code = code
        self.file_name = file_name

    def wrap_code(self):
        if code := self.code.strip():
            indented_code = "\n".join(f"    {line}" for line in code.splitlines())
            source = f"def ____wrapper____():\n{indented_code}\n____wrapper____()"
            self.code = compile(source, self.file_name, "exec")

    def profile(self) -> tuple[list[tuple[str, str, str]], Counter]:
        self.wrap_code()
        events = []

        for event, event_name in TRACKED_EVENTS:

            def record(*args: Any, event_name: str = event_name) -> None:
                code = args[0]
                pattern = event_name, f"{code.co_filename}", f"{code.co_name}"
                events.append(pattern)

            MONITOR.register_callback(TOOL, event, record)

        def record_call(code: types.CodeType, offset: int, obj: Any, arg: Any) -> None:
            file_name = f"{code.co_filename}"
            if isinstance(obj, PY_CALLABLES):
                events.append(("PY_CALL", file_name, str(obj.__code__.co_name)))
            else:
                events.append(("C_CALL", file_name, str(obj)))

        MONITOR.use_tool_id(TOOL, f"{self.__class__.__name__}")
        MONITOR.register_callback(TOOL, EVENTS.CALL, record_call)
        MONITOR.set_events(TOOL, EVENT_SET)
        try:
            exec(self.code)
        except:
            pass
        MONITOR.set_events(TOOL, 0)
        MONITOR.free_tool_id(TOOL)

        return self.format_events(events)

    @staticmethod
    def format_events(
        events: list[tuple[str, str, str]]
    ) -> tuple[list[tuple[str, str, str]], Counter]:
        filtered_events = []
        counter: Counter = collections.Counter()

        for event in events[2:-3]:
            if "____wrapper____" not in event[2]:
                filtered_events.append(event)
                counter[event[0]] += 1

        return filtered_events, counter
