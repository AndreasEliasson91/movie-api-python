from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator

from typing import Optional, List
from typing_extensions import Annotated


PyObjectId: Annotated = Annotated[str, BeforeValidator(str)]


class Legend(BaseModel):
    '''Single Urban Legend Container'''
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    title: str = Field( ... )
    url: str = Field( ... )
    rating: str = Field( ... )
    subtitle: str = Field( ... )
    author: str = Field( ... )
    published: str = Field( ... )
    claim: str = Field( ... )


class LegendCollection(BaseModel):
    '''
    Container for a list of Legend instances
    
    This exists because providing a top-level array in a JSON response can be a vulnerability
    '''
    legends: List[Legend]
