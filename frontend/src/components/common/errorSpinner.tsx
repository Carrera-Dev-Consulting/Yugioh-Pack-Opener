import './spinner.css';

type ErrorSpinnerProps = {
    message: string
}

export const ErrorSpinner: React.FC<ErrorSpinnerProps> = (props: ErrorSpinnerProps) => {
    return (
        <div className='error-spinner'>
            <p>{ props.message }</p>
        </div>
    )
}