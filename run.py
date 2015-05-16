#!/usr/bin/env python
from app import create_app
from app.config import BaseConfiguration
app = create_app(BaseConfiguration)
#app.run(debug=True, use_reloader=False, use_debugger=False)
app.run(debug=True, host='0.0.0.0')
