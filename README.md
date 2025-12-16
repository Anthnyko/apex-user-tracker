# Apex Legends Global Stats Tracker

A lightweight Python tool that fetches and displays **global career statistics** for any Apex Legends player using the public Mozambique API.  
This project focuses on clean architecture, simple usage, and reliable data — no per‑legend analytics, no match history, just the core global stats the API consistently provides.

---

## Features

- Fetches global Apex Legends stats for any username  
- Cleanly parses:
  - Account level  
  - XP progress  
  - Rank (name, division, RP)  
  - Career kills  
  - Career wins  
  - Career revives  
  - Platform  
  - Ban status  
- Simple, readable CLI output  
- Modular architecture:
  - `api_client.py` handles API requests  
  - `parser.py` extracts structured data  
  - `main.py` provides the CLI interface  

---

## Requirements

- Python 3.10+  
- A valid **Mozambique API key**  
  - Get one here: https://portal.apexlegendsapi.com/

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/apex-user-tracker.git
cd apex-user-tracker
```

Install dependencies (if you add any later):

```bash
pip install -r requirements.txt
```

Add your API key to api_client.py:

```Python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## Usage

Run the tracker:

```bash
python main.py
```
Enter a username when prompted (EA Username):

```
Enter Apex Legends username: Mogii_q
```

Example output:

```
=== Global Stats for Mogi ===
Level: 218 (26% to next level)
Rank: Platinum 2 — 10850 RP
Platform: PC

Career Stats:
• Total Kills: 6743
• Total Revives: 1462
• Total Wins: 267

Ban Status: None
```

---

## Project Structure

```
apex-user-tracker/
│
├── api_client.py      # Handles API requests
├── parser.py          # Extracts and structures global stats
├── main.py            # CLI entry point
└── README.md
```

---

## How It Works

1. `api_client.py`
Sends a request to the Mozambique API and returns the raw JSON response.

2. `parser.py`
Extracts only the reliable global stats:
- Level
- XP progress
- Rank
- Kills
- Wins
- Revives
- Ban info

3. `main.py`
Handles user input and prints the formatted results.

---

## Limitations

The public Apex API does not provide:
- Career deaths
- Per‑legend wins
- Per‑legend damage
- Per‑legend K/D
- Match history
- Time played

Because of this, the tracker focuses on global career stats only, which are consistently available and accurate.

---

## Future Improvements

Potential enhancements:
- Command‑line arguments (python main.py Mogi)
- Compact output mode
- Colorized CLI output
- Packaging as a pip‑installable tool
- Web UI (Flask/FastAPI)
- Caching to reduce API calls

---

## License
MIT License — feel free to use, modify, and build on this project.

---
