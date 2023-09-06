import { render, screen } from '@testing-library/react';
import { Yugioh } from './yugioh';
import { DefinedServices } from '../bootstrap';
import { YugiohService } from '../services/yugiohService';
import { mock } from 'jest-mock-extended';
import { YugiohSetPicker } from "../components/yugioh/set/setPicker";

const bootstrapMocks = (): DefinedServices => {
  return {
    yugioh_service: mock<YugiohService>()
  }
}

jest.mock('../components/yugioh/set/setPicker', () => ({YugiohSetPicker: () => <div data-testid="set-picker" />}))

test('renders Appname in to page', async () => {
  render(
      <Yugioh services={bootstrapMocks()} />
  );
  const title = screen.getByTestId(/set-picker/i);
  expect(title).toBeInTheDocument();
});
