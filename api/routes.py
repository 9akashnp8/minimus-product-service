from fastapi import APIRouter

from .endpoints import get_root

router = APIRouter(
    prefix="/api"
)

router.add_api_route("/", get_root)
