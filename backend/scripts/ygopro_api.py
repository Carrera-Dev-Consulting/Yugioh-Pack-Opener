import time
import json
import os 


from fastapi.encoders import jsonable_encoder
import requests
from pydantic import BaseModel


class YGOProSet(BaseModel):
    set_name: str
    set_code: str
    set_rarity: str
    set_rarity_code: str
    set_price: str
    
class YGOProCardImage(BaseModel):
    id: int
    image_url: str
    image_url_small: str
    image_url_cropped: str
    
    
class YGOProCardPrice(BaseModel):
    cardmarket_price: str | None
    tcgplayer_price: str | None
    ebay_price: str | None
    amazon_price: str | None
    coolstuffinc_price: str | None


class YGOProCard(BaseModel):
    id: int
    name: str
    type: str
    frameType: str
    desc: str 
    race: str | None = None
    archetype: str | None = None
    card_sets: list[YGOProSet] = []
    card_images: list[YGOProCardImage] = []
    card_prices: list[YGOProCardPrice] = []

class YGOProAPIHandler:
    def __init__(self, cached_card_file: str = 'cards.json') -> None:
        self.requests_made = 0
        self.cached_card_file = cached_card_file
        
    def _make_request(self, path: str, **kwargs):
        if self.requests_made < 4:
            response = requests.get(path, **kwargs)
            self.requests_made += 1
            return response
        else:
            print('Sleeping for a bit to not overload YGOPro API')
            time.sleep(1.1)
            self.requests_made = 0
            return self._make_request(path, **kwargs)
    
    def _request_stream_to_file(self, url, localpath):
        if not url:
            return
        
        if os.path.exists(localpath):
            return
        
        with self._make_request(url, stream=True) as response:
            with open(localpath, 'wb') as fp:
                for chunk in response.iter_content(255):
                    fp.write(chunk)
        
    
    def get_cards(self):
        if os.path.exists(self.cached_card_file):
            with open(self.cached_card_file, 'r') as fp:
                return [YGOProCard.model_validate(record) for record in json.load(fp)]
        
        cards = self._get_cards_from_api()
        
        with open(self.cached_card_file, 'w') as fp:
            json.dump(jsonable_encoder(cards), fp)
            
        return cards
    
    def _get_cards_from_api(self):
        response = self._make_request('https://db.ygoprodeck.com/api/v7/cardinfo.php')
        value = response.json()
        data = value['data']
        return [YGOProCard.model_validate(record) for record in data]
    
    def save_card_images(self, card: YGOProCard, directory: str):
        for image in card.card_images:
            self._request_stream_to_file(image.image_url, f'{directory}/{card.id}.jpg')
            self._request_stream_to_file(image.image_url_cropped, f'{directory}/{card.id}-cropped.jpg')
            self._request_stream_to_file(image.image_url_small, f'{directory}/{card.id}-small.jpg')
