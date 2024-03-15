from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse

import auth


router = APIRouter()


@router.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@router.post("/users/{username}/register/")
def register(username: str, password: str):
    try:
        return auth.register_user(username, password)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/users/{username}/delete")
def delete(username: str):
    auth.delete_user(username)


@router.post("/users/{username}/login")
def login(username: str, password: str):
    try:
        return auth.login_password(username, password)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sessions/{session}/login")
def login_session(session: str):
    try:
        return auth.login_session(session)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/sessions/{session}/logout")
def logout_session(session: str):
    auth.logout_session(session)
