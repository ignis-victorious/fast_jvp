#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models import FoodEnum
from items_db import fake_items_db
#  ___________________


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "hello world"}


@app.post("/")
async def post() -> dict[str, str]:
    return {"message": "hello from the post route"}


@app.put("/")
async def put() -> dict[str, str]:
    return {"message": "hello from the put route"}


@app.get("/users")
async def list_users() -> dict[str, str]:
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user() -> dict[str, str]:
    return {"Message": "this is the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str) -> dict[str, str]:
    return {"user_id": user_id}


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum) -> dict[str, str]:
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }
    return {"food_name": food_name, "message": "i like chocolate milk"}


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def get_item(
    item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
) -> dict[str, str]:
    item: dict[str, str] = {
        "item_id": item_id,
        "sample_query_param": sample_query_param,
    }
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
            }
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
) -> dict[str, str | int] | None:
    item: dict[str, str | int] = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
            }
        )
        return item


# This is not needed at the moment

# def main():
#     print("Hello from fast-jvp!")


# if __name__ == "__main__":
#     main()
