import type { Meta, StoryObj } from '@storybook/react';

import { Spinner } from './spinner';

const meta = {
    title: 'Common/Spinner',
    component: Spinner,
    tags: [],
    argTypes: {
        background: String,
        size: Number
    },
} satisfies Meta<typeof Spinner>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
    args: {
        background: '#000000',
        size: 64
    },
};