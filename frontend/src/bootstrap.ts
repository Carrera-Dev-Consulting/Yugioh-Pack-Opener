import { YugiohService, MockYugiohService } from "./services/yugiohService"

export type DefinedServices = {
    yugioh_service: YugiohService
}

export default function bootstrapServices(): DefinedServices {
    return {
        yugioh_service: new MockYugiohService()
    }
}