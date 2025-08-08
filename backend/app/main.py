from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, utils
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='KYC as a Service (Dev)')

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/users/', response_model=schemas.UserOut)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already exists')
    u = crud.create_user(db, user)
    utils.write_audit(db, 'user.create', actor=user.email, resource=str(u.id))
    return u

@app.get('/users/', response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post('/kyc/submit', response_model=schemas.KYCOut)
def submit_kyc(payload: schemas.KYCSubmit, db: Session = Depends(get_db)):
    # naive check: user exists
    user = db.query(models.User).filter(models.User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    rec = crud.create_kyc(db, payload)
    utils.write_audit(db, 'kyc.submit', actor=user.email, resource=str(rec.id))
    return rec

@app.get('/kyc/status/{kyc_id}', response_model=schemas.KYCOut)
def kyc_status(kyc_id: int, db: Session = Depends(get_db)):
    rec = crud.get_kyc(db, kyc_id)
    if not rec:
        raise HTTPException(status_code=404, detail='KYC not found')
    return rec

@app.post('/aml/check', response_model=schemas.AMLResponse)
def aml_check(req: schemas.AMLRequest, db: Session = Depends(get_db)):
    rec = crud.get_kyc(db, req.kyc_id)
    if not rec:
        raise HTTPException(status_code=404, detail='KYC not found')
    result = utils.random_aml_check()
    # update status on FAIL for demo
    if result == 'FAIL':
        crud.update_kyc_status(db, req.kyc_id, models.KYCStatus.rejected)
    else:
        crud.update_kyc_status(db, req.kyc_id, models.KYCStatus.approved)
    utils.write_audit(db, 'aml.check', actor='system', resource=str(req.kyc_id), details=result)
    return schemas.AMLResponse(kyc_id=req.kyc_id, result=result)
