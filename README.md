Trackit
=======

What is it?
-----------

Nowadays, we have too many social media accounts. 

Using this tool, a user can follow all updates of another user with just this single page. 

What's included?
----------------------------
* A user can track many users, and a user can be tracked by many users. (Many-to-many relationships + Association object, we save a `following_since` variable on purpose)
* The user has multiple accounts, e.g., Twitter, Facebook, ... (One-to-many relationships)
* We use **inheritance**, as the accounts can differ on multiple aspects (`TwitterAccount`, `FacebookAccount`). 
* A **strategy pattern** will be used to get the appropriate content (Facebook, Twitter)
* However, testing with genuine data can only happen with an internet connection, thus we'll use *mock objects* and *unit tests*. 
* An **observer pattern** will be used to notify the user.


How to install this project
===========================

Use `virtualenv` so we can work independently from other projects. For
instance:

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
```

The following command should install all the dependencies this project
requires.

```
pip -r install requirements.txt
```

Creating the database is not hard:
```
(venv) > python
>>> from app import db
>>> db.create_all()
```

The `scripts/helper.py` script might also be helpful

Notes: 
* `Admin` page can only be accessed by admins obviously. 
* If you delete your own account while being logged in, you will get logged out
  in a fatal way.  

Coming up
==========

* `templates/404`
* An appropriate `.gitignore` file (for Python, Sphinx, however, no LaTeX)
* Find some fixed version for the packages
* Unit-testing
* Integration-testing via Mockups (for Twitter, ...) 

Excellent resources:
* https://github.com/mitsuhiko/flask/wiki/Large-app-how-to (Founder of Flask) 
* https://realpython.com/blog/python/python-web-applications-with-flask-part-ii/ (Realpython Tutorial) 
* https://www.safaribooksonline.com/library/view/flask-web-development/9781491947585/ch04.html

Helpful projects: 
* https://github.com/reddit/reddit/tree/master/r2/r2

