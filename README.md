# Pexels scraper
A python command-line tool for scraping images from [Pexels.com](https://www.pexels.com/) by a specific category.

## Info

[Pexels.com](https://www.pexels.com/) is a platform which provides royalty-free photos and videos. In order to automate the process of downloading images, 200 API calls per hour are available, with a max of 20.000 calls per month. An API key can be requested after sign-up.

This command-line tool was made with Python 3.7.6.

## How To Use

Input arguments:
* `-k/--key` **[str]** : API key (56 chars).
* `-c/--cat` **[str]** : Name of the category to scrape.
* `-d/--save_dir` **[str]** : Output directory for images.
* `-p/--pages` **[int]** : Subsequent integeres denoting `start_page`, `end_page` and `per_page`. If set to *-1*, all images will be scraped.
* `-v/--verbose` **[int/str]** : Optional to set verbose mode, which shows when a page is done scraping. Defaults to `True`.  
 Valid options are: `"y"`, `"yes"`, `"true"`, `"t"`, `1` or `"n"`, `"no"`, `"false"`, `"f"`, `0`.


## Examples

The following will get images from category `universe` while starting from page `1`, ending at page `1` and only getting `10` images per page.

```python
python main_scraper.py -k "lVkECaSAqkFNAq5rQKutrqvXsTW6ySCjejeV9B8M5yN7MLek2H0Ft7ZG" -c "universe" -d "D:\Documents\pexels" -p 1 1 10
```

The following will get images from category `nature` and get every image available, but verbose mode is turned off.

```python
python main_scraper.py -k "lVkECaSAqkFNAq5rQKutrqvXsTW6ySCjejeV9B8M5yN7MLek2H0Ft7ZG" -c "nature" -d "D:\Documents\pexels" -p -1 -v 0
```
