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

def parse_legend_stats(data: dict) -> dict:
    """
    Extracts stats for the selected legend and global legend stats.
    Returns a clean dictionary with only the fields we care about.
    """

    legends = data.get("legends", {})

    # Selected legend info
    selected = legends.get("selected", {})
    selected_name = selected.get("LegendName", "Unknown")

    # Extract selected legend stats
    selected_stats_raw = selected.get("data", [])
    selected_stats = {}

    for stat in selected_stats_raw:
        key = stat.get("key")
        value = stat.get("value", 0)
        if key:
            selected_stats[key] = value

    # Global legend stats (career totals)
    global_section = legends.get("all", {}).get("Global", {})
    global_stats_raw = global_section.get("data", [])
    global_stats = {}

    for stat in global_stats_raw:
        key = stat.get("key")
        value = stat.get("value", 0)
        
        # Skip outdated or irrelevant stats
        if key == "jackson_bow_out_damage_done":
            continue

        if key:
            global_stats[key] = value

    return {
        "selected_legend": selected_name,
        "selected_stats": selected_stats,
        "global_stats": global_stats
    }
