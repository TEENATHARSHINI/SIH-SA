import React, { useEffect, useState } from 'react';
import { Paper, Typography } from '@mui/material';
import { Radar } from 'react-chartjs-2';
import axios from 'axios';

function AspectChart() {
  const [aspects, setAspects] = useState([]);

  useEffect(() => {
    axios.get('/api/v1/analysis/aspects')
      .then(res => setAspects(res.data))
      .catch(() => setAspects([
        { aspect: 'Tax Relief', positive: 60, neutral: 30, negative: 10 },
        { aspect: 'Compliance Burden', positive: 20, neutral: 40, negative: 40 },
        { aspect: 'Digital Filing', positive: 50, neutral: 30, negative: 20 },
      ]));
  }, []);

  const chartData = {
    labels: aspects.map(a => a.aspect),
    datasets: [
      {
        label: 'Positive',
        data: aspects.map(a => a.positive),
        backgroundColor: 'rgba(67,160,71,0.2)',
        borderColor: '#43a047',
      },
      {
        label: 'Neutral',
        data: aspects.map(a => a.neutral),
        backgroundColor: 'rgba(117,117,117,0.2)',
        borderColor: '#757575',
      },
      {
        label: 'Negative',
        data: aspects.map(a => a.negative),
        backgroundColor: 'rgba(229,57,53,0.2)',
        borderColor: '#e53935',
      },
    ],
  };

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Aspect-Based Sentiment</Typography>
      <Radar data={chartData} />
    </Paper>
  );
}

export default AspectChart;
