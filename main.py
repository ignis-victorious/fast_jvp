#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models import FoodEnum
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


# This is not needed at the moment

# def main():
#     print("Hello from fast-jvp!")


# if __name__ == "__main__":
#     main()
