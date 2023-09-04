import './spinner.css';

type SpinnerProps = {
    background: string,
    size: number,
}

export const Spinner: React.FC<SpinnerProps> = (props: SpinnerProps) => {
    return(
        <div className="loading-circle"
            style={{
                background: props.background,
                height: props.size,
                width: props.size,
            }}
        />
    )
}