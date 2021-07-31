# ==========================================================
# imports
# python
from os.path import abspath, join as join_path, pardir

# 3rd party:
from flask import Flask, redirect, render_template, request

# my libs
from git_webhook import webhook #import git #import os

# ==========================================================
# varaibles
instance_path = abspath(join_path(abspath(__file__), pardir))
#process_comments = False

# application
app = Flask(
    __name__,
    instance_path=instance_path,
    template_folder='templates'
)

# ==========================================================
# jinja templates
# process_comments = True


# remove comments
@app.template_filter()
def remove_comments(code):
    process_comments = False
    if 'wc' in request.args.keys(): process_comments = True

    output = code
    if process_comments == False:
        lines = code.splitlines()
        lines_without_comments = [line for line in lines if not (line.__contains__("#") or line=="")]
        output = "\n" +  "\n".join(lines_without_comments)    # "" + ("\n".join(lines_without_comments)) + ""
    return output


# randomis
@app.template_filter()
def randomis(code):
    import random
    output = str(random.randint(0,100))
    return output


# ==================================================================================================
# Endpoints

# home
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", data='cnfsp')  #getItem()


# getItem
@app.route("/sec/<item>", methods=['GET'])
def getItem(item='cnfsp'):
    if not item in ['drupal', 'cnfsp', 'git', 'divers', 'others']:
        return redirect("/", code=302)
    return render_template("index.html", data=item)


# webhook
@app.route("/update_server", methods=['POST'])
def update_server_from_gitwh():
    return webhook()

# ==================================================================================================


# main
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
