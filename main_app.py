import base64
import requests
import dotenv
import os
import logging
import datetime

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

# Elevenlabs configs

VOICE_ID = "29vD33N1CtxCmqQRPOHJ"

dotenv.load_dotenv()
API_KEY_OPENAI = os.getenv("API_OPENAI")
API_KEY_ELEVENLABS = os.getenv("API_ELEVENLABS")
if API_KEY_OPENAI is None or API_KEY_ELEVENLABS is None:
  raise Exception("Api keys not set or env file is not loaded")
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



def call_elevenlabs_api(text):
  CHUNK_SIZE = 1024
  url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "<xi-api-key>"
  }

  data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)
  timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")
  with open(f"./media/audio_{timestamp}.mp3", 'wb') as f:
      for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if chunk:
              f.write(chunk)

  logger.debug(response.json())

  return response.json()

