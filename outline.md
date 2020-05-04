# IA626 Final Project
###### By: Grace De Geus
### Data Sources:
-Reddit
### API and Code used
https://www.reddit.com/dev/api/
https://praw.readthedocs.io/en/latest/
https://pythonprogramming.net/introduction-python-reddit-api-wrapper-praw-tutorial/
https://pythonprogramming.net/parsing-comments-python-reddit-api-wrapper-praw-tutorial/?completed=/introduction-python-reddit-api-wrapper-praw-tutorial/

## Project Summary
General starting point: How much misinformation on the COVID-19 pandemic is being shared on social media?

Due to the current global pandemic of COVID-19 there has been an obvious spike in information regarding viruses, including their mortality rate, infection mechanisms, number and rate of new cases, and how local, state, national, and global communities and governments have reacted to the pandemic. I am interested in trying to determine how much misinformation is being spread on social media. I have heard the spread of misinformation described as an "infodemic". The misinformation being shared most likely plays a role in the spread of the disease itself. I am looking to pull data from Reddit, which has a very well moderated caronavirus subreddit. I'd like to compare this to data pulled from other coronavirus related subreddits, and to the overall Reddit forum as a whole.
### Overview

### Approach
My approach for this started with an investigation into how to retrieve comment information from Reddit. Thankfully Reddit has a readilly available API; just sign up with an account, register with the site the desire to create a script, app, or bot, and receive API credentials.

Now, working with an API might be pretty straightforward, but the Reddit community (where it intersects with the programming community) has developed a wrapper for this API to make it even easier. The Python Reddit API Wrapper (PRAW) aims to be as easy to use as possible, but the main advantage is that the wrapper is designed to follow all of reddit's API rules. These rules are a little extensive and, without keeping each in mind when programming, it wouldn't be very hard to break them. The added peace of mind that comes from the wrapper is greatly appreciated. As such, I only briefly consulted the Reddit API and referenced the PRAW website almost exclusively.

In order to utilize PRAW, one has to import it:
```python
import praw,json,csv,datetime,time
```
I also imported json and csv in order to output data to text and csv files for later analysis. Datetime was imported to manipulate the date/time for each submission and comment retrieved from each subreddit. Time was imported to allow me to time how long the script takes to run (hint: it's a long time).

Next, the most important thing to do is create a Reddit instance. I followed the 'Introduction to Python Reddit API Wrapper PRAW Tutorial' (linked above). This requires a Client ID, Client Secret, Username, Password, and User Agent. The Username, Password, and User Agent are required to be given when requesting API access on the Reddit website, and the Client ID and Client Secret are provided when that access is granted (I have redacted the sensitive information in the code snippet below). 
```python
reddit = praw.Reddit(client_id = 'xxx', client_secret = 'xxx', username = 'Ia626_Final', password = 'xxx', user_agent = 'IA626')
```





### Outline:
- ETL (How did I fetch and store source data, outlined and repeatable. How did I decide on storage format?)
- Determine what data is relevant
- Determine how to gather relevant data
- Extract relevant data from multiple sources
- Perform necessary filtering/transformation on data
- Perform ANOVA
- Analyze results
- Document data processing steps
- 

 ### Hypothesis: 
 There are more posts removed due to misinformation in the coronavirus related subreddits than in the general forum.
 
 ---
 ## Data Collection
 ##### Load Libraries
 
 ##### Access Reddit API
 
 OUTLINE DO ALL THE THINGS, explain code
 
 Provide output data sample
 Distribution of sample
 
 
 ### Conclusions:
