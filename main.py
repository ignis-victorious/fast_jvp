#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
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


# def main():
#     print("Hello from fast-jvp!")


# if __name__ == "__main__":
#     main()
