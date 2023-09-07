import { Axios } from "axios"
import PackRequest from "../models/yugioh/PackRequest"
import PackResponse from "../models/yugioh/PackResponse"
import YugiohSet from "../models/yugioh/YugiohSet"
import testSets from "./testSets"


export interface YugiohService {
    getSets(): Promise<YugiohSet[]>
    openPacks(request: PackRequest): Promise<PackResponse>
}


type Package<T> = {
    items: T[]
    totalPages: number
    page: number
}

type SetsResponse = Package<YugiohSet>



export class YugiohAPIService implements YugiohService {
    session: Axios

    constructor(session: Axios) {
        this.session = session
        // this.session.defaults.baseURL = '/api/v1' // update this whenever we need to switch api versions
    }

    async getSets(): Promise<YugiohSet[]> {
        // TODO: Add something to either go through the pagination or make it apart of the interface definition so we can render the page differently
        // TODO: Consider making a way to query sets down to filter results on the backend??
        return testSets;
        const response = await this.session.get<SetsResponse>('/sets')
        return response.data.items
    }

    async openPacks(request: PackRequest): Promise<PackResponse> {
        const response = await this.session.get<PackResponse>("/pack/open")
        return response.data
    }

}

export class MockYugiohService implements YugiohService {
    getSets(): Promise<YugiohSet[]> {
        return Promise.resolve([]);
    }
    openPacks(request: PackRequest): Promise<PackResponse> {
        return Promise.resolve({});
    }
}