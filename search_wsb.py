from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()


start_time = int(datetime.datetime(2019, 1, 1).timestamp())

submissions = api.search_submissions(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 10)


comments = api.search_comments(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 20)

'''
for submission in submissions:
    #print(submissions)
    print(submission.created_utc)
    print(submission.title)
    print(submission.url)
    print(submission.author)
    print(submission.q)
    '''


#All found usernames are written to new text file Users.txt
users = open("Users.txt","w")

#A set to prevent duplicate duplicates from writing to the file
usersSet = {""}

#Searches all comment authors and adds to set
for comment in comments:
    if comment.author != "[deleted]":
        usersSet.add(comment.author)

#Writes to text file
for user in usersSet:
    users.writelines(user + "\n")
