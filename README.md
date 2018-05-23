# landwatch
Web scraper tutorial: http://first-web-scraper.readthedocs.io/en/latest/


Daniel notes 5/23:

- site breaks after 100 pages, can't find further listings
- should eventually focus on particular counties, not full states
- individual listings are identified by pid ("property ID") which is uniquely identified
- PID is an 8 digit number
- individual listing urls look like: https://www.landwatch.com/Inyo-County-California-Land-for-sale/pid/25031823
- based on source code, looks like PID unquely IDs listing across whole site, not just within county
- IDEA: pull all of the PIDs from a given page. Also record the county and state of the listing
       - then loop through each of the links
- once we get into the listing details we can look at aspects listed under "Property Features":
    - waterfront access
    - city
    - land type
    - road frontage/surface
    - trees
    - views
    - terrain
    - utility access
these will be critical to building any type of interesting model - since not all land is created equal, we only get
    so far with price per acre


LONG TERM:
- i think evenually it would be cool to build a model where we build a valuation of the property and then compare it to
    the listed price
- figure out if we can get data on past sales
- bring in zillow land listings
- incorporate other datsets: weather, distance to airports/highways, historical sales prices