import React, { useState, useEffect } from 'react';
import './Feedback.css';

function Feedback() {
  const [feedback1, setFeedback1] = useState('');
  const [feedback2, setFeedback2] = useState('');
  const [isTyping1, setIsTyping1] = useState(false);
  const [isTyping2, setIsTyping2] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  const typeFeedback = (feedback, setFeedback, setIsTyping, callback) => {
    let index = 0;
    const intervalId = setInterval(() => {
      if (index < feedback.length) {
        setFeedback(prev => prev + feedback.charAt(index));
        index++;
      } else {
        clearInterval(intervalId);
        setIsTyping(false);
        if (callback) {
          callback();
        }
      }
    }, 50);
  };
  
  useEffect(() => {
    console.log("Fetching feedback...");
    // Set loading to true when the component mounts
    setIsLoading(true);
    // Fetch feedback when component mounts
    fetch('http://localhost:4000/get-feedback/')
      .then(response => response.json())
      .then(data => {
        console.log('Feedback received:', data);
        // Set loading to false when feedback is received
        setIsLoading(false);
        // Start typing effect after receiving the feedback
        setIsTyping1(true);
        typeFeedback(data.feedback1, setFeedback1, setIsTyping1, () => {
          setIsTyping2(true);
          typeFeedback(data.feedback2, setFeedback2, setIsTyping2);
        });
      })
      .catch(error => {
        console.error('Error fetching feedback:', error);
        setIsLoading(false); // Also set loading to false in case of error
      });
  }, []);

  return (
    <div className="feedback-container">
      <video controls src="/videos/converted_video.mov" alt="Interview video" className="feedback-video">
        Your browser does not support the video tag.
      </video>
      <div className="feedback-messages">
        {/* Conditionally render the loading message or feedback messages */}
        {isLoading ? (
          <p className="loading-message">Loading Response...</p>
        ) : (
          <>
            <p className={`typing-effect ${isTyping1 ? "typing" : ""}`}>{feedback1}</p>
            <p className={`typing-effect ${isTyping2 ? "typing" : ""}`}>{feedback2}</p>
          </>
        )}
      </div>
    </div>
  );
}

export default Feedback;