import { render, screen } from '@testing-library/react';
import App from './App';
import { DefinedServices } from './bootstrap';
import { YugiohService } from './services/yugiohService';
import { mock } from 'jest-mock-extended';

const bootstrapMocks = (): DefinedServices => {
  return {
    yugioh_service: mock<YugiohService>()
  }
}

test('renders Appname in to page', () => {
  render(<App services={bootstrapMocks()} />);
  const linkElement = screen.getByText(/Yugioh Card Puller/i);
  expect(linkElement).toBeInTheDocument();
});
