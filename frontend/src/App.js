import React from 'react';
import { Routes, Route } from 'react-router-dom';
import QuestionInput from './Components/InterviewApp/Question';
import InterviewApp from './Components/InterviewApp/InterviewApp';
import CompanyInput from './Components/InterviewApp/Company';
import RoleInput from './Components/InterviewApp/Role';
import Feedback from './Components/InterviewApp/Feedback';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<RoleInput />} />
        <Route path="/InterviewApp" element={<InterviewApp />} />
        <Route path="/Company" element={<CompanyInput />} />
        <Route path="/Question" element={<QuestionInput />} />
        <Route path="/Role" element={<RoleInput />} />
        <Route path="/Feedback" element={<Feedback />} />
      </Routes>
    </div>
  );
}

export default App;
