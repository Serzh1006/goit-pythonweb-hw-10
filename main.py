from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from src.databases.connect import get_db
from src.routes import contacts, auth

app = FastAPI()


@app.get("/", name="API root")
def get_index():
    return {"message": "Welcome to Contacts API."}


@app.get("/health", name="Service availability")
def get_health_status(db=Depends(get_db)):
    try:
        result = db.execute(text("Select 1+1")).fetchone()
        print(result)
        if result is None:
            raise Exception
        return {"message": "DataBase is ready for use!"}
    except:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="DataBase is not configure correctly ",
        )


app.include_router(contacts.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)