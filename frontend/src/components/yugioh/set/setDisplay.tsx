import React from "react"
import './setDisplay.css';
// import Layout from "../../../components/layout"

import YugiohSet from "../../../models/yugioh/YugiohSet"

type setDisplayProps = {
    set: YugiohSet,
}


export const YugiohSetDisplay: React.FC<setDisplayProps> = (props: setDisplayProps) => {
    if (props.set.setImage)
        return <div className="yugioh-set-picker">
                <img
                    className="yugioh-set-picker-img yugio-set-picker-child"
                    alt={props.set.name}
                    src={props.set.setImage}
                />
                <div className="set-img-desc yugio-set-picker-child">
                    <p>{props.set.name}</p>
                </div>
            </div>
    else
        return <div className="yugioh-set-picker">
                <p className="yugioh-set-picker-no-img">No set image to display for {props.set.name}</p>
                {/* add blank square here */}
            </div>
}

