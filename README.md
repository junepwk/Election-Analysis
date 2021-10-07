# PyPoll with Python

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview-of-project">Overview of Project</a>
    </li>
    <li>
      <a href="#resources">Resources</a>
    </li>
    <li>
       <a href="#election-audit-results">Election Audit Results</a>
    </li>
    <li>
       <a href="#election-audit-summary">Election Audit Summary</a>
    </li>
  </ol>
</details>

## Overview of Project
Tom, an employee of Colorado Board of Elections, had requested the following data for an election audit analysis:
1. Total number of votes casted
2. A complete list of candidates who received votes
3. Total number of votes for each candidate
4. The percentage of votes each candidate won
5. Determine the winner  of the election based on popular vote
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout


## Resources
- Data Source: election_results.csv
- Software: Python 3.9.5, Visual Studio Code 1.56.2

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.

- The county results were:
   - Jefferson: 10.5% (38,855 votes)
   - Denver: 82.8% (306,055 votes)
   - Arapahoe: 6.7% (24,801 votes)

- Largest county turnout:
   - **Denver** had the largest number of votes. 

* The candidates were:
   * Charles Casper Stockham
   * Diana DeGette
   * Raymon Anthony Doane
   
* The candidate results were:
   * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
   * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
   * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

* The winner of the election was: 
   * **Diana DeGette**, who received 73.8% of the vote and 272,892 number of votes.


## Election Audit Summary
The core of this script could be applied to not only the US congressional state precinct elections, but also larger scale elections like the Electoral College.  This would require a prodigious refactoring of the original script.  Similar to the lists and dictionaries created to store candidate and county informations, adding a list and dictionary to store states' information would broaden the code's capability for future use.  Additionally, the same steps could be done for each political parties.  By building onto the ordered steps in the original script, the possibilites are endless.

```Python
#Example codes that could be utilized
#Create a state list and state vote dictionary
state_list = []
state_votes = {}

#Track the winning elector and vote count
winning_elector = ""
electoral_votes = 0
```
