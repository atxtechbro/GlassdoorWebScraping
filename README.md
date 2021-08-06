Scraping Glassdoor
Linking Corporation Names and ID's thru Automated Processes

by Morgan Joyce
Purpose

Our clients’ have an interest in receiving high quality data hard to obtain anywhere else. Scraping is a data collection method useful in situations where we have little or no custody over the source data. We need to do the groundwork of finding out which ID’s are linked to which Company’s in order to achieve high level insights for our clients’. Rather than complete this process by hand, this project’s goal is to fabricate an automated solution which can be reused. The documentation contained herein is provided to serve as a guide so we can refer to it later as needed.

Challenges

Glassdoor is actively trying to prevent external developers from accessing their data. Unfortunately, they seem to take a strict approach to this - and do not seem to mind inconveniencing legitimate users. Forced throughout this project to take breaks in order to avoid raising red flags
Since there are about 500,000 companies, that means 50,000 web browser requests will have to be sent to Glassdoor servers. The main challenge here is ensuring we do not have to start over should we unexpectedly fail halfway through, and also the time expenditure in running that script. For the purposes of this project, we will not run the script to completion. It should be able to run in 8-36 hours if need be. Refer to this documentation should that ever become necessary

Plan
We will overcome the defenses Glassdoor  has set up by mimicking the behavior of a real user. The scraping app randomly ‘sleeps’ in between HTTP requests so as not to arise suspicious activity. Since it takes a while for a regular website visitor to take up to a minute to read the 10 companies per page, we cannot go noticeably faster than them to avoid raising red flags
The end product will be a Python dictionary with corporationID’s as its’ keys and corporationNames as its’ values. Accuracy goal is 100% and a 98% count of company population is also important so we don’t have to run this more than once per quarter or so.

Assumptions
this approach to grabbing company names and ID’s ten at a time and looping through the pages will capture every single company in the Glassdoor database means we will be 98% rather than 100% successful in counting every single company
In reality, this is extremely unlikely to be the result. Company ranking could change during the course of a 24-hour long web crawling, or new companies could be added to a place where we have already finished already. To mitigate the practical negative side effects of these unfortunate cases, we are choosing to take a specific approach to starting our iterations with this problem in mind, as outlined in the next section.
Transformations
filtering company search results as broadly as possible
search for a blank company name and to type in ‘United States’ in the location bar
immediately to the right hand side of the company bar. It will display in a drop down list after starting to type into the field
fetches 319,046 unique companies as of Friday, August 6, 2021
Sources
easiest to manage the iterations when dealing with the source page directly. There is only one parameter to change which is done programmatically using Python string formatting. The query I am requesting from Glassdoors servers is actually a HTTP url like this - this is the long version which is what we want
view-source:https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=0&page=1&isHiringSurge=0&locId=1&locType=N&locName=US
In the above url, the locId field right above is what will be incremented

Requirements
Python
Requests
Re (regular expressions)
JSON

Destination
Working copy of this application is ready to go on my github at https://github.com/mojo-py
I will include a sample of 500 - 1000 name, id pairs and include that with my submission in case the reviewers don’t have python but still want to check for accuracy

Versions

Version
Date
Developer
Reviewer
v1.0
August 6th, 2021
Morgan Joyce
Hannah Kelsen


















Appendix - Sample


{'9079': 'Google',
 '1651': 'Microsoft',
 '40772': 'Facebook',
 '1425': 'Cisco Systems',
 '1138': 'Apple',
 '41283': 'US Air Force',
 '1327': 'Dell Technologies',
 '1519': 'Intel Corporation',
 '3736': 'Capital One',
 '404': 'Lockheed Martin',
 '316784': 'Raiffeisen International',
 '2763': 'Deloitte',
 '571855': 'BKT',
 '898126': 'Albtelecom',
 '1399466': 'ikubINFO',
 '2933338': 'AlbStar',
 '4825887': 'Innohub Technologies',
 '970526': 'PAE Antarctica McMurdo Station',
 '139275': 'GHG Corp',
 '5847': 'BBC',
 '258853': 'GSC',
 '921832': 'Jalasoft',
 '284292': 'mojix',
 '445442': 'Engro',
 '5143819': 'Banco Ecofuturo',
 '324691': 'Banco de de Credito BCP',
 '360923': 'Zendesk',
 '864485': 'BairesDev',
 '3433': 'Ritz-Carlton',
 '2867': 'KPMG',
 '9955': 'Kimpton Hotels & Restaurants',
 '7790': 'Marriott International',
 '484516': 'Westin',
 '8450': 'PwC',
 '354541': 'Cable & Wireless Communications',
 '2784': 'EY',
 '5744': 'Banco Comercial Português',
 '330': 'Hilton',
 '647048': 'Cabocom',
 '950367': 'TUI Group',
 '3879': 'Boston Consulting Group',
 '122747': 'The Church of Jesus Christ of Latter-day Saints',
 '5833': 'Shell',
 '14903': 'Peace Corps',
 '1064532': 'Ronda',
 '3109239': 'Mudwraps to Manicures',
 '4138': 'Accenture',
 '6036': 'Amazon',
 '10883': 'Capita',
 '10471': 'SAP',
 '433703': 'MongoDB',
 '285406': 'HedgeServ',
 '869180': 'University of the South Pacific',
 '563936': 'Ministry of Youth and Sports',
 '4018863': 'Vinod Patel & Company',
 '3684180': 'Fiji Airways',
 '5782': 'ANZ Bank',
 '21435': 'United Nations',
 '38615': 'DHL Express',
 '230523': 'UNDP',
 '603323': 'TBC Bank',
 '727708': 'Bank of Georgia',
 '696415': 'Evolution',
 '544282': 'Liberty Bank (Georgia)',
 '1921027': 'Georgian Water and Power',
 '3940535': 'Ilia State University',
 '4043294': 'Hualing Group',
 '3141064': 'Iv. Javakhishvili Tbilisi State University',
 '659718': 'Ministry of Economy and Sustainable Development of Georgia',
 '3494': 'Nokia',
 '5775': 'Vodafone',
 '325524': 'Intracom Telecom',
 '1717059': 'Beat',
 '100815': 'Intrasoft International',
 '578010': 'Infobip',
 '39767': 'A1 Hrvatska',
 '3510': 'Siemens',
 '3472': 'Ericsson-Worldwide',
 '354': 'IBM',
 '587146': 'Zagrebacka Banka',
 '3752': 'Bain & Company',
 '2893': 'McKinsey & Company',
 '544': 'Procter & Gamble',
 '327712': 'La Sapienza Università',
 '11701': 'Avanade',
 '304581': 'Safaricom',
 '40545': 'Kenya Airways',
 '460996': 'KCB Bank',
 '564204': 'Kenya Revenue Authority',
 '882830': 'Andela',
 '319345': 'One Acre Fund',
 '422021': 'Equity Bank',
 '483520': 'Sama',
 '26491': 'American University of Beirut',
 '145513': 'Murex',
 '1009457': 'Banque Libano-Française',
 '587211': 'Khalil Fattal et Fils',
 '308175': 'Nexius',
 '1123776': 'ITG Holding',
 '799729': 'Alfa (Lebanon)',
 '1257145': 'Oworkers',
 '16869': 'UNICEF',
 '6685': 'Rio Tinto',
 '4075': 'Orange',
 '4351230': 'Groupe Socota',
 '421612': 'Deutsche Gesellschaft für Internationale Zusammenarbeit',
 '2000864': 'B2Gold',
 '41195': 'The World Bank',
 '547080': 'Danish Refugee Council',
 '35565': 'Oxfam',
 '667913': 'Appen',
 '574190': 'Médecins Sans Frontières',
 '990287': 'Action Contre la Faim ',
 '585411': 'Zalora',
 '461386': 'Agoda',
 '8270': 'Petronas',
 '3492': 'Nestlé',
 '8915': 'Infineon Technologies',
 '877317': 'Keysight Technologies',
 '193828': 'NTNU',
 '10408': 'Equinor',
 '419498': 'University of Bergen',
 '680293': 'DNB',
 '248668': 'Universitetet i Oslo',
 '35206': 'Yara',
 '7834': 'Arm',
 '4212': 'NCR',
 '451902': 'Zühlke',
 '690607': 'msg global solutions',
 '245799': 'Grid Dynamics',
 '233751': 'Endava',
 '990033': 'Hyperoptic',
 '3956': 'Schneider Electric',
 '3353': 'Robert Bosch',
 '6359': 'JTI - Japan Tobacco International',
 '1002327': 'JA Resorts & Hotels',
 '4202': 'Four Seasons',
 '2110438': 'Seychelles Civil Aviation Authority',
 '591828': 'Anantara Hotels, Resorts & Spas',
 '2994585': 'Ministry of Education Seychelles',
 '334402': 'Viceroy Hotel Group',
 '1182256': 'Massy Group of Companies',
 '11013': 'Scotiabank',
 '3358': 'RBC',
 '806': 'Carnival',
 '7508': 'BDO',
 '7860': 'KFC',
 '243793': 'Digicel',
 '1156474': 'HomeLight',
 '364405': 'OSCE',
 '32768': 'U.S. Department of State',
 '320386': 'International Committee of the Red Cross',
 '40056': 'ZTE',
 '2351059': 'Cambridge Worldwide Academy Tajikistan',
 '1358525': 'ANKA Trading',
 '18874': 'IFC',
 '343333': 'Academia Sinica',
 '8983': 'Trend Micro',
 '4130': 'TSMC',
 '40142': 'MediaTek',
 '41150': 'HTC',
 '11939': 'Quanta Computer',
 '40093': 'ASUS',
 '254537': 'National Taiwan University',
 '236656': 'Sail Caribbean',
 '3198061': 'Royal Virgin Islands Police Force',
 '450129': 'Oceania Cruises',
 '121863': 'El Camino Health',
 '6069': 'FTI Consulting',
 '432775': 'Infinite Solutions',
 '288826': 'AIDS Healthcare Foundation',
 '264017': 'Elizabeth Glaser Pediatric AIDS Foundation',
 '2851': 'The Johns Hopkins University',
 '859820': 'Mobile Telephone Network (MTN)',
 '18839': 'World Vision International'}
