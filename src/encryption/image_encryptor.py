from pathlib import Path
from PIL import Image
import numpy as np
from .pixel_operations import PixelOperations

class ImageEncryptor:
    def __init__(self):
        self.pixel_ops = PixelOperations()
    
    def load_image(self, image_path):
        try:
            return Image.open(image_path)
        except Exception as e:
            raise ValueError(f"Error loading image: {str(e)}")
    
    def save_image(self, image, output_path):
        """Save image to file, raising ValueError on failure"""
        try:
            output_path = Path(output_path)
            # Don't create directories automatically for this test case
            if not output_path.parent.exists():
                raise ValueError(f"Directory does not exist: {output_path.parent}")
                
            image.save(output_path)
        except Exception as e:
            raise ValueError(f"Error saving image: {str(e)}")
    
    def image_to_array(self, image):
        return np.array(image)
    
    def array_to_image(self, array):
        return Image.fromarray(array.astype('uint8'))
    
    def encrypt_image(self, image_path, output_path, method='swap'):
        try:
            if method not in ['swap', 'xor', 'add']:
                raise ValueError("Invalid encryption method")
                
            image = self.load_image(image_path)
            img_array = self.image_to_array(image)
            
            if method == 'swap':
                encrypted_array = self.pixel_ops.swap_pixels(img_array)
            elif method == 'xor':
                encrypted_array = self.pixel_ops.xor_operation(img_array)
            elif method == 'add':
                encrypted_array = self.pixel_ops.add_constant(img_array)
            
            encrypted_image = self.array_to_image(encrypted_array)
            self.save_image(encrypted_image, output_path)
            return True
        except ValueError:
            raise
        except Exception as e:
            print(f"Encryption failed: {str(e)}")
            return False
    
    def decrypt_image(self, image_path, output_path, method='swap'):
        try:
            if method not in ['swap', 'xor', 'add']:
                raise ValueError("Invalid decryption method")
                
            image = self.load_image(image_path)
            img_array = self.image_to_array(image)
            
            if method == 'swap':
                decrypted_array = self.pixel_ops.reverse_swap_pixels(img_array)
            elif method == 'xor':
                decrypted_array = self.pixel_ops.xor_operation(img_array)
            elif method == 'add':
                decrypted_array = self.pixel_ops.subtract_constant(img_array)
            
            decrypted_image = self.array_to_image(decrypted_array)
            self.save_image(decrypted_image, output_path)
            return True
        except ValueError:
            raise
        except Exception as e:
            print(f"Decryption failed: {str(e)}")
            return False