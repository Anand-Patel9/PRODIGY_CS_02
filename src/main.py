import os
import argparse
from encryption.image_encryptor import ImageEncryptor
from utils.file_handlers import FileHandler

def main():
    parser = argparse.ArgumentParser(description="Image Encryption Tool using Pixel Manipulation")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Action to perform")
    parser.add_argument('input_image', help="Path to input image file")
    parser.add_argument('output_image', help="Path to save output image file")
    parser.add_argument('--method', choices=['swap', 'xor', 'add'], default='swap',
                       help="Encryption/decryption method to use")
    
    args = parser.parse_args()
    
    # Validate input
    if not FileHandler.validate_path(args.input_image):
        print(f"Error: Input file '{args.input_image}' not found or inaccessible")
        return
    
    if not FileHandler.is_valid_image_file(args.input_image):
        print("Error: Input file must be a valid image (jpg, png, bmp, tiff)")
        return
    
    # Ensure output directory exists
    output_dir = os.path.dirname(args.output_image)
    if output_dir:
        FileHandler.create_directory(output_dir)
    
    # Perform encryption/decryption
    encryptor = ImageEncryptor()
    
    if args.action == 'encrypt':
        success = encryptor.encrypt_image(args.input_image, args.output_image, args.method)
        if success:
            print(f"Image successfully encrypted using {args.method} method")
    else:
        success = encryptor.decrypt_image(args.input_image, args.output_image, args.method)
        if success:
            print(f"Image successfully decrypted using {args.method} method")

if __name__ == "__main__":
    main()