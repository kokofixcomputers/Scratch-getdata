import requests

class ScratchAPIClient:
    def __init__(self):
        print("If you use GetData please credit @kokofixcomputers")
        self.base_url = "https://scratch-get-data.kokoiscool.repl.co"

    def get_follower_count(self, username):
        url = f"{self.base_url}/get/follower-count/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the follower count as a string

    def is_scratcher(self, username):
        url = f"{self.base_url}/get/is_scratcher/{username}/"
        response = requests.get(url)
        return response.text.strip().lower() == "true"  # Return True or False based on the response

    def get_following_count(self, username):
        url = f"{self.base_url}/get/following-count/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the following count as a string

    def get_wiwo(self, username):
        url = f"{self.base_url}/get/wiwo/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the WiWo as a string

    def get_about_me(self, username):
        url = f"{self.base_url}/get/aboutme/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the About Me text as a string

    def get_messages(self, username):
        url = f"{self.base_url}/get/messages/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the Messages as a string

    def get_project_creator(self, project_id):
        url = f"{self.base_url}/get/project/creator/{project_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the project creator username as a string

    def get_project_name(self, project_id):
        url = f"{self.base_url}/get/project/name/{project_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the project name as a string

    def get_project_description(self, project_id):
        url = f"{self.base_url}/get/project/notes_and_credits/{project_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the project description as a string

    def get_project_instructions(self, project_id):
        url = f"{self.base_url}/get/project/instructions/{project_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the project instructions as a string

    def get_project_blocks(self, project_id):
        url = f"{self.base_url}/get/project/blocks/{project_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the project blocks as a string

    def get_forum_title(self, post_id):
        url = f"{self.base_url}/get/forum/title/{post_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the forum post title as a string

    def get_forum_category(self, post_id):
        url = f"{self.base_url}/get/forum/category/{post_id}/"
        response = requests.get(url)
        return response.text.strip()  # Return the forum post category as a string

    def get_scratch_user_country(self, username):
        url = f"{self.base_url}/get/user/country/{username}/"
        response = requests.get(url)
        return response.text.strip()  # Return the Scratch user's country as a string

