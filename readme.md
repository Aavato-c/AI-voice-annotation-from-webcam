# Elevenlabs webcam descriptor

The source is quite simple. I don't think it's necessary to explain everything here but in short:
- The script will save frames from your webcam and store them in the media -folder
  - The most recent frame will be used to make a call to an OpenAI multimodal-endpoint
  - As the descriptions are generated, the dubs are then generated via ElevenLabs API
  - The sound files will also be stored



To start using this little thing do the following:
* Make a venv using python3.8
  * `python3.8 venv -m venv`
* Activate the environment (Linux/MacOs)
  * `source venv/bin/activate`
* Install dependencies
  * `pip install -r requirements.txt`
* Make your own env
  * You can use the env.example provided, remove the .example extension and fill in your api keys
* Run the save_video_frames.py
  * `python3 save_video_frames.py`
* Run the main_app.py
  * `python3 main_app.py`
* Enjoy



