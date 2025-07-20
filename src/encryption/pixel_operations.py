import numpy as np

class PixelOperations:
    @staticmethod
    def swap_pixels(pixel_values):
        return np.roll(pixel_values, shift=-1, axis=-1)
    
    @staticmethod
    def reverse_swap_pixels(pixel_values):
        return np.roll(pixel_values, shift=1, axis=-1)
    
    @staticmethod
    def xor_operation(pixel_values, key=123):
        return np.bitwise_xor(pixel_values, key)
    
    @staticmethod
    def add_constant(pixel_values, constant=50):
        result = pixel_values.astype('int32') + constant
        return np.mod(result, 256).astype('uint8')
    
    @staticmethod
    def subtract_constant(pixel_values, constant=50):
        result = pixel_values.astype('int32') - constant
        return np.mod(result, 256).astype('uint8')