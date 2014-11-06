import sys
from scorekeeper import app, db_access

if len(sys.argv) > 1 and 'initdb' in sys.argv:
    db_access.init_db()
else:
    app.run(host='0.0.0.0', port=5000, debug=True)