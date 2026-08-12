from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to SupportOps!"}


@router.get("/health")
def health_check():
    return {"status": "healthy"}
