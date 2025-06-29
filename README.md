📜 Background

This project doesn’t contain the actual scraping logic, but here’s what I used to do:

I originally used webscraper.io to collect listings from eBay and other sites. While that scraping setup isn’t included here, the CSV and Excel files in this repo contain the links and metadata I exported during those sessions.

You could also just:
	•	Right-click on a webpage with lots of listings
	•	Use “Save As…” in your browser
	•	Grab the HTML elements and preview images that way

Some of the thumbnail URLs may now be outdated, but the method still works: iterate through a CSV of URLs and download the highest-quality image available.

There are many places online to find clean 70mm film cell scans — including:
	•	eBay sellers (search for “IMAX Interstellar film cell”)
	•	Instagram accounts that archive film memorabilia
	•	Collector forums and Blu-ray subreddits

In short: this repo serves as a foundation for organizing and managing scraped preview images. All it does is read a CSV and download each image — that’s it.