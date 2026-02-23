# Web-scraping-itsay-awards
Project Overview
This project was born from a personal curiosity: *Does the critical acclaim of the series "I Told Sunset About You" match the data?* I developed a Python script to automate the extraction of award data directly from Wikipedia. This project demonstrates my ability to handle "messy" web data and transform it into a clean, visual representation.

##  Tech Stack
* *Python 3.x*
* *Pandas*: For data manipulation and HTML table parsing.
* *Requests & BeautifulSoup*: To handle web connectivity and bypass basic scraping blocks.
* *Matplotlib*: To generate the final visual insights.

##  Key Challenges Overcome
* *MultiIndex Tables*: Wikipedia tables often use nested headers. I implemented logic to "flatten" these levels using .get_level_values(-1).
* *Dynamic Column Selection*: Instead of hardcoding indices, the script searches for the "Result" column using case-insensitive string matching, making it more robust to minor Wikipedia edits.

##  Result
The script generates a bar chart showing the distribution of Wins, Nominations, and Pending results, providing a clear snapshot of the show's impact.

<img width="1411" height="924" alt="image" src="https://github.com/user-attachments/assets/bde1a7b8-e18d-4461-b894-c2153c1c75d0" />
