import os
from flask import Flask

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'scorekeeper.db'),
    SECRET_KEY='\xa8\xf1\x9ai\xca\x1b\xe5izr\xd0\xf5K\xe3\xa0\x9e]EJm\xe5N\x08+',
    DEBUG=False,
))
app.config.from_envvar('SCOREKEEPER_SETTINGS', silent=True)

#for use on nginx
#if ( app.debug ):
#    from werkzeug.debug import DebuggedApplication
#    app.wsgi_app = DebuggedApplication( app.wsgi_app, True )

import scorekeeper.views
import scorekeeper.api