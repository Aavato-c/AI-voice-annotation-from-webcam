# Elevenlabs webcam descriptor

The source is quite simple. Go ahead and check it out, I don't think it's necessary to explain everything here but in short:

- This will save frames from your webcam and store them in the media -folder
  - The most current frame will be updated
- The other app makes calls to openai to get a description of the image, then send a request to elevenlabs to make a dub.
  - The sound files will also be stored



To start using this little thing do the following:

* Make a venv using python3.8
  * `python3.8 venv -m venv`
* Activate the environment
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


Made with a mac M1
