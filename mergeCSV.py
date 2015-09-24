__author__ = 'Xun'

fout = open('tweets.csv','a')

for line in open("HalloweenTweetData/tweet_001.csv"):
    fout.write(line)

for docnm in range(2,101):
    f = open('HalloweenTweetData/tweet_{:03}.csv'.format(docnm))
    f.next()
    for line in f:
        fout.write(line)
    f.close()

fout.close()