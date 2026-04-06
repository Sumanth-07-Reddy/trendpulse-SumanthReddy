# trendpulse-SumanthReddy

# TrendPulse: What's Actually Trending Right Now

A 4-part data pipeline project built as part of the Masai School curriculum.  
TrendPulse fetches **live trending stories** from the **Hacker News API**, cleans the data, performs analysis using NumPy & Pandas, and visualizes insights — all across 4 Python scripts.

---

## 📋 Project Overview

**TrendPulse** is a complete end-to-end data pipeline that helps you discover what's trending on Hacker News right now by:

- Fetching real-time top stories from Hacker News (no API key required)
- Categorizing stories into 5 categories: **Technology, Worldnews, Sports, Science, Entertainment**
- Cleaning and standardizing the data
- Analyzing trends (scores, comments, category distribution, etc.)
- Creating insightful visualizations

### Pipeline Structure
| Task | Script                        | Description                          |
|------|-------------------------------|--------------------------------------|
| 1    | `task1_data_collection.py`    | Fetch JSON from Hacker News API + Categorize |
| 2    | `task2_data_cleaner.py`       | Clean CSV/JSON, handle missing values |
| 3    | `task3_data_analyzer.py`      | Analysis using NumPy & Pandas         |
| 4    | `task4_data_visualizer.py`    | Generate visualizations               |

---

## ✨ Features

- Fetches up to **25 stories per category** (max 125 stories total)
- Intelligent keyword-based categorization (case-insensitive)
- Proper error handling and rate-limiting (2-second sleep per category)
- Saves data in structured JSON format with timestamp
- Includes all required fields: `post_id`, `title`, `category`, `score`, `num_comments`, `author`, `collected_at`
- Well-commented, clean, and production-ready code

---

## 🛠️ Tech Stack

- **Python 3**
- `requests` – for API calls
- `pandas` & `numpy` – for analysis
- `matplotlib` / `seaborn` – for visualization
- JSON & CSV handling

---

## 📁 Project Structure
