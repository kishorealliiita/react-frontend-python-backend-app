import React, { useEffect } from 'react';
import { Container, Typography, Grid, Box } from '@mui/material';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { fetchProducts } from '../store/slices/productSlice';
import ProductCard from '../components/ProductCard';

const Home: React.FC = () => {
  const dispatch = useDispatch();
  const { products, loading } = useSelector((state: RootState) => state.products);

  useEffect(() => {
    dispatch(fetchProducts());
  }, [dispatch]);

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Welcome to Our E-Commerce Store
        </Typography>
        <Typography variant="h5" component="h2" gutterBottom color="text.secondary">
          Discover amazing products at great prices
        </Typography>
      </Box>

      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h2" gutterBottom>
          Featured Products
        </Typography>
        <Grid container spacing={3}>
          {loading ? (
            <Grid item xs={12}>
              <Typography>Loading...</Typography>
            </Grid>
          ) : (
            products.slice(0, 4).map((product) => (
              <Grid item xs={12} sm={6} md={3} key={product.id}>
                <ProductCard product={product} />
              </Grid>
            ))
          )}
        </Grid>
      </Box>
    </Container>
  );
};

export default Home; 