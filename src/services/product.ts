import { productApi } from './api';

export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  category_id: number;
  stock: number;
  created_at: string;
  updated_at: string;
}

export interface Category {
  id: number;
  name: string;
  description: string;
  created_at: string;
  updated_at: string;
}

export const productService = {
  async getProducts(): Promise<Product[]> {
    const response = await productApi.get<Product[]>('/products');
    return response.data;
  },

  async getProduct(id: number): Promise<Product> {
    const response = await productApi.get<Product>(`/products/${id}`);
    return response.data;
  },

  async getCategories(): Promise<Category[]> {
    const response = await productApi.get<Category[]>('/categories');
    return response.data;
  },

  async getCategory(id: number): Promise<Category> {
    const response = await productApi.get<Category>(`/categories/${id}`);
    return response.data;
  },
}; 