import subprocess
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import logging
import json
from video_processing import master_function


app = Flask(__name__, static_folder='build')
# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = 'uploaded_videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
shreyan = {"question": "", "path": "", "company": "", "role": ""}

@app.route('/videos/<filename>/')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/get-feedback/', methods=['GET'])
def get_feedback():
    # Simulated feedback
    feedback = {
        "feedback1": "Audio feedback...",
        "feedback2": "Facial expression feedback..."
    }
    response_array = master_function(shreyan["question"], shreyan["path"], shreyan["role"], shreyan["company"])
    feedback["feedback1"] = '#' + response_array[0].text
    feedback["feedback2"] = '#' + response_array[1].text
    print(f"Feedback: {feedback}")
    return jsonify(feedback)

@app.route('/upload-video/', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"converted_{os.path.splitext(filename)[0]}.mov")

        # Save the file
        file.save(file_path)
        #if there is alread a file with the same name, delete it
        if os.path.exists(output_path):
            os.remove(output_path)

        # Convert the file to MOV format using ffmpeg
        try:
            subprocess.run(['ffmpeg', '-i', file_path, output_path], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to convert video: {e}")
            return jsonify({"message": "Conversion failed"}), 500
        
        shreyan["path"] = output_path
        return jsonify({"message": "File successfully uploaded and converted", "path": output_path}), 200


@app.route('/submit-question/', methods=['POST'])
def submit_question():
    print("Received request: ", request)
    try: 
        data = json.loads(request.data)
    except Exception as e:
        print("Error: ", e)
    
    question = data.get('question')
    shreyan["question"] = question
    print(f"Question received: {question}")
    question_json = {
        "message": "Question received",
        "question": question
    }
    return jsonify(question_json), 200

@app.route('/submit-company/', methods=['POST'])
def submit_company():
    print("Received request: ", request)
    try: 
        data = json.loads(request.data)
    except Exception as e:
        print("Error: ", e)
    
    question = data.get('question')
    shreyan["company"] = question
    print(f"Company received: {question}")
    question_json = {
        "message": "Company received",
        "question": question
    }
    return jsonify(question_json), 200

@app.route('/submit-role/', methods=['POST'])
def submit_role():
    print("Received request: ", request)
    try: 
        data = json.loads(request.data)
    except Exception as e:
        print("Error: ", e)
    
    question = data.get('question')
    shreyan["role"] = question
    print(f"Question received: {question}")
    question_json = {
        "message": "Role received",
        "question": question
    }
    return jsonify(question_json), 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>/')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
