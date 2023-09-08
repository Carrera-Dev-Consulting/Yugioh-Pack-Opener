import { render, screen } from '@testing-library/react';
import { YugiohSetImage } from './setImage';

import YugiohSet from '../../../models/yugioh/YugiohSet';

test('render yugioh set image on screen with image', () => {
    const setWithImage = {
        id: 'yes-id',
        name: 'yes',
        cards: [],
        setImage: 'https://cdn-icons-png.flaticon.com/512/6051/6051493.png',
    } as YugiohSet;
    render(<YugiohSetImage set={setWithImage}/>);

    const image = screen.getByAltText(`${setWithImage.name} set image`);
    const setNameDisplay = screen.getByText(setWithImage.name);

    expect(image).toBeInTheDocument();
    expect(setNameDisplay).toBeInTheDocument();
});

test('render yugioh set image on screen without image', () => {
    const setWithoutImage = {
        id: 'setWithImage',
        name: 'set without image',
        cards: [],
        setImage: ''
    } as YugiohSet;
    render(
        <YugiohSetImage set={setWithoutImage}/>
    );
    const image = screen.getByAltText(`${setWithoutImage.name} set image`);
    const setNameDisplay = screen.getByText(setWithoutImage.name);

    expect(image).toBeInTheDocument();
    expect(setNameDisplay).toBeInTheDocument();
});