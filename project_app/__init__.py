from flask import Flask
application = Flask(__name__)
application.secret_key = "shhhhhh"
UPLOAD_FOLDER = 'upload_folder/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
application.config['UPLOAD_PATH'] = UPLOAD_FOLDER
application.config['UPLOAD_EXTENSIONS'] = ALLOWED_EXTENSIONS
application.config['MAX_CONTENT_LENGTH'] = 2048 * 2048
