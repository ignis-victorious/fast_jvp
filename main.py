#  ___________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI

#  Import FILES
from models import FoodEnum, Item
from items_db import fake_items_db
#  ___________________


app = FastAPI()


# Part 1


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "hello world"}


@app.post("/")
async def post() -> dict[str, str]:
    return {"message": "hello from the post route"}


@app.put("/")
async def put() -> dict[str, str]:
    return {"message": "hello from the put route"}


# Part 2


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


# Part 3


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


# Part 4


@app.post("/items")
async def create_item(item: Item) -> dict[str, Any]:
    item_dict: dict[str, Any] = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(
    item_id: int, item: Item, q: str | None = None
) -> dict[str, str | float]:
    result: dict[str, str | float] = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


# This is not needed at the moment

# def main():
#     print("Hello from fast-jvp!")


# if __name__ == "__main__":
#     main()
