import React from "react"
// import Layout from "../../../components/layout"

import YugiohSet from "../../../models/yugioh/YugiohSet"

type setDisplayProps = {
    set: YugiohSet,
}


export const YugiohSetDisplay: React.FC<setDisplayProps> = (props: setDisplayProps) => {
    if (props.set.setImage)
        return <div>
                <img
                    className="yugioh-set-picker-img"
                    alt={props.set.name}
                    src={props.set.setImage}
                />
            </div>
    else
        return <div>
                <p>No set image to display for {props.set.name}</p>
                {/* add blank square here */}
            </div>
}

