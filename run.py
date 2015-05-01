#!/usr/bin/env python
from app import create_app
app = create_app('config.BaseConfiguration')
#app.run(debug=True, use_reloader=False, use_debugger=False)
app.run(debug=True)
