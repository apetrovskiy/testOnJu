from src.main.java.problems.volume001.The_3n_plus_1_problem.the_3n_plus_1_problem import the_3n_plus_1_problem
import pytest


test_data = [
    (1, 10, 20),
    (100, 200, 125),
    (201, 210, 89)  # ,
    # TODO
    # (900, 100, 174)
]


@pytest.mark.parametrize("i,j,expected_result", test_data)
def test_the_3n_plus_1_problem(i: int, j: int, expected_result: int):
    assert expected_result == the_3n_plus_1_problem(i, j)
