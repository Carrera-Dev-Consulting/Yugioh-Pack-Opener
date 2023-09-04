import React from "react";
import { Spinner } from './spinner';
import { ErrorSpinner } from './errorSpinner';

type SpinnerProps = {
    background: string,
    size: number,
}

export const BaseSpinner: React.FC<SpinnerProps> = (props: SpinnerProps) => {
    if (!props.background.match(/#[0-9A-Fa-f]{6}/))
        return (
            <ErrorSpinner message='Background property needs to be a hex value' />
        )
    else if (props.size <= 0)
        return (
            <ErrorSpinner message='Size property needs to be greater than 0' />
        )
    return(
        <Spinner background={props.background} size={props.size} />
    )
}