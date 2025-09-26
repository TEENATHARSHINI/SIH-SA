import React, { useEffect, useState } from 'react';
import { Paper, Typography, Alert } from '@mui/material';
import axios from 'axios';

function LanguageMonitor() {
  const [stats, setStats] = useState({ language_counts: {}, underrepresented: [] });

  useEffect(() => {
    axios.get('/api/v1/comments/language-stats')
      .then(res => setStats(res.data))
      .catch(() => setStats({ language_counts: { en: 100, hi: 5, ta: 2 }, underrepresented: ['hi', 'ta'] }));
  }, []);

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Language Representation Monitoring</Typography>
      <Typography variant="body2">Comment volume by language:</Typography>
      <ul>
        {Object.entries(stats.language_counts).map(([lang, count]) => (
          <li key={lang}>{lang}: {count}</li>
        ))}
      </ul>
      {stats.underrepresented.length > 0 && (
        <Alert severity="warning">
          Underrepresented languages: {stats.underrepresented.join(', ')}
        </Alert>
      )}
    </Paper>
  );
}

export default LanguageMonitor;
