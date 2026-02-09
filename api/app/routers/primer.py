from fastapi import APIRouter

from app.schemas.primer import PrimerDesignRequest, PrimerDesignResponse
from app.services.primer_service import design_primers

router = APIRouter()


@router.post("/primer/design", response_model=PrimerDesignResponse)
def primer_design(payload: PrimerDesignRequest) -> PrimerDesignResponse:
    return design_primers(payload)
