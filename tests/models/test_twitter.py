import unittest

from app.crawling.twitter import TwitterCrawler
from app.models import User, TwitterAccount
from app.extensions import twitter_api
from tests.test_base import BaseTestCase


class TwitterCrawlerTest(BaseTestCase):
    """
    Those tests will be skipped since we are using the API keys...
    """
    @unittest.skip("Not enough API calls")
    def test_crawl(self):
        u1 = User.create(username='gary')
        u1.accounts.append(TwitterAccount(username='GaryYe13'))
        u1.save()
        t = TwitterCrawler()
        t.crawl_user(u1)
        self.assertGreater(len(list(u1.posts)), 1)

    @unittest.skip("Not enough API calls")
    def test_twitter(self):
        new_tweets = twitter_api.user_timeline('GaryYe13')
        for tw in new_tweets:
            print(tw.text)

if __name__ == '__main__':
    unittest.main()
