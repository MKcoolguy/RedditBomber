from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()


start_time = int(datetime.datetime(2019, 1, 1).timestamp())

submissions = api.search_submissions(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 10)


comments = api.search_comments(after=start_time,
                                    subreddit='asktrp',
                                    filter=['url','author', 'title', 'subreddit'], limit = 10)

'''
for submission in submissions:
    #print(submissions)
    print(submission.created_utc)
    print(submission.title)
    print(submission.url)
    print(submission.author)
    print(submission.q)
    '''


for comment in comments:
    print(comment)
