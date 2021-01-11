import pytest
from run import Debugger

def test_debugger():
    d = Debugger('debugger_test.txt', preamble=5)
    result_part1 = d.part1()
    assert result_part1 == 127
    result_part2 = d.part2(result_part1)
    assert result_part2 == 62
