type YugiohSetInfo = {
    set_id: string,
    rarity: string,
    rarity_code: string,
    price: string,
};

type YugiohCard = {
    id: string,
    name: string,
    type: string,
    description: string,
    archetype: string | null,
    race: string | null,
    sets: Array<YugiohSetInfo>
};

export default YugiohCard;