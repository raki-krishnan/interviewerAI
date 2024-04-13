import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate instead of useHistory
import './Question.css';

function QuestionInput() {
  const [question, setQuestion] = useState('');
  const navigate = useNavigate();

  const handleSubmit = () => {
    // You can send the question to your backend here
    navigate('/InterviewApp');
  };

  return (
    <div className="question-container">
      <h2 className="question-prompt">What question are you going to answer today?</h2>
      <input
        type="text"
        className="question-input"
        placeholder="Enter your question here"
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={handleSubmit} className="submit-button">Submit</button>
    </div>
  );
}

export default QuestionInput;
