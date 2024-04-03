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

3. The all_books view isn't rendering as a "Home Page" when running the server. Fixed by emptying the path in the project level URLs ```path('books/', include('books.urls'))``` to ```path('', include('books.urls'))```

<img src="documentation/bugs/bmi-bug3.png" width="500"/>
<img src="documentation/bugs/bmi-fix3.png" width="350"/>

4. Mobile book search not showing results. Fixed by comparing the mobile search section with the search section in base.html. The name attribute was missing from mobile. 
The first image shows 15 results when the word "children" was searched, this should show 6 as there are only 6 books in the children's category.

<img src="documentation/bugs/bmi-bug4.png" height="350"/>
<img src="documentation/bugs/bmi-fix4.png" height="350"/>

5. Back to top button being pushed up to middle of page after moving the overlay closing tag. Fixed by moving the back to top button inside the overlay tags.

<img src="documentation/bugs/bmi-bug5.png" height="350"/>
<img src="documentation/bugs/bmi-fix5.png" height="350"/>

6. Quantity increase and decrease buttons on the book summary page aren't working when clicked. The rest of the logic works; disabling the buttons at certain points. Fixed, I was missing a simple hyphen in one of the classes.

7. Quantity increase and decrease buttons work on the book summary page but not on the basket page. I had two different variables for .qty-input in the script; allQtyInputs and allQuantityInputs. Fixed by removing allQuantityInputs and replacing it with allQtyInputs. Both quantity inputs on the book summary page and the basket page now increment and decrement.