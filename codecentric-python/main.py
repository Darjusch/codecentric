import sqlite3

def find_developer_by_language(language):
    conn = sqlite3.connect('codecentric.db')
    cursor = conn.cursor()
    
    query = '''
    SELECT Members.login
    FROM Members
    JOIN Repositories ON Members.id = Repositories.member_id
    JOIN Languages ON Repositories.id = Languages.repo_id
    WHERE Languages.language = ?
    LIMIT 1
    '''
    
    cursor.execute(query, (language,))
    developer = cursor.fetchone()
    
    conn.close()
    
    if developer:
        return developer[0]
    else:
        return None

while(True):
    language_to_search = input("Enter the programming language to search for: ")
    developer = find_developer_by_language(language_to_search)
    if developer:
        print(f'Found a developer using {language_to_search}: {developer}')
    else:
        print(f'No developer found using {language_to_search}')
    another_search = input("Do you want to search for another language? (y/n): ")
    if another_search.lower() != 'y':
        break