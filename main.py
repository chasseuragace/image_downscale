from PIL import Image
import os

def reduce_image_size(input_path, output_path, quality=85):
    """
    Reduce the file size of an image.

    Parameters:
    - input_path: Path to the input image file.
    - output_path: Path to save the output image file.
    - quality: Quality setting for the output image (1-100). Higher is better quality.

    Returns:
    - None
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Convert the image to RGB if it is in a different mode (e.g., RGBA, P)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Save the image with the specified quality
            img.save(output_path, "JPEG", quality=quality, optimize=True)
    except Exception as e:
        print(f"Error reducing image size for {input_path}: {e}")

def process_images(input_folder, output_folder_base, qualities):
    # Ensure output base folder exists
    if not os.path.exists(output_folder_base):
        os.makedirs(output_folder_base)
    
    for quality in qualities:
        output_folder = os.path.join(output_folder_base, f"quality{quality}")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            if os.path.isfile(input_path):
                reduce_image_size(input_path, output_path, quality)

if __name__ == "__main__":
    input_folder = "/input_images"
    output_folder_base = "/output_images"
    qualities = [10, 30, 50, 70, 80, 90]
    
    process_images(input_folder, output_folder_base, qualities)