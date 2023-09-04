import { render, screen } from '@testing-library/react';
import { BaseSpinner } from './BaseSpinner';

jest.mock('./spinner', () => ({Spinner: () => <div data-testid="spinner"/>}))
jest.mock('./errorSpinner', () => ({ErrorSpinner: () => <div data-testid="error-spinner"/>}))

test('render spinner on page with good props', () => {
    render(
        <BaseSpinner background='#ffffff' size={64} />
    );
    const spinner = screen.getByTestId(/spinner/);
    expect(spinner).toBeInTheDocument();
  });

test('render error spinner on page with bad background', () => {
    render (
        <BaseSpinner background='ffffff' size={64} />
    );
    const spinner = screen.getByTestId(/error-spinner/);
    expect(spinner).toBeInTheDocument();
});

test('render error spinner on page with bad size', () => {
    render (
        <BaseSpinner background='#ffffff' size={0} />
    );
    const spinner = screen.getByTestId(/error-spinner/);
    expect(spinner).toBeInTheDocument();
});

test('render error spinner on page with bad background & size', () => {
    render (
        <BaseSpinner background='ffffff' size={0} />
    );
    const spinner = screen.getByTestId(/error-spinner/);
    expect(spinner).toBeInTheDocument();
});