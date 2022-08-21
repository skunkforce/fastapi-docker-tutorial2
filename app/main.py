from fastapi import FastAPI, File, UploadFile
import shutil


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open ("temporary.txt", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open("temporary.txt", "r") as file:
        data = file.read()
    
    return {"Content": f"{data}"}

