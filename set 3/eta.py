def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), info in route_map.items():
            if start == current_stop:
                total_time += info["travel_time_mins"]
                current_stop = end
                break

    return total_time