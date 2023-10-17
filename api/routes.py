from fastapi import APIRouter

from .endpoints import (
    get_root,
    get_products_list,
)

router = APIRouter(
    prefix="/api"
)

router.add_api_route("/", get_root)
router.add_api_route("/product", get_products_list)
