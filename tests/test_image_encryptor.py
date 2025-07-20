import pytest
import numpy as np
from PIL import Image
from src.encryption.image_encryptor import ImageEncryptor
from src.utils.file_handlers import FileHandler

class TestImageEncryptor:
    @pytest.fixture
    def encryptor(self):
        return ImageEncryptor()

    @pytest.fixture
    def sample_image(self, tmp_path):
        # Create a temporary image for testing
        img_path = tmp_path / "test_image.png"
        img_array = np.array([[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8)
        img = Image.fromarray(img_array)
        img.save(img_path)
        return img_path

    def test_load_image(self, encryptor, sample_image):
        img = encryptor.load_image(sample_image)
        assert isinstance(img, Image.Image)

    def test_load_invalid_image(self, encryptor):
        with pytest.raises(ValueError):
            encryptor.load_image("nonexistent_image.jpg")

    def test_image_to_array_conversion(self, encryptor, sample_image):
        img = encryptor.load_image(sample_image)
        img_array = encryptor.image_to_array(img)
        assert isinstance(img_array, np.ndarray)
        assert img_array.shape == (1, 2, 3)  # 1x2 RGB image (corrected shape)

    def test_array_to_image_conversion(self, encryptor):
        test_array = np.array([[[10, 20, 30]]], dtype=np.uint8)
        img = encryptor.array_to_image(test_array)
        assert isinstance(img, Image.Image)

    def test_encrypt_decrypt_swap(self, encryptor, sample_image, tmp_path):
        output_path = tmp_path / "encrypted.png"
        decrypt_path = tmp_path / "decrypted.png"
        
        # Encrypt
        success = encryptor.encrypt_image(sample_image, output_path, 'swap')
        assert success
        assert FileHandler.validate_path(output_path)
        
        # Decrypt
        success = encryptor.decrypt_image(output_path, decrypt_path, 'swap')
        assert success
        assert FileHandler.validate_path(decrypt_path)
        
        # Verify original and decrypted images match
        original = encryptor.load_image(sample_image)
        decrypted = encryptor.load_image(decrypt_path)
        assert np.array_equal(encryptor.image_to_array(original), 
                             encryptor.image_to_array(decrypted))

    def test_encrypt_decrypt_xor(self, encryptor, sample_image, tmp_path):
        output_path = tmp_path / "encrypted_xor.png"
        decrypt_path = tmp_path / "decrypted_xor.png"
        
        # Encrypt
        success = encryptor.encrypt_image(sample_image, output_path, 'xor')
        assert success
        
        # Decrypt
        success = encryptor.decrypt_image(output_path, decrypt_path, 'xor')
        assert success
        
        # Verify
        original = encryptor.load_image(sample_image)
        decrypted = encryptor.load_image(decrypt_path)
        assert np.array_equal(encryptor.image_to_array(original), 
                             encryptor.image_to_array(decrypted))

    def test_encrypt_decrypt_add(self, encryptor, sample_image, tmp_path):
        output_path = tmp_path / "encrypted_add.png"
        decrypt_path = tmp_path / "decrypted_add.png"
        
        # Encrypt
        success = encryptor.encrypt_image(sample_image, output_path, 'add')
        assert success
        
        # Decrypt
        success = encryptor.decrypt_image(output_path, decrypt_path, 'add')
        assert success
        
        # Verify
        original = encryptor.load_image(sample_image)
        decrypted = encryptor.load_image(decrypt_path)
        assert np.array_equal(encryptor.image_to_array(original), 
                             encryptor.image_to_array(decrypted))

    def test_invalid_method(self, encryptor, sample_image, tmp_path):
        output_path = tmp_path / "output.png"
        with pytest.raises(ValueError):
            encryptor.encrypt_image(sample_image, output_path, 'invalid_method')
        
        with pytest.raises(ValueError):
            encryptor.decrypt_image(sample_image, output_path, 'invalid_method')

    def test_save_invalid_path(self, encryptor, sample_image, tmp_path):
        invalid_path = tmp_path / "nonexistent_dir" / "output.png"
        with pytest.raises(ValueError):
            encryptor.encrypt_image(sample_image, invalid_path, 'swap')