import React from "react";

import YugiohSet from "../../../models/yugioh/YugiohSet"

type setImageProps = {
    set: YugiohSet,
};


export const YugiohSetImage: React.FC<setImageProps> = (props: setImageProps) => {
    return <div>
        <img
            className="yugioh-set-picker-img yugio-set-picker-child"
            alt={props.set.name + " set image"}
            src={props.set.setImage}
        />
        <div className="set-img-desc">
            <p>{props.set.name}</p>
        </div>
    </div>
}