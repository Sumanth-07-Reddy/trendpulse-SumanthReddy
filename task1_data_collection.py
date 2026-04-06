# task1_data_collection.py
# TrendPulse - Task 1: Fetch trending stories from Hacker News

import requests
import json
import os
from datetime import datetime
import time

# ====================== CONFIGURATION ======================
TOPSTORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {"User-Agent": "TrendPulse/1.0"}

# Category keywords (case-insensitive)
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

MAX_PER_CATEGORY = 25
DATA_FOLDER = "data"

# Create data folder if it doesn't exist
os.makedirs(DATA_FOLDER, exist_ok=True)

# ====================== STEP 1: Fetch Top Story IDs ======================
print("Fetching top story IDs from Hacker News...")
response = requests.get(TOPSTORIES_URL, headers=HEADERS)
response.raise_for_status()
story_ids = response.json()[:500]   # Limit to first 500 IDs

print(f"Received {len(story_ids)} story IDs.")

# ====================== STEP 2: Collect Stories by Category ======================
collected_stories = []
today_str = datetime.now().strftime("%Y%m%d")

for category, keywords in CATEGORIES.items():
    print(f"\nCollecting up to {MAX_PER_CATEGORY} stories for category: {category.upper()}")
    count = 0

    for sid in story_ids:
        if count >= MAX_PER_CATEGORY:
            break

        try:
            url = ITEM_URL.format(sid)
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            item = resp.json()

            if not item or item.get("type") != "story" or not item.get("title"):
                continue

            title_lower = item["title"].lower()

            # Check keyword match for this category
            if any(kw in title_lower for kw in keywords):
                story = {
                    "post_id": item.get("id"),
                    "title": item.get("title"),
                    "category": category,
                    "score": item.get("score", 0),
                    "num_comments": item.get("descendants", 0),
                    "author": item.get("by", ""),
                    "collected_at": datetime.now().isoformat()
                }
                collected_stories.append(story)
                count += 1
                print(f"  ✓ Added [{category}] {item['title'][:70]}...")

        except Exception as e:
            print(f"  ⚠ Error fetching story {sid}: {e}")
            continue

    # Wait 2 seconds after each category (as per project instruction)
    time.sleep(2)

# ====================== STEP 3: Save to JSON File ======================
json_filename = f"{DATA_FOLDER}/trends_{today_str}.json"

with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(collected_stories, f, indent=2, ensure_ascii=False)

# ====================== FINAL OUTPUT ======================
total = len(collected_stories)
print("\n" + "=" * 60)
print(f"✅ Collected {total} stories successfully!")
print(f"✅ Saved to: {json_filename}")
print("=" * 60)

# Show category-wise count
from collections import Counter
print("Category distribution:")
for cat, cnt in Counter(s["category"] for s in collected_stories).items():
    print(f"   {cat.capitalize():12} : {cnt} stories")