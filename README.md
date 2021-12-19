<h1>Scraping Glassdoor</h1>
<h2>Linking Corporation Names and ID's thru Automated Processes</h2>
<h3>by Morgan Joyce</h3>
 
<h3>Purpose</h3>
 
Job-based social media websites such as Glassdoor provide a window into the human resources of almost nearly all companies. This paradigm lends itself to some unique analytics opportunities, such as gleaning info before it becomes reflected in a quarterly earnings report or even a stock price.
For example, if ten tenured sales professionals within the last two weeks have updated their statuses on LinkedIn to reflect their departure from a company, that could be perceived as a potential red flag investors would want to be aware of. Another example would be an institutional investor requesting ESG metrics about a midsize company, along the lines of age buckets / gender ratio’s etc.
Before tackling some of these highly promising human resource analytics, we need to be able to document the html structure of these social media websites, and figure out a way to automatically program a Python script to extract the needed data for us.
In addition to the documentation herein, this submission includes a Github hosted Python script with ~50 lines which promises to fulfill the requirement of a complete Glassdoor company census of ID, Name pairs. It is extremely lightweight, requiring only one external library, which is an extremely well documented library called requests[^1].

<h3>Challenges</h3>
 
Glassdoor working against the web scraper during every phase of development
url format needed to receive a json response very hard to find
Ctrl+Shift+E, network tab, clear, refresh, filter for json responses and find the earliest one - that should be it
limited to requesting 100 records per request
Limited to 100 pages x 100 records per page = 10,000 companies
Could parse up to 50 x 10,000 = 500,000 if we adjusted the rating parameters to scan each tenth of a 5.0 scale score



<h3>Plan</h3>
 
The code 'turns the page' when it has either landed on the last page of the companies in existence meeting the criteria, or resets to 1 after reading the 99th page. For example, for the first industry Finance & Accounting, there are more than 10,000 registered companies so the script will only count 10,000 before switching over to Aerospace & Defence - for which there will be only 20 pages and then reset to the third industry rather than return pages 20-100 which would be null values.

In order to go even further and collect every single company, additional funcitonality would need to take advantage of a further filter for example sub-industry or ratings.

Rating over and under 3.5/5 for companies for example - this would work until a group of companies in a given industry still had in excess of 10,000 entities either above or below 3.5. If this is the case, the developer coud break it down into smaller buckets or tinker with subSectors as needed. This is a #goodfirst issue and any contributions are welcomed to offer assistance. I would be glad to collaborate with you.




[^1]: *Reitz, Kenneth. 2021. “Requests 2.26.0 documentation.” Requests: HTTP for Humans™. https://docs.python-requests.org/en/master/index.html#the-user-guide


Destination
bizBook.json local storage solution keeps track of the data and saves it to local disk


v1.0 August 6th, 2021
v2.0 August 12, 2021
developer: Morgan Joyce
