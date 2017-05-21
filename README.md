# leet-o-clock
Twitter-celebrate leet o'clock every day with a random gif!

To use this, you must do the following steps:

1. pip3 install tweepy and safygiphy (make sure you're using python3!)

2. Go to https://apps.twitter.com, from here, make a new app.

3. Go to your 'Keys and Access Tokens', and generate yourself an access token pair.

4. Create a file in the same directory as 1337.py called 'keys.txt'. Copy and paste, line by line:

  `(line 1) your_consumer_key`

  `(line 2) your_consumer_secret`

  `(line 3) your_access_token`

  `(line 4) your_access_token_secret`

5. Add this to your crontab (if you don't have cron, install it) as:

  `37 13 * * * /path/to/1337.py`

6. Happy 1337 h4x0ring!
