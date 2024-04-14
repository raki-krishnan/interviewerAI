import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
from moviepy.editor import VideoFileClip

# helpful for video processing
import cv2
import os
import shutil

load_dotenv()

# Configure the API key
GOOGLE_API_KEY=os.environ['GOOGLE_API_KEY']



#path = "/home/shreyanp/projects/mhacks/frontend/src/Components/Files/IMG_4184.mov"

#attempt to convert from WEBM to MP4

genai.configure(api_key=GOOGLE_API_KEY)
#----------------------------------------------
class File:
  def __init__(self, file_path: str, display_name: str = None):
    self.file_path = file_path
    if display_name:
      self.display_name = display_name
    self.timestamp = get_timestamp(file_path)

  def set_file_response(self, response):
    self.response = response


# splits audio and video and can return a path to the audio-less clip
def split_audio_video(video_file_path):
    # Load the video file
    video_clip = VideoFileClip(video_file_path)

    # Extract the audio
    audio_clip = video_clip.audio
    audio_file_path = "extracted_audio.mp3"  # Choose your desired audio format and filename
    audio_clip.write_audiofile(audio_file_path)

    # Save the video without audio (optional)
    video_clip_no_audio = video_clip.set_audio(None)
    video_file_path_no_audio = "video_without_audio.mp4"  # Choose your desired video format and filename
    video_clip_no_audio.write_videofile(video_file_path_no_audio)

    return audio_file_path, video_file_path_no_audio

# Create or cleanup existing extracted image frames directory.
FRAME_EXTRACTION_DIRECTORY = "backend/extracted_frames"
FRAME_PREFIX = "AT_TIME"
def create_frame_output_dir(output_dir):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  else:
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)




def extract_frame_from_video(video_file_path):
  print(f"Extracting {video_file_path} at 1 frame per second. This might take a bit...")
  create_frame_output_dir(FRAME_EXTRACTION_DIRECTORY)
  vidcap = cv2.VideoCapture(video_file_path)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_duration = 1 / fps  # Time interval between frames (in seconds)
  output_file_prefix = os.path.basename(video_file_path).replace('.', '_')
  frame_count = 0
  count = 0
  while vidcap.isOpened():
      success, frame = vidcap.read()
      if not success: # End of video
          break
      if int(count / fps) == frame_count: # Extract a frame every second
          min = frame_count // 60
          sec = frame_count % 60
          time_string = f"{min:02d}:{sec:02d}"
          image_name = f"{output_file_prefix}{FRAME_PREFIX}{time_string}.jpg"
          output_filename = os.path.join(FRAME_EXTRACTION_DIRECTORY, image_name)
          cv2.imwrite(output_filename, frame)
          frame_count += 1
      count += 1
  vidcap.release() # Release the capture object\n",
  print(f"Completed video frame extraction!\n\nExtracted: {frame_count} frames")

def get_timestamp(filename):
  """Extracts the frame count (as an integer) from a filename with the format
     'output_file_prefix_frame00:00.jpg'.
  """
  parts = filename.split(FRAME_PREFIX)
  if len(parts) != 2:
      return None  # Indicates the filename might be incorrectly formatted
  return parts[1].split('.')[0]

def master_function(question, MOVpath, jobTitle, companyName):
  model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", system_instruction="Your task is to give feedback to a candidate"
                                " who is applying for the " + jobTitle + "position at " + companyName + ". Please use what you know about this company" + 
                                " and the role to give specific feedback. Thank you!")
  feedbackResponses = []
  # actual extraction of frames:
  audiopath, videopath = split_audio_video(MOVpath)
  audiopathfile = genai.upload_file(path="extracted_audio.mp3")

  promptaudio = "This audio is a response to this interview question:" + question + "." + "Please give some pros and cons about it within 4 sentences. Thank you!"
  response_audio = model.generate_content([promptaudio, audiopathfile])
  extract_frame_from_video(videopath)

  feedbackResponses.append(response_audio)

  #-----------------------------

  # Process each frame in the output directory
  files = os.listdir(FRAME_EXTRACTION_DIRECTORY)
  files = sorted(files)
  files_to_upload = []
  for file in files:
    files_to_upload.append(
        File(file_path=os.path.join(FRAME_EXTRACTION_DIRECTORY, file)))

  # Upload the files to the API
  # Only upload a 10 second slice of files to reduce upload time.
  # Change full_video to True to upload the whole video.
  full_video = True
  uploaded_files = []
  print(f'Uploading {len(files_to_upload) if full_video else 10} files. This might take a bit...')
  for file in files_to_upload if full_video else files_to_upload[40:50]:
    print(f'Uploading: {file.file_path}...')
    response = genai.upload_file(path=file.file_path)
    file.set_file_response(response)
    uploaded_files.append(file)

  prompt1 = "The following images are frames in a video that is a response to an interview question. "
  prompt2 = "Analyze the interviewee's facial expressions throughout the frames and give pros and cons about it in 4 sentences."
  prompt = prompt1 + prompt2

  # Make GenerateContent request with the structure described above.

  request = [prompt]
  for file in uploaded_files:
    request.append(file.timestamp)
    request.append(file.response)

  response_video = model.generate_content(request, request_options={"timeout": 1000})
  feedbackResponses.append(response_video)
  return feedbackResponses
