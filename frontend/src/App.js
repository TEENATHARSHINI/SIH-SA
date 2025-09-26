import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Moderation from './pages/Moderation';
import Export from './pages/Export';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/moderation" element={<Moderation />} />
        <Route path="/export" element={<Export />} />
      </Routes>
    </Router>
  );
}

export default App;
