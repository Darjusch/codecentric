#!/usr/bin/python


# All members:
# https://api.github.com/orgs/codecentric/members

# Repos of a member:
# https://api.github.com/users/danielschleindlsperger/repos

# Languages used in one Repo:
# https://api.github.com/repos/danielschleindlsperger/adventofcode2022/languages


import sqlite3
import requests


github_token = False
if not github_token:
    raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN in setup.py")


conn = sqlite3.connect('codecentric.db')
print("Opened database successfully")

url = 'https://api.github.com/orgs/codecentric/members'
headers = {'Authorization': 'token {github_token}'}

response = requests.get(url, headers=headers)
members = response.json()

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, login TEXT UNIQUE)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS repositories (id INTEGER PRIMARY KEY, name TEXT UNIQUE, member_id INTEGER, FOREIGN KEY (member_id) REFERENCES Members (id))''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repo_id INTEGER,
    language TEXT,
    FOREIGN KEY (repo_id) REFERENCES Repositories (id))''')

print("This can take a while, please wait...")
for member in members:
    print("Inserting data for member: ", member)
    cursor.execute('INSERT OR IGNORE INTO Members (id, login) VALUES (?, ?)', (member['id'], member['login']))
    repos_url = member['repos_url']
    repos_response = requests.get(repos_url, headers=headers)
    repos = repos_response.json()
    for repo in repos:
        cursor.execute('INSERT OR IGNORE INTO Repositories (id, name, member_id) VALUES (?, ?, ?)',
                       (repo['id'], repo['name'], member['id']))
        
        languages_url = repo['languages_url']
        languages_response = requests.get(languages_url, headers=headers)
        languages = languages_response.json()

        for language in languages.keys():
            cursor.execute('INSERT INTO Languages (repo_id, language) VALUES (?, ?)', (repo['id'], language))
print("Data inserted successfully")
conn.commit()
conn.close()