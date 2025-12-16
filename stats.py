def compute_basic_stats(global_stats: dict, legend_stats: dict) -> dict:
    """
    Computes basic performance metrics from parsed global and legend stats.
    """

    # Global totals
    total_kills = legend_stats["global_stats"].get("career_kills", 0)
    total_wins = legend_stats["global_stats"].get("career_wins", 0)
    total_revives = legend_stats["global_stats"].get("career_revives", 0)

    # Selected legend stats
    selected_kills = legend_stats["selected_stats"].get("career_kills", 0)
    selected_revives = legend_stats["selected_stats"].get("career_revives", 0)

    # Derived metrics
    damage_done = legend_stats["global_stats"].get("jackson_bow_out_damage_done", 0)
    damage_per_kill = damage_done / total_kills if total_kills > 0 else 0

    return {
        "total_kills": total_kills,
        "total_wins": total_wins,
        "total_revives": total_revives,
        "selected_kills": selected_kills,
        "selected_revives": selected_revives,
        "damage_done": damage_done,
        "damage_per_kill": round(damage_per_kill, 2)
    }

def compute_legend_performance(legend_stats: dict) -> dict:
    selected = legend_stats["selected_stats"]

    score = 0
    components = {}

    # Kills
    if "career_kills" in selected:
        kills = selected["career_kills"]
        components["kills"] = kills
        score += min(kills / 10000, 1.0) * 0.5  # up to 50% of score

    # Revives
    if "career_revives" in selected:
        revives = selected["career_revives"]
        components["revives"] = revives
        score += min(revives / 3000, 1.0) * 0.3  # up to 30%

    # Mobility / other trackers
    if "double_time_distance" in selected:
        dist = selected["double_time_distance"]
        components["mobility"] = dist
        score += min(dist / 500000, 1.0) * 0.2  # up to 20%

    return {
        "components": components,
        "performance_score": round(score, 3)
    }

