from pydantic import BaseModel

class Base(BaseModel):
    # Add whatever we need to format values correctly for json and ultimately for the api responses
    # i.e. if we need to normalize how datetime strings are made etc...
    pass