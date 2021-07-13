# python
from os.path import abspath, join as join_path, pardir
import git


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
#
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")  #tree01

# ===========================================================================
# webhook
@app.route("/update_server", methods=['POST'])
def webhook():
    def callGitOriginPul():                   #import os
        repo = git.Repo('')
        origin = repo.remotes.origin
        origin.pull()                         #os.system('/var/www/aliben_pythonanywhere_com_wsgi.py')
        return "Updated site version successfully it is a test"

    msg =  callGitOriginPul() #if request.method == 'POST' else 'Wrong event type'
    return msg, 200 #HttpResponse(msg, status=200 if request.method == "POST" else 400)

# ==================================================================================================
#
if __name__ == "__main__":
    app.run(host='0.0.0.0' ,debug=True, port=5001)