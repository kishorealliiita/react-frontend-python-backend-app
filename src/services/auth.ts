import { userApi } from './api';

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  password: string;
  full_name: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export const authService = {
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await userApi.post<AuthResponse>('/auth/login', credentials);
    localStorage.setItem('token', response.data.access_token);
    return response.data;
  },

  async register(data: RegisterData): Promise<AuthResponse> {
    const response = await userApi.post<AuthResponse>('/auth/register', data);
    localStorage.setItem('token', response.data.access_token);
    return response.data;
  },

  logout(): void {
    localStorage.removeItem('token');
  },

  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  },
}; 