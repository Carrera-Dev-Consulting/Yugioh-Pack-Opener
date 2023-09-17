import yugiohFetcher from '../../../../fetchers/yugiohFetcher';

import YugiohSet from '../../../../models/yugioh/YugiohSet';
import useSWR from 'swr';

type SetHookResponse = {
    sets?: YugiohSet[]
    error: boolean
}

export const useSets = (): SetHookResponse  => {
    const { data, error } = useSWR('/sets', yugiohFetcher);
    return {sets: (data as YugiohSet[]), error}
}