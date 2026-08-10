from app.db.database import SessionLocal


def get_db():
    """Provides a database session to each request, then closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
