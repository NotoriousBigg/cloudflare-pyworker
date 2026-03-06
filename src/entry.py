# from workers import Response, WorkerEntrypoint
# from submodule import get_hello_message
# class Default(WorkerEntrypoint):
#     async def fetch(self, request):
#         return Response(get_hello_message())


from fastapi import FastAPI
from workers import Response

app = FastAPI()

@app.get("/test")
async def get_user(user_id: int):
    return {"message": "Farming is better"}