import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Role.css';

function RoleInput() {
  const [question, setQuestion] = useState('');
  const navigate = useNavigate();

  function handleSubmit() {
    if (!question) {
      alert('Please enter a role.');
      return;
    }
  
    fetch('http://localhost:4000/submit-role/', {
      method: 'POST',
    //   mode: 'no-cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "question": question })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); // Parse JSON data from the response
    })
    .then(data => {
      console.log(data); // Handle the data from the response
      navigate('/Company/');
    })
    .catch(error => {
      console.error('Error submitting role:', error);
    });
  }

  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      handleSubmit(event);
    }
  }

  return (
    <div className="container">
      <div className="question-container">
        <h2 className="question-prompt">What role are you applying to?</h2>
        <div className="input-group">
          <input
            type="text"
            className="question-input"
            placeholder="Enter your question here"
            value={question}
            onChange={e => setQuestion(e.target.value)}
            onKeyDown={handleKeyPress}
          />
          <button onClick={handleSubmit} className="submit-button">Submit</button>
        </div>
      </div>
    </div>
  );
}

export default RoleInput;
