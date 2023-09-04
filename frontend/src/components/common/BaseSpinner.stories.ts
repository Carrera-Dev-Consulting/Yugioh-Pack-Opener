import type { Meta, StoryObj } from '@storybook/react';

import { BaseSpinner } from './BaseSpinner';

const meta = {
    title: 'BaseSpinner',
    component: BaseSpinner,
    tags: [],
    argTypes: {
        background: String,
        size: Number
    },
} satisfies Meta<typeof BaseSpinner>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
    args: {
        background: '#000000',
        size: 64
    },
};

export const BadBackground: Story = {
    args: {
        background: '123',
        size: 64
    }
};

export const BadSize: Story = {
    args: {
        background: '#111111',
        size: 0
    }
};