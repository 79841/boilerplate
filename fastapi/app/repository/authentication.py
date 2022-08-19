from fastapi import Depends, status, HTTPException, Response
import schemas, database, models, getToken
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.responses import  JSONResponse


def signin(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = getToken.create_access_token(
        data={"id": user.id, "username": user.username})

    response = JSONResponse(content={"msg":"Login success"}, status_code=200)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        
    )
    return response


def logout(response:Response):
    response.delete_cookie("Authorization")
    return response
