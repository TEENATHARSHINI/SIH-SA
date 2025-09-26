import React, { useEffect, useRef } from 'react';
import { Paper, Typography } from '@mui/material';
import axios from 'axios';
import WordCloud from 'wordcloud';

function WordCloudComponent() {
  const canvasRef = useRef(null);

  useEffect(() => {
    axios.post('/api/v1/visualization/wordcloud/sentiment', {
      texts: [], // TODO: Provide comment texts
      analysis_results: [], // TODO: Provide sentiment results
      max_words: 100,
      width: 800,
      height: 400,
    })
      .then(res => {
        const words = Object.entries(res.data.word_data).map(([word, info]) => [word, info.count]);
        WordCloud(canvasRef.current, {
          list: words,
          gridSize: 8,
          weightFactor: 3,
          color: (word, weight) => {
            const info = res.data.word_data[word];
            if (info.sentiment === 'positive') return '#43a047';
            if (info.sentiment === 'negative') return '#e53935';
            return '#757575';
          },
          backgroundColor: '#fff',
        });
      });
  }, []);

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6">Word Cloud</Typography>
      <canvas ref={canvasRef} width={800} height={400} />
    </Paper>
  );
}

export default WordCloudComponent;
