import base64
import requests
import dotenv
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("main_app.log"),
        logging.StreamHandler()
    ]
  )

IMAGE_PATH = "./media/CURRENT.jpg"
PROMPT = "You're task is to create a narration to this image. What is the person doing? What are their intentions? You can speculate freely."

dotenv.load_dotenv()
API_KEY_OPENAI = os.getenv("API_OPENAI")
if API_KEY_OPENAI is None:
  raise Exception("API_OPENAI is not set or env file is not loaded")
# OpenAI API Key


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 strin
def get_description(image_path = IMAGE_PATH):
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY_OPENAI}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": PROMPT
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  logger.debug(response.json())

  return response.json()["choices"][0]["text"]

