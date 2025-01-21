from PIL import Image
import pytesseract

# Load the image
img = Image.open("expression_1.png")

# Extract the text from the image
extracted_text = pytesseract.image_to_string(img)

# Clean the text to remove unwanted characters (like newlines)
expression = extracted_text.strip()

# Evaluate the expression
try:
    result = eval(expression)
    print(f"The result of '{expression}' is: {result}")
except Exception as e:
    print(f"Error: {e}")
