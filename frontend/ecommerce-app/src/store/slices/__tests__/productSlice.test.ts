import productReducer, { setProducts, setCategories, setLoading, setError } from '../productSlice';
import { Product } from '../productSlice';

describe('productSlice', () => {
  const initialState = {
    products: [],
    categories: [],
    loading: false,
    error: null,
  };

  const mockProducts: Product[] = [
    {
      id: '1',
      name: 'Test Product 1',
      description: 'Test Description 1',
      price: 99.99,
      category: 'Electronics',
      image: 'test-image-1.jpg',
    },
    {
      id: '2',
      name: 'Test Product 2',
      description: 'Test Description 2',
      price: 149.99,
      category: 'Clothing',
      image: 'test-image-2.jpg',
    },
  ];

  const mockCategories = ['Electronics', 'Clothing', 'Books'];

  it('should handle initial state', () => {
    expect(productReducer(undefined, { type: 'unknown' })).toEqual(initialState);
  });

  it('should handle setProducts', () => {
    const actual = productReducer(initialState, setProducts(mockProducts));
    expect(actual.products).toEqual(mockProducts);
  });

  it('should handle setCategories', () => {
    const actual = productReducer(initialState, setCategories(mockCategories));
    expect(actual.categories).toEqual(mockCategories);
  });

  it('should handle setLoading', () => {
    const actual = productReducer(initialState, setLoading(true));
    expect(actual.loading).toBe(true);
  });

  it('should handle setError', () => {
    const errorMessage = 'Failed to fetch products';
    const actual = productReducer(initialState, setError(errorMessage));
    expect(actual.error).toBe(errorMessage);
  });
}); 