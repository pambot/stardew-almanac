# Stardew Almanac
The Stardew Valley farmer's almanac. All icons and artwork and data comes 
from the [Stardew Valley Wiki](https://stardewvalleywiki.com/), which is a 
much more complete resource for everything Stardew. This site is intended to 
organize a few bits and pieces of it so it's easier to remember what you're 
supposed to do on every calendar day.

## For users
Everything you need is on the Github project site: 
[The Stardew Almanac]().

## For developers
This site is comprised of static HTML pages built with Pelican in Python. The 
data is scraped from the Wiki and organized into tables using Pandas (why 
Pandas? I'm a data scientist and when all you have is a hammer, etc.). The 
information from those tables are organized and formatted into the static 
pages.

To get started, install dependencies.
```bash
pip install -r requirements.txt

```
To run the scrapers that retrieves and formats the site data:
```bash
python scraper.py

```
To make site changes:
```bash

```

To start the site preview:
```bash

```
