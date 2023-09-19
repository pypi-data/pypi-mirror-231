import unittest

from resumer.gen.filter import ResumerFilter #noqa

class T_filter(unittest.TestCase):
    def test_filter_1(self):
        f = ResumerFilter(
            includes=["a", "z", "hh.b", "hh.c"],
            excludes=["b", "c", "f", "e.w"],
        )

        self.assertTrue(
            f.direct_match("a")
        )

        self.assertFalse(
            f.direct_match("b")
        )

        self.assertFalse(
            f.direct_match("d")
        )

        self.assertTrue(
            f.structured_match("b", "hh")
        )
        self.assertTrue(
            f.structured_match("c", "hh")
        )

        self.assertFalse(
            f.structured_match("w", "e")
        )

        self.assertFalse(
            f.structured_match("d", "hh")
        )

        self.assertTrue(
            f.direct_matches(
                ["a", "c"]
            )
        )

    def test_filter_2(self):
        f = ResumerFilter(
            includes=["a", "z", "hh.b", "hh.c"],
        )

        self.assertTrue(
            f.direct_match("a")
        )

        self.assertFalse(
            f.direct_match("b")
        )
