import os
import qrcode

def generate_qr_code(data, output_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(output_path)

# Example usage
if __name__ == "__main__":
    data = 'https://github.com/Karan3R'
    output_path = 'C:/Users/ADMIN/Downloads/qr_code.png'  # Make sure this path is correct
    generate_qr_code(data, output_path)
    print(f'QR Code generated and saved as {output_path}')
