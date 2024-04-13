import React from 'react';
import { Routes, Route } from 'react-router-dom';
import QuestionInput from './Components/InterviewApp/Question';
import InterviewApp from './Components/InterviewApp/InterviewApp'; // Import your InterviewApp component if it's not already imported

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<QuestionInput />} />
        <Route path="/InterviewApp" element={<InterviewApp />} />
      </Routes>
    </div>
  );
}

export default App;
