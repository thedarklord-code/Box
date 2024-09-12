from PIL import Image
import pytesseract
import cv2

# Path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'hinalpatel/local/bin/tesseract'

def extract_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to RGB (Tesseract expects RGB images)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(rgb_image)
    
    return text

if __name__ == "__main__":
    image_path = '/Users/hinalpatel/Downloads/1.jpeg'  # Replace with your image path
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:", extracted_text)
