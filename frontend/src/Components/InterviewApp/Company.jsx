import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Company.css';

function CompanyInput() {
  const [question, setQuestion] = useState('');
  const navigate = useNavigate();

  function handleSubmit() {
    if (!question) {
      alert('Please enter a company.');
      return;
    }
  
    fetch('http://localhost:4000/submit-company/', {
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
      navigate('/Question/');
    })
    .catch(error => {
      console.error('Error submitting company:', error);
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
        <h2 className="question-prompt">What company are you applying to?</h2>
        <div className="input-group">
          <input
            type="text"
            className="question-input"
            placeholder="Enter your company here"
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

export default CompanyInput;
