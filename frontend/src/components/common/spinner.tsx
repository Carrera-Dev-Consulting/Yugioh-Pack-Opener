import './spinner.css';

type SpinnerProps = {
    // color for the circle as a hex value
    background: string,
    // size of spinner, this sets both height and width
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
        ></div>
    )
}