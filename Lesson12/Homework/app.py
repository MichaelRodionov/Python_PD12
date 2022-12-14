from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

posts = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)
