# import pytest
# import mongomock

# from mongoengine import connect, disconnect, get_connection
# from fastapi.testclient import TestClient
# from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

# from app.main import app
# # from app.db.connect import get_test_database


# @pytest.fixture
# def test_client(get_test_database, monkeypatch):
#     def override_get_db():
#         yield get_test_database

#     app.dependency_overrides[get_test_database] = override_get_db
#     yield TestClient(app)
#     app.dependency_overrides.clear()


# @pytest.fixture(scope="session", autouse=True)
# def get_test_database():
#     client = mongomock.MongoClient(connect=False)
#     db = client['UrbanLegendsDB']
#     collection = db['legends']

#     init_data = [
#         {'title': 'LEGEND01', 'rating': 'true', 'claim': 'This is the first legend'},
#         {'title': 'LEGEND02', 'rating': 'false', 'claim': 'This is the second legend'},
#         {'title': 'LEGEND03', 'rating': 'false', 'claim': 'This is the thir legend'},
#     ]

#     collection.insert_many(init_data)

#     return db

# @pytest.mark.asyncio
# async def test_get_random_id(test_client, get_test_database):
#     response = await test_client.get("/legends/random-id")
#     assert response.status_code == 200
#     assert isinstance(response.json(), str)

# @pytest.mark.asyncio
# async def test_get_legend_from_id(test_client, get_test_database):
#     # Insert a legend for testing
#     inserted_legend = {"title": "Test Legend", "rating": False, "claim": "This is a test."}
#     result = await get_test_database.legends.insert_one(inserted_legend)
#     legend_id = str(result.inserted_id)

#     # Test retrieving the inserted legend
#     response = await test_client.get(f"/legends/legend/{legend_id}")
#     assert response.status_code == 200
#     assert response.json() == inserted_legend

# @pytest.mark.asyncio
# async def test_get_all_legends(test_client, get_test_database):
#     # Insert multiple legends for testing
#     inserted_legends = [
#         {"title": "Legend 1", "rating": False, "claim": "This is legend 1."},
#         {"title": "Legend 2", "rating": True, "claim": "This is legend 2."},
#     ]

#     result = await get_test_database.legends.insert_many(inserted_legends)

#     # Test retrieving all legends
#     response = await test_client.get("/legends/")
#     assert response.status_code == 200
#     assert response.json()["legends"] == inserted_legends

# if __name__ == "__main__":
#     pytest.main([__file__])

import pytest
import random
from mongomock import MongoClient

@pytest.fixture
def test_db():
    client = MongoClient()
    db = client["UrbanLegendsDB"]
    collection = db["legends"]

    init_data = [
        {"_id": "1", "title": "Legend 1", "rating": False, "claim": "This is legend 1."},
        {"_id": "2", "title": "Legend 2", "rating": True, "claim": "This is legend 2."},
        # Add more initial data as needed
    ]

    # Insert initial data into the collection
    collection.insert_many(init_data)

    # Provide the test database to the test
    yield db

    # Clean up after the test by dropping the collection
    collection.drop()

# Your tests go here
def test_get_legend_from_id(test_db):
    legend = test_db.legends.find_one({'_id': '1'})
    assert legend["title"] == "Legend 1"

def test_get_random_id(test_db):
    random_id = random.choice(list(test_db.legends.find()))['_id']
    assert isinstance(random_id, str)

def test_get_all_legends(test_db):
    legends = list(test_db.legends.find())
    assert len(legends) == 2 