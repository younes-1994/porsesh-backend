"""Logic"""
import csv
from io import StringIO, BytesIO
from .models import Form as FormModel

def get_all_forms_csv(db):
    # Retrieve all records from the database
    forms = db.query(FormModel).all()

    # Create a CSV string buffer
    csv_file = StringIO()
    csv_writer = csv.writer(csv_file)
    
    # Write CSV header
    csv_writer.writerow([
        'id', 'کد', 'تاریخ', 'پرسشگر', 'دپارتمان', 
        'نام', 'کدملی', 'موبایل', 'تلفن', 'تاریخ تولد', 'سوال', 'سوال', 'سوال', 'مقدار', 'q10'
    ])
    
    # Write data rows
    for form in forms:
        csv_writer.writerow([
            form.id, form.code, form.date, form.questioner, form.department, 
            form.name, form.national_code, form.mobile, form.tel, 
            form.birth_date, form.q6, form.q7, form.q8, form.q9, form.q10
        ])
    
    # Get CSV content as bytes
    csv_bytes = csv_file.getvalue().encode('utf-8')
    # csv_bytes = csv_file.getvalue().encode('utf-8-sig')
    
    # Use BytesIO for the response
    return BytesIO(csv_bytes)

def create_form(db, form):
    db_item = FormModel(**form)
    db.add(db_item)
    db.commit()
    return {"status": "success"}