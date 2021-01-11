import pytest
from run import Joltage

def test_joltage():
    joltage = Joltage('input_test.txt')
    assert joltage.part1() == 22*10
    assert joltage.part2() == 19208