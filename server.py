from project_app import application
from project_app.controllers import users, posts, channels

if __name__ == "__main__":
    application.run(debug=True)
