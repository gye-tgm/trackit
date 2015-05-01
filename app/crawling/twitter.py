from app.models.user import User
from app.models.twitter.post import TwitterPost
from app.crawling import Crawler
from app.extensions import twitter_api


class TwitterCrawler(Crawler):
    def crawl_user(self, user):
        for a in user.get_twitter_accounts():
            for tw in twitter_api.user_timeline(a.username):
                if TwitterPost.query.filter_by(tw_id=tw.id).count() == 0:
                    TwitterPost.create(content=tw.text,
                                       time=tw.created_at,
                                       user_id=user.id,
                                       tw_id=tw.id)

    def crawl_all(self):
        for u in User.query.all():
            self.crawl_user(u)