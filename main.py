from flask_openapi3 import Info, OpenAPI

import db as db
from api.tasks_api import tasks_api
from pages.tasks_page import tasks_page

info = Info(title="Tasks API", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.register_blueprint(tasks_page)
app.register_api(tasks_api)

if __name__ == "__main__":
    db.create_database()
    app.run(debug=True)
