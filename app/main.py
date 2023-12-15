import os

from bson import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.db.model import Legend, LegendCollection
from app.db.connect import get_database

if os.environ['ENVIRONMENT'] == 'development':
    load_dotenv()


app = FastAPI(
    title='Urban Legends API',
    summary='FastAPI connected to MongoDb collection'
)


db = get_database()
collection = db.legends


@app.get(
    '/legends/legend/{id}',
    response_description='Get a single legend from ID',
    response_model=Legend,
    response_model_by_alias=False
)
async def get_legend_from_id(id: str):
    '''
    Get the document of a single urban legend by id
    '''
    if (legend := await collection.find_one({'_id': ObjectId(id)})) is not None:
        return legend
    
    raise HTTPException(status_code=404, detail=f'Legend with id: {id} not found')

@app.get(
        '/legends/random-id',
        response_description='Get a random ID',
        response_model=str,
        response_model_by_alias=False
)
async def get_random_id():
    '''
    Get a random legend ID to use for accessing a random legend in the UI
    '''
    import random
    return random.choice([str(legend['_id']) for legend in await collection.find().to_list(500)])


@app.get(
    '/legends/',
    response_description='List all legends',
    response_model=LegendCollection,
    response_model_by_alias=False
)
async def get_all_legends():
    '''
    List all urban legends in the database
    Max limit for responses is set to 500
    '''
    return LegendCollection(legends=await collection.find().to_list(500))

