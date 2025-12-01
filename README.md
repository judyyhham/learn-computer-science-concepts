# CS Concept Randomizer – Wikipedia Scraper & Study Helper

This project uses **Selenium** and **BeautifulSoup** to scrape a Wikipedia page, extract a list of computer science–related terms, and then **randomly pick concepts to study** by opening Google search tabs for them.

It’s meant as a small learning tool and a practice project to:
- To refresh the memory of fundamental computer science concepts
- Practice handling different data types and Python structures
- Make studying computer science concepts a bit more fun and randomized

---

## Features

- 🌐 Scrapes a target Wikipedia page for a list of terms (e.g. computer science concepts)
- 🧹 Cleans and filters the raw HTML into a usable Python list
- 🎲 Randomly picks one or more concepts from the list
- 🔍 Opens a new browser tab with Google search results for the selected concept(s)
- 🧠 Designed as a study aid so you can repeatedly pull random topics to review

> **Note:** This project is for personal learning and educational use only. Be respectful of website terms of service and scraping rules.

---

## Tech Stack

- **Language:** Python (version X.X – e.g. 3.10)
- **Web Automation:** [Selenium](https://www.selenium.dev/)
- **HTML Parsing:** [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- **Browser:** e.g. Chrome + ChromeDriver (or another driver of your choice)

---

## Prerequisites

- Python installed (e.g. `python3 --version` to check)
- A compatible web driver (e.g. **ChromeDriver**) available on your system path  
  - Make sure the driver version matches your browser version
- `pip` for installing Python packages

---

## Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
