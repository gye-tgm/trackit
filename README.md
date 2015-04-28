Preparing for the FT Matura
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

Notes: 
* `Admin` page can only be accessed by admins obviously. 
* If you delete your own account while being logged in, you will get logged out
  in a fatal way.  


Coming up:
* `app/constants.py`
* `templates/404` or `templates/base.html`
* An appropriate `.gitignore` file (for Python, Sphinx, however, no LaTeX)
* More packages
* Unit-testing
* Integration-testing via Mockups

