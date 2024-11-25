from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get("", status_code=HTTPStatus.OK)
def hello_world():
    return {"message": "Hello, World!"}
