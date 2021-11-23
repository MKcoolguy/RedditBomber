from psaw import PushshiftAPI
import datetime
import praw
import threading
import re


api = PushshiftAPI()

#Edit start date for searched posts here
start_time = int(datetime.datetime(2021, 6, 25).timestamp())

#Variable to store all submissions and posts
submissions = api.search_submissions(after=start_time,
                                    subreddit='NameHere', #Insert subreddit name
                                    filter=['url','author', 'title', 'subreddit'], limit = 20)

#All found usernames are written to new text file Users.txt
users = open("Users.txt","w")

#Usernames to avoid adding to the set
blockedUsersSet = {""}
with open("restrictedUsers.txt") as file:
    while (line := file.readline().rstrip()):
        blockedUsersSet.add(line)

#A set of users to prevent duplicates from writing to the file
usersSet = {""}
#A set for links to each thread
linksSet = {""}

#Searches all post authors and adds to set
for submission in submissions:
    if submission.author not in blockedUsersSet:
        usersSet.add(submission.author)
        linksSet.add(submission.url)

#Reddit API credentials
reddit = praw.Reddit(
    client_id="", #Insert client ID
    client_secret="", #Insert secret ID
    password="", #Insert account password
    user_agent="agent", 
    username="", #Insert username
)

#Searches each post for comment authors and adds to set
for link in linksSet:
    if link != "":
        url = link
        submission = reddit.submission(url=url)
        for top_level_comment in submission.comments:
            name = str (top_level_comment.author)
            re.findall(r"'([^']+)'", name)
            if name not in blockedUsersSet:
                usersSet.add(name)
            

#Writes users to text file
for user in usersSet:
    users.writelines(user + "\n")


#Message users
for user in usersSet:
    if (user != ""):
        try:
            reddit.redditor(user).message("Message Title Here", "Message body") #Insert Message 
            print("Message sent to: " + user)
        except praw.exceptions.RedditAPIException:
            print("Exceeded DM Limit. Resting for 60 seconds before trying again")
            time.sleep(60)



print("Script Executed Sucessfully")