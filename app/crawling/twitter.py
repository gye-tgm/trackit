from app.models.user import User
from app.models.twitter.post import TwitterPost
from app.crawling import Crawler
from app.extensions import twitter_api


class TwitterCrawler(Crawler):
    """
    The TwitterCrawler is responsible for crawling Twitter posts that will automatically be stored into the database.

    To use the TwitterCrawler approriately, use the following code

        twitter_crawler = TwitterCrawler()
        twitter_crawler.crawl_all()
    """

    def crawl_user(self, user):
        """
        Crawls a certain number of posts from the given user's Twitter accounts and stores the data into the database.

        :param user: the user
        """
        for a in user.get_twitter_accounts():
            for tw in twitter_api.user_timeline(a.username):
                if TwitterPost.query.filter_by(tw_id=tw.id).count() == 0:
                    TwitterPost.create(content=tw.text,
                                       time=tw.created_at,
                                       user_id=user.id,
                                       tw_id=tw.id)

    def crawl_all(self):
        """
        Crawls all user in the database.
        """
        for u in User.query.all():
            self.crawl_user(u)