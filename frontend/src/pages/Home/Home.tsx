import React from 'react';
import { Typography, Box, Paper } from '@mui/material';

const Home: React.FC = () => {
  return (
    <Box>
      <Paper elevation={3} sx={{ p: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Welcome to My Web Application
        </Typography>
        <Typography variant="body1" paragraph>
          This is a modern web application built with React, TypeScript, and Material-UI.
          It provides a solid foundation for building scalable and maintainable applications.
        </Typography>
      </Paper>
      
      <Box sx={{ display: 'grid', gridTemplateColumns: { xs: '1fr', md: '1fr 1fr' }, gap: 4 }}>
        <Paper elevation={2} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Features
          </Typography>
          <Typography variant="body2" component="ul" sx={{ pl: 2 }}>
            <li>Modern React with TypeScript</li>
            <li>Material-UI components</li>
            <li>Responsive design</li>
            <li>Clean project structure</li>
          </Typography>
        </Paper>
        
        <Paper elevation={2} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Getting Started
          </Typography>
          <Typography variant="body2" paragraph>
            To start developing, you can:
          </Typography>
          <Typography variant="body2" component="ul" sx={{ pl: 2 }}>
            <li>Edit src/pages/Home/Home.tsx</li>
            <li>Add new components in src/components</li>
            <li>Create new pages in src/pages</li>
            <li>Add API calls in src/services</li>
          </Typography>
        </Paper>
      </Box>
    </Box>
  );
};

export default Home; 