import React from 'react';
import { Box, Typography, Paper, Button } from '@mui/material';
// TODO: Connect to backend moderation endpoints

function Moderation() {
  return (
    <Box sx={{ p: 3, background: '#fff', minHeight: '100vh' }}>
      <Typography variant="h4" color="#003366" gutterBottom>Moderation Panel</Typography>
      <Paper sx={{ p: 2, mb: 2 }}>
        <Typography variant="h6">Flagged Comments for Review</Typography>
        {/* TODO: List flagged comments, approve/override actions */}
        <Box>[Flagged Comments Table]</Box>
      </Paper>
      <Button variant="contained" color="primary" sx={{ background: '#003366' }}>
        Refresh
      </Button>
    </Box>
  );
}

export default Moderation;
