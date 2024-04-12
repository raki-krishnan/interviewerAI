import google.generativeai as genai
import os
from PIL import Image


# Configure the API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Example: Generate text content
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Give me python code to sort a list")
print(response.text)

# Example: Use images in your prompt
img = Image.open('smile.jpg')
prompt = "This image contains a sketch of a potential product along with some notes. Given the product sketch, describe the product as thoroughly as possible based on what you see in the image, making sure to note all of the product features. Return output in json format: {description: description, features: [feature1, feature2, feature3, etc]}"
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content([prompt, img])
print(response.text)
