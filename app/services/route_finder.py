from app.utils.loader import STOP_TO_ROUTES, ROUTE_TO_STOPS, ROUTE_TRANSFERS

def find_direct_routes(source, destination):
    result = []

    source_routes = set(STOP_TO_ROUTES.get(source, []))
    dest_routes = set(STOP_TO_ROUTES.get(destination, []))

    common_routes = source_routes & dest_routes

    for route in common_routes:
        stops = ROUTE_TO_STOPS.get(route, [])
        if source in stops and destination in stops:
            s = stops.index(source)
            d = stops.index(destination)
            if s < d:
                result.append({
                    "bus_number": route,
                    "stops": stops[s:d+1]
                })

    return result


def find_connected_route(source, destination):
    source_routes = STOP_TO_ROUTES.get(source, [])
    dest_routes = STOP_TO_ROUTES.get(destination, [])

    for r1 in source_routes:
        stops1 = ROUTE_TO_STOPS.get(r1, [])

        if source not in stops1:
            continue

        s1_index = stops1.index(source)

        # Try every stop AFTER source as transfer stop
        for transfer_stop in stops1[s1_index + 1:]:

            for r2 in dest_routes:
                stops2 = ROUTE_TO_STOPS.get(r2, [])

                if transfer_stop not in stops2 or destination not in stops2:
                    continue

                t2_index = stops2.index(transfer_stop)
                d2_index = stops2.index(destination)

                if t2_index < d2_index:
                    return {
                        "route_1": {
                            "bus_number": r1,
                            "stops": stops1[s1_index : stops1.index(transfer_stop) + 1]
                        },
                        "route_2": {
                            "bus_number": r2,
                            "stops": stops2[t2_index : d2_index + 1]
                        }
                    }

    return None