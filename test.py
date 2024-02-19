# test.py
from main import StudentsInMLOps
import pytest

def test_enrollStudents():
    ops = StudentsInMLOps()
    ops.enrollStudents(5)
    assert ops.getTotalStrength() == 5

def test_dropStudents():
    ops = StudentsInMLOps()
    ops.enrollStudents(10)
    ops.dropStudents(3)
    assert ops.getTotalStrength() == 7

def test_getClassName():
    ops = StudentsInMLOps()
    assert ops.getClassName() == "StudentsInMLOps"
