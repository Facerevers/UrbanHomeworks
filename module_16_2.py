from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter the user id")]
):
    return {"message": f"Вы вошли как пользователь №{user_id}"}


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Query(min_length=5, max_length=20, description="Enter username")],
                        age: Annotated[int, Query(ge=18, le=120, description="Enter age")]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}