__author__ = 'Xun'

import pandas as pd
import re

tweets = pd.read_csv('tweets.csv')

print type(tweets)

# Extract the Tweet Body Column out #
textCont = pd.Series(tweets['body'])


# Process the content and create more column #
# Generate two variable IsRT & FwdFrom #
proTweets = list(range(10000))
IsRT = list(range(10000))
FwdFrom = list(range(10000))
i=0
for tweet in textCont:
    proTweets[i] = (tweet.strip())

    # Confirm RT status, YES - '1' NO - '0' #
    if proTweets[i].__contains__('RT'):
        IsRT[i] = 1
        # Remove RT tag #
        proTweets[i] = proTweets[i].replace('RT','',1).strip()
        # Extract Forwarding Source #
        regex = ur'@\w*:'
        match = re.search(regex,proTweets[i])
        if match:
            FwdFrom[i] = match.group()[:-1]
        else:
            FwdFrom[i] = "Unknown"
    else:
        IsRT[i] = 0

    # Clean up the Tweet #
    regex = ur'@\w*:' #Clean forwarder #
    proTweets[i] = re.sub(regex, '', proTweets[i]).strip()
    regex = ur'@\w*\b' #Clean other connection
    proTweets[i] = re.sub(regex, '', proTweets[i]).strip()
    regex = ur'\bi\b' # Force big case of i
    proTweets[i] = re.sub(regex, 'I', proTweets[i]).strip()
    regex = ur'http.*\b' # Force big case of i
    proTweets[i] = re.sub(regex, '', proTweets[i]).strip()
    i=i+1


for i in range(0,100):
    print proTweets[i]

print proTweets[99]
