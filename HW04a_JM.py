"""
@author- Jigar Masekar

Code for HW04a

"""

import requests
import json


def rep_checker(user_id):
    url = 'https://api.github.com/users/'+user_id+'/repos'
    html = requests.get(url)
    loaded_json = json.loads(html.text)
    repos = []
    for x in loaded_json:
        if "name" in x:
            repos.append([x["name"]])
    for i in repos:
        url = "https://api.github.com/repos/"+user_id+"/"+i[0]+"/commits"
        html = requests.get(url)
        loaded_json = json.loads(html.text)
        commit = 0
        for x in loaded_json:
            if "commit" in x:
                commit = commit + 1
        i.append(commit)
    return repos


def result(repos):
    for i in repos:
        print(f"Repo: {i[0]} Number of commits: {i[1]}")
    print(repos)


def main():
    user_id = input("Enter GitHub user ID: ")
    repos = rep_checker(user_id)
    result(repos)


if __name__ == "__main__":
    main()
