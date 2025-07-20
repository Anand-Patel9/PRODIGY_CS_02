import numpy as np
import pytest
from src.encryption.pixel_operations import PixelOperations

class TestPixelOperations:
    @pytest.fixture
    def pixel_ops(self):
        return PixelOperations()

    def test_swap_pixels(self, pixel_ops):
        # Test with RGB pixel
        input_pixels = np.array([[[10, 20, 30]]])
        expected_output = np.array([[[20, 30, 10]]])
        result = pixel_ops.swap_pixels(input_pixels)
        assert np.array_equal(result, expected_output)

        # Test with multiple pixels
        input_pixels = np.array([[[10, 20, 30], [40, 50, 60]]])
        expected_output = np.array([[[20, 30, 10], [50, 60, 40]]])
        result = pixel_ops.swap_pixels(input_pixels)
        assert np.array_equal(result, expected_output)

    def test_reverse_swap_pixels(self, pixel_ops):
        # Test with GBR pixel (swapped)
        input_pixels = np.array([[[20, 30, 10]]])
        expected_output = np.array([[[10, 20, 30]]])
        result = pixel_ops.reverse_swap_pixels(input_pixels)
        assert np.array_equal(result, expected_output)

    def test_xor_operation(self, pixel_ops):
        input_pixels = np.array([[[10, 20, 30]]])
        key = 123
        # 10 XOR 123 = 113, 20 XOR 123 = 111, 30 XOR 123 = 101
        expected_output = np.array([[[113, 111, 101]]])
        result = pixel_ops.xor_operation(input_pixels, key)
        assert np.array_equal(result, expected_output)

    def test_add_constant(self, pixel_ops):
        input_pixels = np.array([[[200, 210, 220]]])
        constant = 60
        # (200+60)%256=4, (210+60)%256=14, (220+60)%256=24
        expected_output = np.array([[[4, 14, 24]]])
        result = pixel_ops.add_constant(input_pixels, constant)
        assert np.array_equal(result, expected_output)

    def test_subtract_constant(self, pixel_ops):
        input_pixels = np.array([[[4, 14, 24]]])
        constant = 60
        # (4-60)%256=200, (14-60)%256=210, (24-60)%256=220
        expected_output = np.array([[[200, 210, 220]]])
        result = pixel_ops.subtract_constant(input_pixels, constant)
        assert np.array_equal(result, expected_output)