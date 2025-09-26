import React, { useEffect, useState } from 'react';
import { Paper, Typography } from '@mui/material';
import { AgGridReact } from 'ag-grid-react';
import axios from 'axios';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

function CommentExplorer() {
  const [rowData, setRowData] = useState([]);

  useEffect(() => {
    axios.get('/api/v1/comments/list')
      .then(res => setRowData(res.data))
      .catch(() => setRowData([
        {
          id: 1,
          text: 'This draft is not good at all',
          language: 'en',
          sentiment: 'negative',
          confidence: 0.55,
          highlights: ['not good'],
        },
      ]));
  }, []);

  const columns = [
    { headerName: 'Comment', field: 'text', flex: 2 },
    { headerName: 'Language', field: 'language', flex: 1 },
    { headerName: 'Sentiment', field: 'sentiment', flex: 1, cellStyle: params => {
      if (params.value === 'positive') return { color: '#43a047', fontWeight: 'bold' };
      if (params.value === 'negative') return { color: '#e53935', fontWeight: 'bold' };
      return { color: '#757575', fontWeight: 'bold' };
    } },
    { headerName: 'Confidence', field: 'confidence', flex: 1 },
    { headerName: 'Highlights', field: 'highlights', flex: 2, cellRenderer: params => params.value?.join(', ') },
  ];

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Comment Explorer</Typography>
      <div className="ag-theme-alpine" style={{ height: 320, width: '100%' }}>
        <AgGridReact rowData={rowData} columnDefs={columns} pagination={true} />
      </div>
    </Paper>
  );
}

export default CommentExplorer;
