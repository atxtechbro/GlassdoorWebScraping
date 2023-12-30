<h1>Scraping Glassdoor: A GraphQL Journey</h1>
<h2>Harnessing Automated Data Harvesting for In-depth Business Insights</h2>
<h3>by Morgan Joyce</h3>

<h3>Purpose</h3>

The inspiration for this project, version 3.1 as of 12/29/23, stems from the recognition of the immense value that lies within the vast amounts of data available on platforms like Glassdoor. Glassdoor, being a rich repository of company data, employee reviews, and job postings, presents a unique opportunity for data-driven insights.

The purpose of this project is to harness this potential by providing a robust tool that can efficiently extract and analyze this data. The tool is designed with an API-first strategy, ensuring it is lightweight, fast, and capable of handling large volumes of data.

The extracted data can be used to fuel a variety of business intelligence and analytics applications. From understanding market trends and competitor performance to predicting future industry shifts using machine learning algorithms and predictive analytics, the possibilities are vast.

This project is a testament to the power of data and our commitment to enabling businesses to leverage this power to drive decision-making, strategy, and growth.

<h3>Challenges</h3>

One of the main challenges faced during the development of this project was figuring out the correct structure for the GraphQL query and headers. Glassdoor's API is not publicly documented, which made it difficult to determine the correct format for the query and headers. Additionally, the URL format needed to receive a JSON response was hard to find, possibly hidden intentionally.

Another challenge was dealing with rate limits. The script is limited to 100 pages x 100 records per page = 10,000 companies per query.

<h3>Plan</h3>

The current script is designed to efficiently navigate through the pages of company data, resetting after reaching the 99th page or upon landing on the last page of existing companies meeting the criteria. However, to truly scale this solution and optimize for performance, implementing a database system is a crucial next step.

A well-structured database would allow for more efficient storage and retrieval of data, reducing the need for repeated API calls and thus mitigating the risk of hitting rate limits. It would also provide a robust foundation for adding more complex features, such as advanced filtering by sub-industry, ratings, or other criteria.

While the current script serves its purpose for a limited scope of data, we are fully aware that scalability and performance optimization are key considerations for any data-intensive application. As such, the implementation of a database system is a planned enhancement for future iterations of this project.

This presents an excellent opportunity for contributors looking to gain experience in system design and database implementation. We welcome any contributions and look forward to collaborating with you on this exciting enhancement.

[^1]: *Reitz, Kenneth. 2021. “Requests 2.26.0 documentation.” Requests: HTTP for Humans™. https://docs.python-requests.org/en/master/index.html#the-user-guide


<h3>Example Data</h3>

Here is an example of what one row in the query might look like for a well-known company like Google:

| ID | Name | Logo | Location | Size | Size Category | Description | Glassdoor URL | Number of Reviews | Number of Jobs | Number of Salaries | Overall Rating |
|----|------|------|----------|------|---------------|-------------|---------------|-------------------|----------------|--------------------|----------------|
| 9079 | Google | https://media.glassdoor.com/sql/9079/google-squarelogo-1630549979272.png | Mountain View, CA | 10000+ Employees | GIANT | Google is not a conventional company, and we don’t intend to become one... | /Overview/Working-at-Google-EI_IE9079.11,17.htm | 16700 | 1234 | 12345 | 4.5 |

Each row in the query represents a unique company and contains the following information:

- `ID`: The unique identifier for the company.
- `Name`: The name of the company.
- `Logo`: The URL of the company's logo.
- `Location`: The location of the company's headquarters.
- `Size`: The size of the company in terms of number of employees.
- `Size Category`: The category of the company's size (e.g., SMALL, MEDIUM, LARGE, GIANT).
- `Description`: A brief description of the company.
- `Glassdoor URL`: The URL of the company's Glassdoor page.
- `Number of Reviews`: The number of reviews the company has received on Glassdoor.
- `Number of Jobs`: The number of job postings the company currently has on Glassdoor.
- `Number of Salaries`: The number of salaries reported for the company on Glassdoor.
- `Overall Rating`: The company's overall rating on Glassdoor.

<h3>Version History</h3>

- v1.0 08/06/21
- v2.0 08/12/21
- v2.1 12/18/21
- v3.1 12/29/23

<h3>Developer</h3>

Morgan Joyce