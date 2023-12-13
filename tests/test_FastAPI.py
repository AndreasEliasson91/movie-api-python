import pytest
import random
from mongomock import MongoClient

@pytest.fixture
def test_db():
    client = MongoClient()
    db = client['UrbanLegendsDB']
    collection = db['legends']

    init_data = [
        {
            '_id': '6569c205dc70e0fe6ce98f31',
            'title': 'Did American TV Viewers Hear the Devil\'s Voice on Aug. 29, 1968?', 
            'rating': 'false', 
            'claim': 'On August 29th, 1968, all the televisions in America were shut down. There was a murmuring on the TV that some believe was the devil\'s voice. The televisions were off for about 25 seconds. No one knows what the issue was and no one knows what the sound was from the TVs.'
        },
        {
            '_id': '6569c205dc70e0fe6ce98f32', 
            'title': 'Does This Video Show a "Jersey Devil" Perched in a Tree?', 
            'rating': 'false', 
            'claim': 'A video shows a real "Jersey Devil" cryptid perched in a tree..'
        },
        {
            '_id': '6569c205dc70e0fe6ce98f33', 
            'title': 'Did a Power Surge in a Plugged-In Air Fryer Cause a Fire, as Claimed in Viral Facebook Post?', 
            'rating': 'true', 
            'claim': 'A plugged-in air fryer underwent a power surge and caused a kitchen fire, despite the fact that it was plugged in to a special outlet for protection.'
        },
        {
            '_id': '6569c205dc70e0fe6ce98f34', 
            'title': 'No, This Is Not a "Human Skin Jacket" from Balenciaga', 
            'rating': 'false', 
            'claim': 'A viral photo emblazoned with fashion house Balenciaga\'s logo shows a "human skin jacket" made and sold by the company.'
        },
    ]

    collection.insert_many(init_data)

    yield db

    collection.drop()

def test_get_legend_from_id(test_db):
    legend = test_db.legends.find_one({'_id': '6569c205dc70e0fe6ce98f31'})
    assert legend['title'] == 'Did American TV Viewers Hear the Devil\'s Voice on Aug. 29, 1968?'

def test_get_random_id(test_db):
    random_id = random.choice(list(test_db.legends.find()))['_id']
    assert isinstance(random_id, str)

def test_get_all_legends(test_db):
    legends = list(test_db.legends.find())
    assert len(legends) == 4