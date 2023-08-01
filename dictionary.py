favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
persons = ["john","jen","sarah","edward",'phil']
for person  in persons:
    if person  not in favorite_languages.keys():
        print(f"{person}, please come and take the survey")
    elif person  in persons:
        print(f"Thanks {person}")