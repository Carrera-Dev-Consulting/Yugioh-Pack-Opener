import axios from "axios";
import { YugiohAPIService } from "../services/yugiohService";

const yugiohService = new YugiohAPIService(axios.create({
    baseURL: '/api/v1',
}));


const yugiohFetcher = async (v: string) => {
    if (v === '/sets')
        return yugiohService.getSets();
};

export default yugiohFetcher;