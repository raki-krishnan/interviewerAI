import React, { useState, useRef, useEffect } from 'react';
import './InterviewApp.css';

function VideoRecorder() {
  const [recording, setRecording] = useState(false);
  const [videoURL, setVideoURL] = useState(null);
  const mediaRecorderRef = useRef(null);
  const videoRef = useRef(null);
  const streamRef = useRef(null);

  const startCamera = async () => {
    try {
      streamRef.current = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      videoRef.current.srcObject = streamRef.current;
    } catch (error) {
      console.error("Error accessing media devices.", error);
    }
  };

  useEffect(() => {
    startCamera();
    // Make sure to stop the camera stream when the component unmounts
    return () => {
      if (streamRef.current) {
        streamRef.current.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  const startRecording = async () => {
    try {
      streamRef.current = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      videoRef.current.srcObject = streamRef.current;
      mediaRecorderRef.current = new MediaRecorder(streamRef.current);
      mediaRecorderRef.current.addEventListener("dataavailable", handleDataAvailable);
      mediaRecorderRef.current.start();
      setRecording(true);
      // Reset the video URL if you want to allow for a new recording after stopping a previous one
      setVideoURL(null);
    } catch (error) {
      console.error("Error accessing media devices.", error);
    }
  };

  const handleDataAvailable = (event) => {
    if (event.data.size > 0) {
      setVideoURL(URL.createObjectURL(event.data));
    }
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    streamRef.current.getTracks().forEach(track => track.stop());
    setRecording(false);
  };

  const handleSubmit = async () => {
    console.log('Submit the video here...');
    // Add the code to upload the video to your backend here.
    // After submitting, you can reset the videoURL to null to remove the playback video
    setVideoURL(null);
    startCamera();
  };

  return (
    <div className = "container">
        <div className="video-recorder">
            <div className="camera-feed">
                <video ref={videoRef} className="video-preview" autoPlay muted />
            </div>
            <div className="controls">
                {recording
                ? <button className="button stop" onClick={stopRecording}>Stop Recording</button>
                : <button className="button start" onClick={startRecording}>Start Recording</button>}
            </div>
            {videoURL && (
                <div className="playback">
                <video src={videoURL} className="video-playback" controls />
                <button className="button submit" onClick={handleSubmit}>Submit Video</button>
                </div>
            )}
        </div>
    </div>
    
  );
}

export default VideoRecorder;
