'''
 Made by Luthpai ( Luthfi Afriansyah )
 GitHub : luthpai
 MIT License 2023©
 You are able to modify
 You are able to distribute or sell
 I'm not liable and responsible of everything
 Thanks :•D
'''

import requests

import sys
sys.tracebacklimit=0

# GitHub API base url
url = "https://api.github.com/users"

# Ask user to input username
search_input = input("Input username: ")

# Check if user has inputted username
if search_input:
	profile = requests.get(f"{url}/{search_input}")

# Turn the profile result to JSON
profile = profile.json()

# Check if user is found
# By checking "login" in the profile result
if "login" in profile:
  # If the profile is found then
  # Declare a new variable with the profile data from the result
  profile_data = f"""\n
    username: {profile['login']}
    name: {profile['name']}
    link: {profile['blog']}
    bio: {profile['bio']}
    location: {profile['location']}
    followers: {profile['followers']}
    following: {profile['following']}
    repositories: {profile['public_repos']}
  """
  # Print the data
  print(profile_data)
else:
	# print User not found if "login" is not found
	print("\n User not found.")
