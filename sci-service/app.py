from flask import Flask, request, jsonify
import os
import git
app = Flask(__name__)


@app.route('/push', methods=['POST'])
def github_push_webhook():
    branch_name = str(request.get_json().get("ref", "")).replace("refs/heads/", "")
    if branch_name not in app.config["branches"]:
        return jsonify({"status": 404}), 404      
    path_to_env = app.config['branches'][branch_name]
    if not os.path.isfile(f"{path_to_env}/.git/HEAD"):
        git.Repo.clone_from(app.config["repo"], path_to_env, branch=branch_name)
    else:
        repo = git.Repo(path_to_env)
        repo.git.checkout(branch_name)
        repo.remotes.origin.pull()
    os.system(f"chown -R {app.config['apache_user']}: {path_to_env}")
    return jsonify({"status": 200}), 200