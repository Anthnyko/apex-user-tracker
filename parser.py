def parse_global_stats(data: dict) -> dict:
    """
    Extracts clean, safe global stats from the Apex API response.
    Returns a dictionary with only the fields we care about.
    """

    global_data = data.get("global", {})

    # Defensive programming: safely extract fields
    name = global_data.get("name", "Unknown")
    level = global_data.get("level", 0)
    next_level_percent = global_data.get("toNextLevelPercent", 0)

    # Ban info
    bans = global_data.get("bans", {})
    is_banned = bans.get("isActive", False)
    ban_reason = bans.get("last_banReason", None)

    # Ranked info
    rank = global_data.get("rank", {})
    rank_name = rank.get("rankName", "Unranked")
    rank_div = rank.get("rankDiv", None)
    rank_score = rank.get("rankScore", 0)

    return {
        "name": name,
        "level": level,
        "next_level_percent": next_level_percent,
        "is_banned": is_banned,
        "ban_reason": ban_reason,
        "rank_name": rank_name,
        "rank_div": rank_div,
        "rank_score": rank_score
    }
