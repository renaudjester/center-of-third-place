from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self, host: str, port: int, database: str) -> None:
        self.client = MongoClient(host, port)
        self.database = self.client[database]


class MongoDB:
    def __init__(self, mongodb_connection: MongoDBConnection):
        self.connection = mongodb_connection

    def _insert_data(self, collection_name: str, data: dict) -> None:
        collection = self.connection.database[collection_name]
        collection.insert_one(data)

    def _query_data(self, collection_name: str) -> list[dict]:
        collection = self.connection.database[collection_name]
        return [self._convert_id(elmt) for elmt in collection.find()]  # type: ignore

    def _convert_id(self, data: dict) -> dict:
        if "_id" in data:
            data["_id"] = str(data["_id"])
        return data

    def insert_participant(self, data: dict) -> None:
        self._insert_data("participants", data)

    def query_participants(self) -> list[dict]:
        return self._query_data("participants")

    def insert_place(self, data: dict) -> None:
        self._insert_data("places", data)

    def query_places(self) -> list[dict]:
        return self._query_data("places")

    def close(self):
        self.connection.client.close()
