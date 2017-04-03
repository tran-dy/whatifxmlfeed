# whatifxmlfeed

Combining archived Atom feeds to create an ereader version of [What If?](https://what-if.xkcd.com/).

## Why?

[Calibre](https://calibre-ebook.com/) offers a way to create ebook "newspapers" out of RSS/Atom feeds. Feeds are intrinsically volatile so there are limits on the number of articles any single feed contains. So, ebooks with older articles can be made by combining archived feeds.

## How?

1. Gather a list of timestamps
2. Utilize the [Internet Archive's Wayback Machine API](https://archive.org/help/wayback_api.php) to access archived feeds at these timestamps
3. Parse archived feeds to gather articles
4. Append articles to a new feed
5. Host this feed and use calibre to make an ebook

By providing the Wayback Machine API a timestamp, a specific archived feed can be located. Each feed contains about three articles. So, a list of timestamps was made by determining which timestamps would be sufficient for total coverage of all previous articles.

The raw output of "buildxml.py" contained several duplications and missed a number of articles. These were corrected by hand. Adding in articles that had no archived feed was a matter of reformatting some HTML to XML.

The calibre recipe was modified twice: "oldest_article" and "max_articles_per_feed" were both increased to accommodate the backlog of articles.
