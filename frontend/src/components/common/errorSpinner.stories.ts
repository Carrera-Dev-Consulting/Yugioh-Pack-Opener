import type { Meta, StoryObj } from '@storybook/react';

import { ErrorSpinner } from './errorSpinner';

const meta = {
    title: 'ErrorSpinner',
    component: ErrorSpinner,
    tags: [],
    argTypes: {
        message: String,
    },
} satisfies Meta<typeof ErrorSpinner>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
    args: {
        message: 'here is the message'
    },
};