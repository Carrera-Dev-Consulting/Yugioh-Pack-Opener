import { render, screen } from '@testing-library/react';
import { Home } from './home';
import { DefinedServices } from '../bootstrap';
import { YugiohService } from '../services/yugiohService';
import { mock } from 'jest-mock-extended';

const bootstrapMocks = (): DefinedServices => {
  return {
    yugioh_service: mock<YugiohService>()
  }
}

test('renders Appname in to page', async () => {
  render(
      <Home services={bootstrapMocks()} />
  );
  const title = screen.getByText(/Home/i);
  expect(title).toBeInTheDocument();
});
