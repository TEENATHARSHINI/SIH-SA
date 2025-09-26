import React from 'react';
import { Box, Typography, Paper, Button } from '@mui/material';
// TODO: Connect to backend export endpoints

function Export() {
  return (
    <Box sx={{ p: 3, background: '#fff', minHeight: '100vh' }}>
      <Typography variant="h4" color="#003366" gutterBottom>Export Reports</Typography>
      <Paper sx={{ p: 2, mb: 2 }}>
        <Typography variant="h6">Download PDF/Excel Reports</Typography>
        {/* TODO: Export buttons, show watermark/timestamp/language */}
        <Button variant="contained" color="primary" sx={{ background: '#003366', mr: 2 }}>
          Export PDF
        </Button>
        <Button variant="contained" color="secondary" sx={{ background: '#1976d2' }}>
          Export Excel
        </Button>
      </Paper>
    </Box>
  );
}

export default Export;
