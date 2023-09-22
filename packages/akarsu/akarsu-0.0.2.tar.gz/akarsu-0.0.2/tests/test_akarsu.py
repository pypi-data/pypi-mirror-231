import textwrap
import unittest
from collections import Counter

from akarsu.akarsu import Akarsu


class TestNine(unittest.TestCase):
    def test_profile_print(self):
        code = "print('Hello, world!')"
        events, event_counter = Akarsu(code, "<string>").profile()
        self.assertEqual(len(events), 1)
        self.assertEqual(event_counter, Counter({"C_CALL": 1}))
        self.assertEqual(events[0], ("C_CALL", "<string>", "<built-in function print>"))

    def test_profile_isinstance(self):
        code = "isinstance(1, int)"
        events, event_counter = Akarsu(code, "<string>").profile()
        self.assertEqual(len(events), 1)
        self.assertEqual(event_counter, Counter({"C_CALL": 1}))
        self.assertEqual(
            events[0], ("C_CALL", "<string>", "<built-in function isinstance>")
        )

    def test_profile_generator(self):
        code = "list(i for i in range(5))"
        events, event_counter = Akarsu(code, "<string>").profile()
        self.assertEqual(len(events), 15)
        self.assertEqual(
            event_counter,
            Counter(
                {
                    "YIELD": 5,
                    "RESUME": 5,
                    "C_CALL": 2,
                    "PY_CALL": 1,
                    "PY_START": 1,
                    "PY_RETURN": 1,
                }
            ),
        )
        self.assertEqual(events[0], ("C_CALL", "<string>", "<class 'range'>"))
        self.assertEqual(events[1], ("PY_CALL", "<string>", "<genexpr>"))
        self.assertEqual(events[2], ("C_CALL", "<string>", "<class 'list'>"))
        self.assertEqual(events[3], ("PY_START", "<string>", "<genexpr>"))
        self.assertEqual(events[4], ("YIELD", "<string>", "<genexpr>"))
        self.assertEqual(events[5], ("RESUME", "<string>", "<genexpr>"))
        self.assertEqual(events[6], ("YIELD", "<string>", "<genexpr>"))
        self.assertEqual(events[7], ("RESUME", "<string>", "<genexpr>"))
        self.assertEqual(events[8], ("YIELD", "<string>", "<genexpr>"))
        self.assertEqual(events[9], ("RESUME", "<string>", "<genexpr>"))
        self.assertEqual(events[10], ("YIELD", "<string>", "<genexpr>"))
        self.assertEqual(events[11], ("RESUME", "<string>", "<genexpr>"))
        self.assertEqual(events[12], ("YIELD", "<string>", "<genexpr>"))
        self.assertEqual(events[13], ("RESUME", "<string>", "<genexpr>"))
        self.assertEqual(events[14], ("PY_RETURN", "<string>", "<genexpr>"))

    def test_profile_empty_code(self):
        code = ""
        events, event_counter = Akarsu(code, "<string>").profile()
        self.assertEqual(event_counter, Counter())
        self.assertEqual(len(events), 0)

    def test_profile_multiple_calls(self):
        code = "print('Hello, world!'); print('Goodbye, world!')"
        events, event_counter = Akarsu(code, "<string>").profile()
        self.assertEqual(len(events), 2)
        self.assertEqual(event_counter, Counter({"C_CALL": 2}))
        self.assertEqual(events[0], ("C_CALL", "<string>", "<built-in function print>"))
        self.assertEqual(events[1], ("C_CALL", "<string>", "<built-in function print>"))

    def test_profile_nested_functions(self):
        source = textwrap.dedent("""
            def foo():
                print("Hello, world!")
            def bar():
                foo()
            bar()
            """)
        events, event_counter = Akarsu(source, "<string>").profile()
        self.assertEqual(
            event_counter,
            Counter(
                {
                    "PY_CALL": 2,
                    "PY_START": 2,
                    "PY_RETURN": 2,
                    "C_CALL": 1,
                    "C_RETURN": 1,
                }
            ),
        )
        self.assertEqual(len(events), 8)
        self.assertEqual(events[0], ("PY_CALL", "<string>", "bar"))
        self.assertEqual(events[1], ("PY_START", "<string>", "bar"))
        self.assertEqual(events[2], ("PY_CALL", "<string>", "foo"))
        self.assertEqual(events[3], ("PY_START", "<string>", "foo"))
        self.assertEqual(events[4], ("C_CALL", "<string>", "<built-in function print>"))
        self.assertEqual(events[5], ("C_RETURN", "<string>", "foo"))
        self.assertEqual(events[6], ("PY_RETURN", "<string>", "foo"))
        self.assertEqual(events[7], ("PY_RETURN", "<string>", "bar"))

    def test_profile_function_with_multiple_args(self):
        source = textwrap.dedent("""
            def foo(x, y, z=10):
                print(x, y, z)

            foo(1, 2, z=3)
            """)
        events, event_counter = Akarsu(source, "<string>").profile()

        self.assertEqual(len(events), 5)
        self.assertEqual(
            event_counter,
            Counter(
                {
                    "PY_CALL": 1,
                    "PY_START": 1,
                    "C_CALL": 1,
                    "C_RETURN": 1,
                    "PY_RETURN": 1,
                }
            ),
        )
        self.assertEqual(events[0], ("PY_CALL", "<string>", "foo"))
        self.assertEqual(events[1], ("PY_START", "<string>", "foo"))
        self.assertEqual(events[2], ("C_CALL", "<string>", "<built-in function print>"))
        self.assertEqual(events[3], ("C_RETURN", "<string>", "foo"))
        self.assertEqual(events[4], ("PY_RETURN", "<string>", "foo"))

    def test_profile_class(self):
        source = textwrap.dedent("""
            class C:
                def foo(self):
                    pass
            """)

        events, event_counter = Akarsu(source, "<string>").profile()
        self.assertEqual(len(events), 3)
        self.assertEqual(
            event_counter,
            Counter({"C_CALL": 1, "PY_START": 1, "PY_RETURN": 1}),
        )
        self.assertEqual(
            events[0], ("C_CALL", "<string>", "<built-in function __build_class__>")
        )
        self.assertEqual(events[1], ("PY_START", "<string>", "C"))
        self.assertEqual(events[2], ("PY_RETURN", "<string>", "C"))

        source = textwrap.dedent("""
            class C:
                def foo(self):
                    x = 1
            c = C()
            c.foo()
            """)

        events, event_counter = Akarsu(source, "<string>").profile()
        self.assertEqual(len(events), 6)
        self.assertEqual(
            event_counter,
            Counter({"PY_START": 2, "PY_RETURN": 2, "C_CALL": 1, "PY_CALL": 1}),
        )
        self.assertEqual(
            events[0], ("C_CALL", "<string>", "<built-in function __build_class__>")
        )
        self.assertEqual(events[1], ("PY_START", "<string>", "C"))
        self.assertEqual(events[2], ("PY_RETURN", "<string>", "C"))
        self.assertEqual(events[3], ("PY_CALL", "<string>", "foo"))
        self.assertEqual(events[4], ("PY_START", "<string>", "foo"))
        self.assertEqual(events[5], ("PY_RETURN", "<string>", "foo"))

    def test_profile_class_method(self):
        source = textwrap.dedent("""
            class MyClass:
                @classmethod
                def foo(cls):
                    print("Hello, world!")
            my_class = MyClass()
            my_class.foo()
            """)
        events, event_counter = Akarsu(source, "<string>").profile()

        self.assertEqual(len(events), 10)
        self.assertEqual(
            event_counter,
            Counter(
                {
                    "C_CALL": 3,
                    "PY_START": 2,
                    "C_RETURN": 2,
                    "PY_RETURN": 2,
                    "PY_CALL": 1,
                }
            ),
        )
        self.assertEqual(
            events[0], ("C_CALL", "<string>", "<built-in function __build_class__>")
        )
        self.assertEqual(events[1], ("PY_START", "<string>", "MyClass"))
        self.assertEqual(events[2], ("C_CALL", "<string>", "<class 'classmethod'>"))
        self.assertEqual(events[3], ("C_RETURN", "<string>", "MyClass"))
        self.assertEqual(events[4], ("PY_RETURN", "<string>", "MyClass"))
        self.assertEqual(events[5], ("PY_CALL", "<string>", "foo"))
        self.assertEqual(events[6], ("PY_START", "<string>", "foo"))
        self.assertEqual(events[7], ("C_CALL", "<string>", "<built-in function print>"))
        self.assertEqual(events[8], ("C_RETURN", "<string>", "foo"))
        self.assertEqual(events[9], ("PY_RETURN", "<string>", "foo"))
