from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"email": "22f2001388@ds.study.iitm.ac.in", "message": "Deployed on Vercel"}
