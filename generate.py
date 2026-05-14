from github import Github
import base64

ACCESS_TOKEN = '#'
REPO_NAME = 'tyauk/conditions-report'
FILE_PATH = 'test.jpg'
LOCAL_IMAGE_PATH = 'test.jpg'

def replace_github_image():
	g = Github(ACCESS_TOKEN)
	repo = g.get_repo(REPO_NAME)

	#GET THE EXISTING FILE DATA TO RETRIEVE ITS SHA (REQUIRED FOR UPDATES)
	contents = repo.get_contents(FILE_PATH)

	#READ THE NEW LOCAL IMAGE AS BINARY
	with open(LOCAL_IMAGE_PATH, "rb") as image_file:
		new_content = image_file.read()

	#UPDATE THE FILE IN THE REPOSITORY
	repo.update_file(
		path=FILE_PATH,
		message="Automated image update via Python",
		content=new_content,
		sha=contents.sha,
		branch="main"
		)
	print(f"Successfully replaced {FILE_PATH}")

if __name__ == "__main__":
	replace_github_image()