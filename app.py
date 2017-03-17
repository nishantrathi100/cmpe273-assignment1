from flask import Flask
from github import Github

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"


@app.route("/v1/<filename>")
def getConfigFile(filename):
	gitClient = Github();
	gitRepo = gitClient.get_repo('');
	file_content = repo.get_file_contents(removeExtension(name)+'.yml');
	return file_content;
	

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')