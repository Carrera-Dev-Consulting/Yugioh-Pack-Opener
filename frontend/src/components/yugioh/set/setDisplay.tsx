import React from "react"
import { YugiohSetImage } from './setImage';
import './setDisplay.css';

import YugiohSet from "../../../models/yugioh/YugiohSet"

type setDisplayProps = {
    set: YugiohSet,
}


export const YugiohSetDisplay: React.FC<setDisplayProps> = (props: setDisplayProps) => {
    const [count, setCount] = React.useState<number>(0);

    return <div className="yugioh-set-picker"
            >
                <div onClick={() => setCount(count + 1)} data-testid='clickable-div'>
                    <YugiohSetImage set={props.set}/>
                    {count > 0 && <p className="set-selected-count" data-testid="displayed-count">{count}</p>}
                </div>
                {count > 0 && <p
                    className="set-decrement-count"
                    onClick={() => setCount((count || 1) - 1)}
                    >
                        X
                    </p>}
        </div>
}

