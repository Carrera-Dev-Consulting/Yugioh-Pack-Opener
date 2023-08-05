import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/Yugioh Card Puller/i);
  expect(linkElement).toBeInTheDocument();
});
