import React from "react"

import './setPicker.css';
import Layout from "../../../components/layout"
import { YugiohSetDisplay } from "./setDisplay";
import { BaseSpinner } from '../../common/BaseSpinner';
import { YugiohError } from '../common/yugiohError';
import { useSets } from "./hooks/setHook";


type setPickerProps = {
}


export const YugiohSetPicker: React.FC<setPickerProps> = (props: setPickerProps) => {
    
    const {sets, error} = useSets() 
    if (sets === undefined) return <BaseSpinner background="#ffffff" size={64}/>
    if (error) return <YugiohError status={400} message={'Failed to get sets'}/>
    
    return <Layout title="Pick A Set!">
        <div className="set-display-holder">
            {sets.map((set, i) => React.createElement(YugiohSetDisplay, { set, key: set.id }))}
        </div>
    </Layout>
}