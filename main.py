from api_client import fetch_player_data
from parser import parse_global_stats

def main():
    username = input("Enter Apex Legends username: ")
    data = fetch_player_data(username)

    if data is None:
        print("Failed to fetch data.")
        return

    global_stats = parse_global_stats(data)

    print(f"\n=== Global Stats for {global_stats['name']} ===")
    print(f"Level: {global_stats['level']} ({global_stats['next_level_percent']}% to next level)")
    print(f"Rank: {global_stats['rank_name']} {global_stats['rank_div']} — {global_stats['rank_score']} RP")
    print(f"Platform: {data['global'].get('platform', 'Unknown')}")

    # Optional fields
    if global_stats["ban_reason"]:
        print(f"Ban Status: {global_stats['ban_reason']}")
    else:
        print("Ban Status: None")

    # If you want to show global kills/wins/revives:
    legends = data.get("legends", {})
    global_legend_stats = legends.get("all", {}).get("Global", {}).get("data", [])

    kills = next((s["value"] for s in global_legend_stats if s["key"] == "career_kills"), None)
    revives = next((s["value"] for s in global_legend_stats if s["key"] == "career_revives"), None)
    wins = next((s["value"] for s in global_legend_stats if s["key"] == "career_wins"), None)

    if kills is not None:
        print(f"Total Kills: {kills}")
    if revives is not None:
        print(f"Total Revives: {revives}")
    if wins is not None:
        print(f"Total Wins: {wins}")

if __name__ == "__main__":
    main()