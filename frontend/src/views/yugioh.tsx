import React from "react"
import Layout from "../components/layout"
import { ViewProps } from "./base"

import { YugiohSetPicker } from "../components/yugioh/set/setPicker";

type YugiohPageProps = {
} & ViewProps



export const Yugioh: React.FC<YugiohPageProps> = (props: YugiohPageProps) => {
    return <Layout title="Yugioh">
        <div>
            <p>Yugioh Home Page</p>
            <YugiohSetPicker />
        </div>
    </Layout>
}