import React, { PropsWithChildren } from "react"

type LayoutProps = {
    title: string
} & PropsWithChildren

export const Layout: React.FC<LayoutProps> = (props: LayoutProps) => {
    return (<div>
        <h1>
            {props.title}
        </h1>
        <div>
            {props.children}
        </div>
    </div>)
}

export default Layout;