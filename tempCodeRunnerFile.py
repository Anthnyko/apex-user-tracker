from api_client import fetch_player_data
from parser import parse_global_stats

def main():
    username = input("Enter your Apex Legends username: ")
    data = fetch_player_data(username)

    if data is None:
        print("Failed to fetch data.")
        return

    global_stats = parse_global_stats(data)

    print("\n=== Global Stats ===")
    for key, value in global_stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()