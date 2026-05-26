"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0,0],[0,0],[0,0]],[0,0]),
            ([[1,2],[3,4],[5,6]],[3,4]),
            (np.zeros((3,5)), np.zeros(5))
        ]
)

def test_daily_mean(test_input, test_result):
    """Test that mean function works for both zeros anf integers"""
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
        "test_input_max, test_result_max",
        [
            ([[0,0],[0,0],[0,0]],[0,0]),
            ([[1,2],[3,4],[5,6]],[5,6]),
            (np.zeros((3,5)), np.zeros(5))
        ]
)


def test_daily_max(test_input_max, test_result_max):
    """Test that max function works for both zeros anf integers"""
    npt.assert_array_equal(daily_max(test_input_max), test_result_max)



# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
    

#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""

#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)

# def test_daily_max():
#     """Test that max function works for an array of positive integers."""

#     test_input = np.array([[-1, 2],
#                            [3, 4],
#                            [5, -6]])
#     test_result = np.array([5, 4])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_max(test_input), test_result)

# def test_daily_min():
#     """Test that min function works for an array of positive integers."""

#     test_input = np.array([[-1, 2],
#                            [3, 4],
#                            [5, -6]])
#     test_result = np.array([-1, -6])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_min(test_input), test_result)

# def test_daily_max_string():


#     """Test for type error when parsing strings"""

#     with pytest.raises(TypeError):
#         error_expected = daily_max(['Hello', 'there'])

# def test_daily_average():

#     """Test that mean function works providing a value into the range."""

#     with pytest.raises(TypeError):
#         error_expected = daily_mean(['Ciao', 'bello'])


