from src.schemas.user import UserCreate, UserLogin
from src.databases.connect import get_db
from fastapi import Depends, HTTPException, APIRouter, status
from src.databases.models import User
from src.repository.users import create_user, authenticate_user
from src.auth.auth import create_access_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", status_code = status.HTTP_201_CREATED)
async def register(user: UserCreate, db = Depends(get_db)):
    existing = db.query(User).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    new_user = await create_user(user, db)
    token = await create_access_token({"sub": new_user.email})
    return {"Email": new_user.email, "access_token": token}


@router.post("/login", status_code = status.HTTP_200_OK)
async def login(user: UserLogin, db = Depends(get_db)):
    user_in_db = await authenticate_user(user.email, user.password, db)
    if not user_in_db:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED ,detail="Invalid authorization")
    token = await create_access_token({"sub": user_in_db.email})
    return {"access_token": token, "token_type": "bearer"}