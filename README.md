# RedditBomber
A script that compiles a list of authors from posts and comments on a specified subreddit then sends a mass message to those users.

# How to Use:
1. Add usernames you would like to avoid messaging in the restrictedUsers text file
2. Edit start time if you wish. This will only search for posts after the specified date
3. Insert subreddit name in the submissions variable
4. Edit number of posts you wish to go through in the submission's limit variable. Default is set to 20, but I do not recommended setting it to over 250 because pushShiftAPI will not be able to handle more. 
5. Add reddit api info to the reddit variable. https://www.reddit.com/prefs/apps
6. Script is ready to run
