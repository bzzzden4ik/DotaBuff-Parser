# Dota 2 Match & Stats Parser

A robust Python-based web scraper designed to extract comprehensive Dota 2 match statistics and player data from Dotabuff and export it directly into structured Excel (`.xlsx`) spreadsheets for deep data analysis.

## ✨ Key Features

* **Automated Extraction:** Scrapes match details, hero statistics, win rates, and custom player metrics from Dotabuff.
* **Data Structuring & Cleaning:** Processes raw HTML structures and filters out noise into uniform datasets.
* **Excel Export:** Generates fully structured `.xlsx` files with clean columns, ready for pivot tables, filtering, or visualization.
* **Modular Design:** Easily extensible to target new endpoints or extract additional metrics.

## 🛠 Tech Stack

* **Python 3.x:** Core programming language.
* **Requests:** For handling HTTP network requests and managing session headers.
* **BeautifulSoup4 (bs4):** For parsing HTML documents and traversing the DOM tree to extract specific data nodes.
* **Pandas:** For advanced data manipulation, structuring dataframes, and seamless export to Excel formats.

## 🔄 Current Project Status & Technical Challenges

**Current Phase:** *Active Maintenance & Refactoring (Bypassing Dynamic Protections)*

Due to recent changes in the target website's security policies, the parser is currently being updated to handle advanced anti-scraping mechanisms:
* **JS Execution Bypass:** Overcoming the "Enable JavaScript" challenge page.
* **Cookie & Session Management:** Implementing dynamic cookie handling and mimicking legitimate browser footprints to avoid automated blocks.
* *Note:* The project is transitioning from a lightweight static scraper to a more resilient headless or token-based session handling architecture to ensure long-term stability.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed, then install the required dependencies:

```bash
pip install requests beautifulsoup4 pandas fake-useragent
```

Or set up an environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

And install dependecies:

```bash
pip install -r requirements.txt
```

## How to use
Run DotabaffParser.py

Then enter user id and it will collect all matches into xlsx table: [userName.xlsx] 
