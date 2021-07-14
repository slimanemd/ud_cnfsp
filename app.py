# python
from os.path import abspath, join as join_path, pardir
import git
import os

# 3rd party:
from flask import Flask
from flask import render_template

# instance_path
instance_path = abspath(join_path(abspath(__file__), pardir))

# assets
app = Flask(
    __name__,
    instance_path=instance_path,
    template_folder='templates'
)

# ==================================================================================================
# home


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", data='cnfsp')

# ==================================================================================================
# git

@app.route("/git", methods=['GET'])
def getgit01():
    return render_template("index.html", data='git')

# ==================================================================================================
# git

@app.route("/divers", methods=['GET'])
def divers():
    return render_template("index.html", data='divers')

# ===========================================================================
# webhook


@app.route("/update_server", methods=['POST'])
def webhook():
    repo = git.Repo('/home/slimanemd/udcnf')
    repo.remotes.origin.pull('main')

    app_loader = "/var/www/slimanemd_pythonanywhere_com_wsgi.py"
    os.system("touch " + app_loader)

    msg = "Updated site version successfully oh"
    return msg, 200

# ==================================================================================================
# main


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
