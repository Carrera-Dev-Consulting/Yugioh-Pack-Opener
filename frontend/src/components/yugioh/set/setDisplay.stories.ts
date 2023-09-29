import type { Meta, StoryObj } from '@storybook/react';

import { YugiohSetDisplay } from './setDisplay';
import YugiohSet from '../../../models/yugioh/YugiohSet';

const meta = {
    title: 'Yugioh/SetDisplay',
    component: YugiohSetDisplay,
    tags: ['Yugioh'],
    argTypes: {
        set: {} as YugiohSet,
    },
} satisfies Meta<typeof YugiohSetDisplay>;

export default meta;

type Story = StoryObj<typeof meta>;

export const SetWithoutImage: Story = {
    args: {
        set: {
            id: 'setWithImage',
            name: 'set without image',
            cards: [],
            setImage: ''
        } as YugiohSet,
    },
};

export const SetWithImage: Story = {
    args: {
        set: {
            id: 'setWithImage',
            name: 'set with image',
            cards: [],
            setImage: 'https://cdn-icons-png.flaticon.com/512/6051/6051493.png'
        } as YugiohSet,
    },
};