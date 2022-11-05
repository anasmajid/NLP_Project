#Import Libraries
import snscrape.modules.twitter as sntwitter
import emoji

def scrape_ui(
    tweet_limit = 12,
    tags = ["Senate", "Senator", "US", "Midterms", "Fetterman", "Democrat", "Republican", "GOP", "Pennsylvania","stroke", "dog", "America", "vote"]
    ):
    
    #Democrats 
    query1= "#johnfetterman until:2022-10-11 since:2022-08-11"
    query2 = "#fetterman until:2022-10-11 since:2022-08-11"
    query3 = "#VoteFetterman until:2022-10-11 since:2022-08-11"

    #Republicans
    query4 = "#VoteOz until:2022-10-11 since:2022-08-11"
    query5 = "#OZ until:2022-10-11 since:2022-08-11"
    query6 = "#Pennsylvania #Oz until:2022-10-11 since:2022-08-11"

    queries_list = [query1, query2, query3, query4, query5, query6]

    tweets =[]
    tweets_meta =[]
    usernames = []
    otherTags = tags
    num_tweets_limit = tweet_limit

    for query in queries_list:
        limit_per_query = num_tweets_limit / len(queries_list)
        tweet_counter = 0
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if tweet_counter == limit_per_query:
                break

            else:
                if tweet.user not in usernames:
                    if emoji.emoji_count(tweet.rawContent) ==0:
                    #ensure at least one other tag is inside tweet, ensure tweet is within subject
                        for tag in otherTags:
                            if tag in tweet.rawContent:
                                tweets_meta.append([tweet.date, tweet.rawContent, tweet.id, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.conversationId, tweet.retweetedTweet, tweet.quotedTweet, tweet.inReplyToTweetId, tweet.inReplyToUser, tweet.mentionedUsers])
                                tweets.append(tweet.rawContent)
                                usernames.append(tweet.user)
                                tweet_counter+=1
                                break

    print(tweets)
    ret = str()
    for tweet in tweets:
        ret = tweet + "\n" + ret
    return ret

    # return tweets