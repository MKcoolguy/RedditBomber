from psaw import PushshiftAPI
import datetime
import praw
import threading



api = PushshiftAPI()
start_time = int(datetime.datetime(2019, 1, 1).timestamp())

submissions = api.search_submissions(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 100)


comments = api.search_comments(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 100)

#All found usernames are written to new text file Users.txt
users = open("Users.txt","w")

#Usernames to avoid adding to the set
blockedUsersSet = {""}
with open("restrictedUsers.txt") as file:
    while (line := file.readline().rstrip()):
        blockedUsersSet.add(line)

#A set to prevent duplicates from writing to the file
usersSet = {""}

#Searches all post authors and adds to set
for submission in submissions:
    if submission.author not in blockedUsersSet:
        usersSet.add(submission.author)

#Searches all comment authors and adds to set
for comment in comments:
    if comment.author not in blockedUsersSet:
        usersSet.add(comment.author)

#Writes users to text file
for user in usersSet:
    users.writelines(user + "\n")
'''
#API credentials
reddit = praw.Reddit(
    client_id="aMDdLPzpiQ1rVTWpaCg7PQ",
    client_secret="7BGwl2oOSgq8-js7K4Jm75cCaJtr2A",
    password="matteo11",
    user_agent="USERAGENT",
    username="LifeExposed",
)

#message users
for user in usersSet:
    if (user != ""):
        reddit.redditor(user).message("The New r/asktrp!",
         "**##Hello!** we have decided to start a new community at **#r/askrp** to replace r/asktrp. **Please come join us at #r/askrp** so we can have an **##active community!**")

'''

print("Application executed successfully")