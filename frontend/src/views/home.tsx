import React from "react"
import Layout from "../components/layout"
import { ViewProps } from "./base"

type HomePageProps = {
} & ViewProps



export const Home: React.FC<HomePageProps> = (props: HomePageProps) => {
    return <Layout title="Home">
        <div>
            <p>Will be something more later</p>
        </div>
    </Layout>
}