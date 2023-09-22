## lefaso-net-scraper

<div align="center">
  <p>
    <a href="https://pypi.org/project/lefaso-net-scraper/"><img src="https://pypi.org/static/images/logo-small.2a411bc6.svg" style="width:50px;height:50px;"></a>
    <a href="https://github.com/abdoulfataoh/lefaso-net-scraper/"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png" style="width:80px;height:40px;"></a> 
  </p>
</div>



<div align="center">
  <p>
    <img src="https://github.com/abdoulfataoh/lefaso-net-scraper/actions/workflows/test-action.yaml/badge.svg">
    <img src="https://github.com/abdoulfataoh/lefaso-net-scraper/actions/workflows/publish-action.yaml/badge.svg">
  </p>
</div>

### Description
lefaso-net-scraper is a robust and versatile Python library designed to efficiently extract articles from the popular online news source, lefaso.net. This powerful scraping tool allows users to effortlessly collect article content and data from Internet users’ comments on lefaso.net.

# Data Format

<div align="center">

| Field                  | Description            |
|------------------------|------------------------|
| article_topic          | article topic          |
| article_title          | article title          |
| article_published_date | article published date |
| article_origin         | article origin         |
| article_url            | article url            |
| article_content        | article content        |
| article_comments       | article comments       |

</div>

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
scraper = LefasoNetScraper(section_url)
data = scraper.run()
```

> Settings Pagination range

```python
# coding: utf-8

from lefaso_net_scraper import LefasoNetScraper

section_url = 'https://lefaso.net/spip.php?rubrique473'
scraper = LefasoNetScraper(section_url)
scraper.set_pagination_range(start=20, stop=100)
data = scraper.run()
```

> Save data to csv

```python

# coding: utf-8

from lefaso_net_scraper import LefasoNetScraper
import pandas as pd

section_url = 'https://lefaso.net/spip.php?rubrique473'
scraper = LefasoNetScraper(section_url)
data = scraper.run()
df = pd.DataFrame.from_records(data)
df.to_csv('path/to/df.csv')
```
