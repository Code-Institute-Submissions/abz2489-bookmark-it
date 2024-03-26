# Bugs

## Bugs & Fixes

1. When launching the project for the very first time after creation I received a 400 error "Invalid HTTP_HOST header". This was an easy fix by following the instructions displayed on the error page I added my request URL  to the ALLOWED_HOSTS section of settings.py within the bookmark-it project folder.

<img src="documentation/bugs/bmi-bug1.png" width="500"/>
<img src="documentation/bugs/bmi-fix1.png" width="350"/>

2. db.sqlite3 file is pulling through to github despite being in the .gitignore file. Fixed with the help of Simen Daehlin's very helpful thread in the CI Slack about removing unwanted files using ```git rm -r --cached db.sqlite3 ``` and committing the changes. Due to having to change directory to run the server my db.sqlite3 and requirements.txt files weren't in the root directory.
**Steps taken to fix:**
- Move db.sqlite3 and requirements.txt to the root directory.
- Execute ```git rm -r --cached db.sqlite3 ```
- Commit changes
- Push changes to Github
- Apply migrations ```python3 manage.py migrate```
- Create new super user ```python3 manage.py createsuperuser```