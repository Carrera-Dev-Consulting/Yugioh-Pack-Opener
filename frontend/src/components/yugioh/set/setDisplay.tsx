import React from "react"
import './setDisplay.css';

import YugiohSet from "../../../models/yugioh/YugiohSet"

type setDisplayProps = {
    set: YugiohSet,
}


export const YugiohSetDisplay: React.FC<setDisplayProps> = (props: setDisplayProps) => {
    const [count, setCount] = React.useState<number>(0);

    return <div className="yugioh-set-picker"
            >
                <div onClick={() => setCount(count + 1)}>
                    <img
                        className="yugioh-set-picker-img yugio-set-picker-child"
                        alt={props.set.name + " set image"}
                        src={props.set.setImage}
                    />
                    <div className="set-img-desc">
                        <p>{props.set.name}</p>
                    </div>
                    {count > 0 && <p className="set-selected-count">{count}</p>}
                </div>
                {count > 0 && <p
                    className="set-decrement-count"
                    onClick={() => setCount((count || 1) - 1)}
                    >
                        X
                    </p>}
        </div>
}

