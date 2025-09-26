import React, { useEffect, useState } from 'react';
import { Paper, Typography } from '@mui/material';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

function TimelineChart() {
  const [timeline, setTimeline] = useState([]);

  useEffect(() => {
    axios.get('/api/v1/analysis/timeline')
      .then(res => setTimeline(res.data))
      .catch(() => setTimeline([
        { date: '2025-09-01', positive: 20, neutral: 10, negative: 5 },
        { date: '2025-09-02', positive: 30, neutral: 15, negative: 10 },
      ]));
  }, []);

  const chartData = {
    labels: timeline.map(t => t.date),
    datasets: [
      {
        label: 'Positive',
        data: timeline.map(t => t.positive),
        borderColor: '#43a047',
        fill: false,
      },
      {
        label: 'Neutral',
        data: timeline.map(t => t.neutral),
        borderColor: '#757575',
        fill: false,
      },
      {
        label: 'Negative',
        data: timeline.map(t => t.negative),
        borderColor: '#e53935',
        fill: false,
      },
    ],
  };

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Timeline</Typography>
      <Line data={chartData} />
    </Paper>
  );
}

export default TimelineChart;
