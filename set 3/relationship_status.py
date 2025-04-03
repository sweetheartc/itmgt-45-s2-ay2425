def relationship_status(from_member, to_member, social_graph):
    from_follows_to = to_member in social_graph[from_member]["following"]
    to_follows_from = from_member in social_graph[to_member]["following"]

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"
