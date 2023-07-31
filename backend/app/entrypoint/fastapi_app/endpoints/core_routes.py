from fastapi import APIRouter

router = APIRouter()

@router.get('/resource')
def get_resource():
    return {
        'name': 'resource'
    }
