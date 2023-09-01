import React, { PropsWithChildren } from "react"

type LayoutProps = {
    title: string
} & PropsWithChildren

export const Layout: React.FC<LayoutProps> = (props: LayoutProps) => {
    return (<div>
        <h2>
            {props.title}
        </h2>
        <div>
            {props.children}
        </div>
    </div>)
}

export default Layout;