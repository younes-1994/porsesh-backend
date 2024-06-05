"""Handling route"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from src.util.db_dependency import get_db
from src.routes.auth import controller as authController
from src.routes.auth import schemas as authSchemas
from . import controller as formsController
from .schemas import Form as FormSchemas

router = APIRouter(
    prefix="/api/v1/forms",
    tags=["Forms"],
    responses={404: {"description": "Not found"}},
)


# ---------------------------
# ----- Crud-Operations -----
# ---------------------------
# @router.get("/all")
@router.post("/all/csv")
async def get_all_forms_csv(login: authSchemas.Login, db: Session = Depends(get_db)):
    """
    # Get a list of all forms as csv
    """
    authController.authenticate_user(login)
    csv_file = formsController.get_all_forms_csv(db=db)
    
    # Create a StreamingResponse for the CSV file
    response = StreamingResponse(csv_file, media_type="text/csv; charset=utf-8")
    response.headers["Content-Disposition"] = "attachment; filename=forms.csv"
    
    return response

@router.post("/create")
def create_form(form: FormSchemas, db: Session = Depends(get_db)):
    """
    # create a form
    """
    form_data = {}
    for item in form.items:
        form_data[item.name.replace('-', '_')] = item.value
    return formsController.create_form(db=db, form=form_data)
