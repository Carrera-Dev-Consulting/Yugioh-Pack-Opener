import { render, screen } from '@testing-library/react';
import { Yugioh } from './yugioh';
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
      <Yugioh services={bootstrapMocks()} />
  );
  const title = screen.getByText(/(?:Yugioh)$/i);
  expect(title).toBeInTheDocument();
});
