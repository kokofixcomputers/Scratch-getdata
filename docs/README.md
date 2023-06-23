ScratchAPIClient Documentation
=============================

Introduction
------------
The ScratchAPIClient class provides a convenient interface for accessing data from the Scratch API using the "https://scratch-get-data.kokoiscool.repl.co" base URL.

Usage
-----
1. Instantiating the ScratchAPIClient class:
client = ScratchAPIClient()


2. Retrieving the follower count of a user:
follower_count = client.get_follower_count(username)


3. Checking if a user is a Scratcher:
is_scratcher = client.is_scratcher(username)


4. Retrieving the following count of a user:
following_count = client.get_following_count(username)

5. Retrieving the "What I'm Working On" (WIWO) status of a user:
wiwo_status = client.get_wiwo(username)


6. Retrieving the "About Me" information of a user:
about_me = client.get_about_me(username)


7. Retrieving the messages of a user:
messages = client.get_messages(username)


8. Retrieving the creator of a project:
project_creator = client.get_project_creator(project_id)


9. Retrieving the name of a project:
project_name = client.get_project_name(project_id)


10. Retrieving the description of a project:
project_description = client.get_project_description(project_id)


11. Retrieving the instructions of a project:
project_instructions = client.get_project_instructions(project_id)


12. Retrieving the blocks of a project:
project_blocks = client.get_project_blocks(project_id)


13. Retrieving the title of a forum post:
forum_title = client.get_forum_title(post_id)


14. Retrieving the category of a forum post:
forum_category = client.get_forum_category(post_id)


15. Retrieving the country of a Scratch user:
user_country = client.get_scratch_user_country(username)


Note: Replace `username` with the desired Scratch username and `project_id` with the desired project ID.

API website: https://scratch-get-data.kokoiscool.repl.co

Credits
-------
If you use GetData, please credit @kokofixcomputers.
