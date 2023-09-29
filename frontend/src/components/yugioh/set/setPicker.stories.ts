import type { Meta, StoryObj } from '@storybook/react';

import { YugiohSetPicker } from './setPicker';

const meta: Meta = {
    title: 'Yugioh/SetPicker',
    component: YugiohSetPicker,
} satisfies Meta<typeof YugiohSetPicker>;
export default meta;

type Story = StoryObj<typeof meta>;

export const Primary: Story = {
    args: {}
};
