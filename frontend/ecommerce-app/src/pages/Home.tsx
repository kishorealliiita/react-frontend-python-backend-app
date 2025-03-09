import React from 'react';
import { Container, Typography, Grid, Box } from '@mui/material';
import { useSelector } from 'react-redux';
import { RootState } from '../store';
import ProductCard from '../components/ProductCard';

const Home: React.FC = () => {
  const { products, loading } = useSelector((state: RootState) => state.products);

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Welcome to Our E-Commerce Store
        </Typography>
        <Typography variant="h5" component="h2" gutterBottom color="text.secondary">
          Featured Products
        </Typography>
        {loading ? (
          <Typography>Loading...</Typography>
        ) : (
          <Grid container spacing={4}>
            {products.slice(0, 4).map((product) => (
              <Grid item key={product.id} xs={12} sm={6} md={3}>
                <ProductCard product={product} />
              </Grid>
            ))}
          </Grid>
        )}
      </Box>
    </Container>
  );
};

export default Home; 