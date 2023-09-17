import YugiohCard from "./YugiohCard";

type YugiohSet = {
    id: string,
    name: string,
    cards: Array<YugiohCard>,
    setImage: string | undefined,
};

export default YugiohSet;