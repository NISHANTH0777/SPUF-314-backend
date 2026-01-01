from fastapi import APIRouter
from app.services.route_finder import find_direct_routes, find_connected_route

router = APIRouter()

@router.get("/search-route")
def search_route(source: str, destination: str):

    direct = find_direct_routes(source, destination)
    if direct:
        return {
            "type": "DIRECT",
            "routes": direct
        }

    connected = find_connected_route(source, destination)
    if connected:
        return {
            "type": "CONNECTED",
            "route": connected
        }

    return {
        "type": "NO_ROUTE",
        "message": "No route found"
    }
