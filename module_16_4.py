from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, conint, field_validator
from typing import List

app = FastAPI()

users: List['User '] = []


class User(BaseModel):
    id: int
    username: constr(min_length=5, max_length=20)
    age: conint(ge=18, le=100)

    @field_validator('Username')
    def validation_username(cls, v):
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric.")
        elif len(v) < 5 or len(v) > 20:
            raise ValueError("Username length must be between 5 and 20.")
        return v


@app.get("/users", responce_model=List[User ])
async def get_users():
    return users


@app.post("user/{username}/{age}", responce_model=User)
async def add_user(username: str, age: int):
    if age < 18 or age > 100:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 100.")

    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", responce_model=User)
async def update_user(user_id: int, username: str, age: int):
    # Проверка на валидность параметров
    if age < 18 or age > 100:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 100.")

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User  was not found")


@app.delete("/user/{user_id}", responce_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User  was not found")