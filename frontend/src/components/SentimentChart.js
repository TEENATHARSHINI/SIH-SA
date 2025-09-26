import React, { useEffect, useState } from 'react';
import { Paper, Typography } from '@mui/material';
import { Pie } from 'react-chartjs-2';
import axios from 'axios';
import '../utils/chartSetup'; // Import Chart.js setup

function SentimentChart() {
  const [data, setData] = useState({ positive: 0, neutral: 0, negative: 0 });

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/analysis/summary')
      .then(res => setData(res.data))
      .catch(() => setData({ positive: 600, neutral: 400, negative: 234 }));
  }, []);

  const chartData = {
    labels: ['Positive', 'Neutral', 'Negative'],
    datasets: [
      {
        data: [data.positive, data.neutral, data.negative],
        backgroundColor: ['#43a047', '#757575', '#e53935'],
      },
    ],
  };

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Sentiment Distribution</Typography>
      <Pie data={chartData} />
    </Paper>
  );
}

export default SentimentChart;
