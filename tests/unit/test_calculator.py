import pytest
from src.calculator import add, subtract, multiply, divide, power, sqrt


class TestBasicOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_subtract_positive_numbers(self):
        assert subtract(5, 2) == 3


class TestMultiplyDivideWithValidation:
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestMultiplyDivide:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-3, 4) == -12

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5


class TestAdvancedOperations:
    def test_power_positive_numbers(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(2, 0) == 1

    def test_square_root_positive_numbers(self):
        assert sqrt(16) == 4

    def test_square_root_negative_raises_error(self):
        with pytest.raises(
            ValueError, match="Cannot take square root of negative number"
        ):
            sqrt(-4)
