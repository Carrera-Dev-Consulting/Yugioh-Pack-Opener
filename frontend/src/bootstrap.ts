import { YugiohAPIService, YugiohService, MockYugiohService } from "./services/yugiohService"

export type DefinedServices = {
    yugioh_service: YugiohService
}

export default function (): DefinedServices {
    return {
        yugioh_service: new MockYugiohService()
    }
}