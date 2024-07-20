from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app2 = FastAPI()

# Allow CORS
app2.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app2.get("/app2/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


def custom_openapi():
    if app2.openapi_schema:
        return app2.openapi_schema
    openapi_schema = get_openapi(
        title="Microservice 2",
        version="1.0.0",
        description="This is a custom OpenAPI schema for Microservice 2",
        routes=app2.routes,
    )
    openapi_schema["openapi"] = "3.0.0"
    app2.openapi_schema = openapi_schema
    return app2.openapi_schema


app2.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app2, host="127.0.0.1", port=8002)
