#!/usr/bin/env python3
"""Tests for the Two Dice Comprehension assignment."""

import contextlib
import io
import re
import unittest

from src.two_dice_comprehension import main


class TestMain(unittest.TestCase):
    """main() prints every (a, b) pair of dice values that sum to 5."""

    def test_lines(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            main()
        result = out.getvalue().split('\n')
        self.assertEqual(
            len(result),
            4,
            msg="main() should print exactly four lines (plus the trailing "
            "newline), one for each (a, b) pair of dice values that sums to "
            "5. Got %d lines: %r." % (len(result), result),
        )

    def test_content(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            main()
        result = out.getvalue().split('\n')
        pattern = r'\((\d),\s*(\d)\)'
        s = set()
        for line in result:
            self.assertRegex(
                line,
                pattern,
                msg="Line %r did not contain a pair of numbers formatted "
                "like '(a, b)'." % (line,),
            )
            m = re.match(pattern, line)
            a = int(m.group(1))
            b = int(m.group(2))
            self.assertEqual(
                a + b,
                5,
                msg="Printed pair (%d, %d) does not sum to 5." % (a, b),
            )
            self.assertIn(
                a,
                range(1, 7),
                msg="The value of a dice should be between 1 and 6, got %d."
                % (a,),
            )
            self.assertIn(
                b,
                range(1, 7),
                msg="The value of a dice should be between 1 and 6, got %d."
                % (b,),
            )
            s.add((a, b))
        self.assertEqual(
            len(s),
            4,
            msg="Output should contain four distinct pairs. Got %r." % (s,),
        )


if __name__ == '__main__':
    unittest.main()
