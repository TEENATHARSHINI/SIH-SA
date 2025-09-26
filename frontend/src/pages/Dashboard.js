import React from 'react';
import { Box, Typography, Grid } from '@mui/material';
import SummaryStats from '../components/SummaryStats';
import SentimentChart from '../components/SentimentChart';
import TimelineChart from '../components/TimelineChart';
import WordCloudComponent from '../components/WordCloud';
import AspectChart from '../components/AspectChart';
import CommentExplorer from '../components/CommentExplorer';
import LanguageMonitor from '../components/LanguageMonitor';

function Dashboard() {
  return (
    <Box sx={{ p: 3, background: '#fff', minHeight: '100vh' }}>
      <Typography variant="h4" color="#003366" gutterBottom>Policy Feedback Dashboard</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <SummaryStats />
        </Grid>
        <Grid item xs={12} md={4}>
          <SentimentChart />
        </Grid>
        <Grid item xs={12} md={4}>
          <TimelineChart />
        </Grid>
        <Grid item xs={12} md={6}>
          <WordCloudComponent />
        </Grid>
        <Grid item xs={12} md={6}>
          <AspectChart />
        </Grid>
        <Grid item xs={12} md={8}>
          <CommentExplorer />
        </Grid>
        <Grid item xs={12} md={4}>
          <LanguageMonitor />
        </Grid>
      </Grid>
    </Box>
  );
}

export default Dashboard;
