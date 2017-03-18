from flask import Flask
from flask import jsonify
from github import Github
import sys

app = Flask(__name__)
gitRepoURL=''

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"


@app.route("/v1/<filename>")
def getConfigFile(filename):
	gitClient = Github();
	gitRepo = gitClient.get_repo(gitRepoURL);
	file_content = gitRepo.get_file_contents(filename);
	return file_content.decoded_content;
	

if __name__ == "__main__":
    gitRepoURL = sys.argv[1].replace('https://github.com/','')
    app.run(debug=True,host='0.0.0.0')