import React from "react"
import Layout from "../../../components/layout"

type yugiohErrorProps = {
    status: number,
    message: string,
}

export const YugiohError: React.FC<yugiohErrorProps> = (props: yugiohErrorProps) => {
    return <Layout title="Error Occured">
        <div>
            <h3>{ props.status }</h3>
            <p>{ props.message }</p>
        </div>
    </Layout>
}