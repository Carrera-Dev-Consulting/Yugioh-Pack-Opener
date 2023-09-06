import { render, screen } from '@testing-library/react';
import { YugiohSetPicker } from './setPicker';
import YugiohSet from '../../../models/yugioh/YugiohSet';


const mockedValue = {
    sets: [] as YugiohSet[], error: false
}

jest.mock('./SetDisplay', () => ({ YugiohSetDisplay: () => <div data-testid="yugioh-set-display" /> }));

jest.mock('./hooks/setHook', () => ({
    useSets: () => {
        return mockedValue
    }
}));

test('render yugioh set picker on screen', () => {
    mockedValue.sets = [
        {
            id: 'singleSet',
            name: 'Single Set',
            cards: [],
            setImage: 'https://cdn-icons-png.flaticon.com/512/6051/6051493.png',
        }
    ]
    mockedValue.error = false
    render(
        <YugiohSetPicker />
    );
    const setPicker = screen.getByText(/Pick A Set!/i);
    expect(setPicker).toBeInTheDocument();
});

test('render yugioh set picker with single set', async () => {
    mockedValue.sets = [
        {
            id: 'singleSet',
            name: 'Single Set',
            cards: [],
            setImage: 'https://cdn-icons-png.flaticon.com/512/6051/6051493.png',
        }
    ]
    mockedValue.error = false

    render(
        <YugiohSetPicker />
    );
    const setDisplay = screen.getByTestId(/yugioh-set-display/);
    expect(setDisplay).toBeInTheDocument();
});