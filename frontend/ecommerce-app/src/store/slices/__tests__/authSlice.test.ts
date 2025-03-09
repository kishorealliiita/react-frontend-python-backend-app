import authReducer, { login, logout } from '../authSlice';

interface AuthState {
  isAuthenticated: boolean;
  user: {
    id: string;
    email: string;
    fullName: string;
  } | null;
  token: string | null;
}

describe('authSlice', () => {
  const initialState: AuthState = {
    isAuthenticated: false,
    user: null,
    token: null,
  };

  it('should handle initial state', () => {
    expect(authReducer(undefined, { type: 'unknown' })).toEqual(initialState);
  });

  it('should handle login', () => {
    const mockUser = {
      id: '1',
      email: 'test@example.com',
      fullName: 'Test User',
    };
    const mockToken = 'mock-token';
    
    const actual = authReducer(initialState, login({ user: mockUser, token: mockToken }));
    
    expect(actual.isAuthenticated).toBe(true);
    expect(actual.user).toEqual(mockUser);
    expect(actual.token).toBe(mockToken);
  });

  it('should handle logout', () => {
    const loggedInState: AuthState = {
      isAuthenticated: true,
      user: {
        id: '1',
        email: 'test@example.com',
        fullName: 'Test User',
      },
      token: 'mock-token',
    };

    const actual = authReducer(loggedInState, logout());
    
    expect(actual).toEqual(initialState);
  });
}); 