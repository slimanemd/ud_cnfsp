# python
from os.path import abspath, join as join_path, pardir
import git
import os

# 3rd party:
from flask import Flask
from flask import render_template

# instance_path
instance_path = abspath(join_path(abspath(__file__), pardir))

process_comments = True

# assets
app = Flask(
    __name__,
    instance_path=instance_path,
    template_folder='templates'
)

@app.template_filter()
def remove_comments(code):
    output = code
    if process_comments == True:
        lines = code.splitlines()
        lines_without_comments = [line for line in lines if not (line.__contains__("#") or line=="")]
        output = "\n" +  "\n".join(lines_without_comments)    # "" + ("\n".join(lines_without_comments)) + ""
    return output


@app.template_filter()
def randomis(code):
    import random
    output = str(random.randint(0,100))
    return output
# ==================================================================================================
# home


@app.route("/", methods=['GET'])
def index():
    yaml00 = {
   'vrs':
"""## Set the API endpoint used to create the Deployment resource.
apiVersion: apps/v1""",
   'kind' :
"""## Define the type of the resource.
kind: Deployment""",
   'metadata' :
"""## Set the parameters that make the object identifiable, such as its name, namespace, and labels.
metadata:
  annotations:
  labels:
    app: go-helloworld
  name: go-helloworld
  namespace: default""",
'spec':
"""## Define the desired configuration for the Deployment resource.
spec:
  ## Set the number of replicas.
  ## This will create a ReplicaSet that will manage 3 pods of the Go hello-world application.
  replicas: 3
  ## Identify the pods managed by this Deployment using the following selectors.
  ## In this case, all pods with the label `go-helloworld`.
  selector:
    matchLabels:
      app: go-helloworld
  ## Set the RollingOut strategy for the Deployment.
  ## For example, roll out only 25% of the new pods at a time.
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  ## Set the configuration for the pods.
  template:
    ## Define the identifiable metadata for the pods.
    ## For example, all pods should have the label `go-helloworld`
    metadata:
      labels:
        app: go-helloworld
    ## Define the desired state of the pod configuration.
    spec:
      containers:
        ## Set the image to be executed inside the container and image pull policy
        ## In this case, run the `go-helloworld` application in version v2.0.0 and
        ## only pull the image if it s not available on the current host.
      - image: pixelpotato/go-helloworld:v2.0.0
        imagePullPolicy: IfNotPresent
        name: go-helloworld
        ## Expose the port the container is listening on.
        ## For example, exposing the application port 6112 via TCP.
        ports:
        - containerPort: 6112
          protocol: TCP
        ## Define the rules for the liveness probes.
        ## For example, verify the application on the main route `/`,
        ## on application port 6112. If the application is not responsive, then the pod will be restarted automatically.
        livenessProbe:
           httpGet:
             path: /
             port: 6112
        ## Define the rules for the readiness probes.
        ## For example, verify the application on the main route `/`,
        ## on application port 6112. If the application is responsive, then traffic will be sent to this pod.
        readinessProbe:
           httpGet:
             path: /
             port: 6112
        ## Set the resource requests and limits for an application.
        resources:
        ## The resource requests guarantees that the desired amount
        ## CPU and memory is allocated for a pod. In this example,
        ## the pod will be allocated with 64 Mebibytes and 250 miliCPUs.
          requests:
            memory: "64Mi"
            cpu: "250m"
        ## The resource limits ensure that the application is not consuming
        ## more than the specified CPU and memory values. In this example,
        ## the pod will not surpass 128 Mebibytes and 500 miliCPUs.
          limits:
            memory: "128Mi"
            cpu: "500m" """
}


    ddd = """
## Define the desired configuration for the Deployment resource.
spec:
  ## Set the number of replicas.
  ## This will create a ReplicaSet that will manage 3 pods of the Go hello-world application.
  replicas: 3
  ## Identify the pods managed by this Deployment using the following selectors.
  ## In this case, all pods with the label `go-helloworld`.
  selector:
    matchLabels:
      app: go-helloworld"""

    import json, yaml
    response = app.response_class(
        response=json.dumps(yaml00),
        status=200,
        mimetype='application/json'
    )


    #def remove_comments_from_dict(code_dict):
    #    for key in code_dict.keys():
    #        code_dict[key] = remove_comments(code_dict[key])

    #return yaml00 #remove_comments(ddd)  # { "message" : yaml.dump(ddd, allow_unicode=True) }
    return render_template("index.html", data='cnfsp')

# ==================================================================================================
# git

@app.route("/drupal", methods=['GET'])
def getdrupal():
    return render_template("index.html", data='drupal')

# ==================================================================================================
# git

@app.route("/git", methods=['GET'])
def getgit():
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
