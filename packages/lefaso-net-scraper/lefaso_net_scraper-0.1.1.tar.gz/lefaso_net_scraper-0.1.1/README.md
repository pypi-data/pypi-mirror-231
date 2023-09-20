## lefaso-net-scraper


### Description
lefaso-net-scraper is a robust and versatile Python library designed to efficiently extract articles from the popular online news source, lefaso.net. This powerful scraping tool allows users to effortlessly collect article content and data from Internet users’ comments on lefaso.net.

# Data Format

| Field                  | Description            |
|------------------------|------------------------|
| article_topic          | article topic          |
| article_title          | article title          |
| article_published_date | article published date |
| article_origin         | article origin         |
| article_url            | article url            |
| article_content        | article content        |
| article_comments       | article comments       |

### Installation

- With poetry

```bash
poetry add lefaso-net-scraper
```

- With pip

```bash
pip install lefaso-net-scraper
```

### Usage

```python
# coding: utf-8

from lefaso_net_scraper import LefasoNetScraper

section_url = 'https://lefaso.net/spip.php?rubrique473'
task = LefasoNetScraper(section_url)
data = task.run()
```
