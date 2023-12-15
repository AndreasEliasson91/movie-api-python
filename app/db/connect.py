import os

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

def get_database() -> AsyncIOMotorDatabase:
    return AsyncIOMotorClient(os.environ['MONGODB_URL'])['UrbanLegendsDB']
