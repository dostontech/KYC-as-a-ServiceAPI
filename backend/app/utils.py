import random
from .database import get_db
from .models import AuditLog

from sqlalchemy.orm import Session

def random_aml_check() -> str:
    # Simple random pass/fail for demo
    return 'PASS' if random.random() > 0.3 else 'FAIL'

def write_audit(db: Session, event: str, actor: str = None, resource: str = None, details: str = None):
    log = AuditLog(event=event, actor=actor, resource=resource, details=details)
    db.add(log)
    db.commit()