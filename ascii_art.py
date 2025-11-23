from PIL import Image
import sys

def image_to_ascii(image_path, width=100):
    """
    Converts an image to ASCII art.
    
    Args:
    - image_path: Path to the input image file.
    - width: Desired width of the ASCII art (height scales proportionally).
    
    Returns:
    - A string representing the ASCII art.
    """
    # ASCII characters from darkest to lightest
    ascii_chars = "@%#*+=-:. "
    
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Convert to grayscale
        img = img.convert('L')
        
        # Calculate new height to maintain aspect ratio
        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio * 0.5)  # 0.5 to account for character aspect ratio
        
        # Resize the image
        img = img.resize((width, height))
        
        # Get pixel data
        pixels = list(img.getdata())
        
        # Map pixels to ASCII
        ascii_art = ""
        for i in range(0, len(pixels), width):
            row = pixels[i:i+width]
            ascii_row = "".join(ascii_chars[pixel * len(ascii_chars) // 256] for pixel in row)
            ascii_art += ascii_row + "\n"
        
        return ascii_art
    except Exception as e:
        return f"Error processing image: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ascii_art.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)
