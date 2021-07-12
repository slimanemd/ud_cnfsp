# python
from os.path import abspath, join as join_path, pardir

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

# ==================================================================================================
#
if __name__ == "__main__":
    app.run(host='0.0.0.0' ,debug=True, port=5001)