from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):
    username: str
    password: str
    balance: int


database_users = Dict[str, UserInDB]
database_users = {
    "tendero1": UserInDB(**{"username": "tendero1",
                            "password": "desten1app",
                            "balance": 3}),
    "tendero2": UserInDB(**{"username": "tendero2",
                            "password": "desten2app",
                            "balance": 4}),
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):  
    database_users[user_in_db.username] = user_in_db
    return user_in_db
