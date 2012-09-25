class TweetFirehose(threading.Thread):
    import urllib2
import base64
def run(self):
    status_sample_url = 'http://stream.twitter.com/1/statuses/sample.json'
request = urllib2.Request(status_sample_url)
# Be sure to use your own twitter login information
auth_basic = base64.encodestring('USERNAME:PASSWORD')[:-1]
request.add_header('Authorization', 'Basic %s' % auth_basic)
# open the connection
firehose = urllib2.urlopen(request)
for tweet in firehose:
    if len(tweet) > 2:
    tweetQueue.put(tweet)
firehose.close()