from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app1 = FastAPI()

# Allow CORS
app1.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app1.get("/app1/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


def custom_openapi():
    if app1.openapi_schema:
        return app1.openapi_schema
    openapi_schema = get_openapi(
        title="Microservice 1",
        version="1.0.0",
        description="This is a custom OpenAPI schema for Microservice 1",
        routes=app1.routes,
    )
    openapi_schema["openapi"] = "3.0.0"
    app1.openapi_schema = openapi_schema
    return app1.openapi_schema


app1.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app1, host="127.0.0.1", port=8001)
