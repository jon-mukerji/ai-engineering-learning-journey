
import requests
print("========================================")
print("🔎 GITHUB PROFILE FINDER")
print("========================================")
username = input("Enter the Github username: ")
print("----------------------------------------")


def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout = 10)
    except requests.RequestException:
        print("Network error. Please check your connection and try again.")
        return None

    if response.status_code == 200:
        data = response.json()
        print("Profile Found!!")
        print('----------------------------------------')
        profile_info = {
            "Name": data['name'],
            "Username": data['login'],
            "Bio": data['bio'] if data['bio'] is not None else "No bio available",
            "Location": data['location'] if data['location'] is not None else "No location available",
            "Public Repos": data['public_repos'],
            "Followers": data['followers'],
            "Following": data['following'],
            "Profile URL": data['html_url']
            }
        return profile_info

    elif response.status_code == 404:
        print("Profile not found. Please check the username and try again.")
        return None
    else:
        print(f"Error: {response.status_code}, Something went wrong!!")
        return None

def display_profile(profile_info):
    print(f"Name: {profile_info['Name']}")
    print(f"Username: {profile_info['Username']}")
    print(f"Bio: {profile_info['Bio']}")
    print(f"Location: {profile_info['Location']}")
    print(f"Public Repos: {profile_info['Public Repos']}")
    print(f"Followers: {profile_info['Followers']}")
    print(f"Following: {profile_info['Following']}")
    print(f"Profile URL: {profile_info['Profile URL']}")

profile = get_github_profile(username)

if profile is not None:
    display_profile(profile)