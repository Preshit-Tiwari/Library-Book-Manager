# Library System
#### Video Demo:  <URL https://youtu.be/FLqYUutenVs>
# Description:

#### This is project Uses:
    - HTML
    - CSS
    - JavaScript
    - Bootstrap
    - Flask
    - Sqlite3

#### This project requires:
    - cs50
    - Flask
    - Flask-Session
    - pytz
    - requests

### This is a Library record system that provides:

1. **login facility**: It helps user to login.
2. **Registration facility**: It helps user to register themselves in the system.
3. **Home Page**: This is the first page of the site and it contains general description of the site and am image that redirects to the global library list.
4. **Global library list**: A global library is maintained to show data in tabular format which shows book id, name and availability of the library books form the database.
5. **Issue book**: This is a option used by the logged person to issue book for themselves by entering book id in correct manner.
6. **Return book**: This is a option used by the logged person to return book to the library by entering book id in correct manner.
7. **History**: This section saves the history of the logged user and shows it in the tabular format containing fields like book id, name, type of service, date/time of service.
8. **Password Changing facility**: This feature helps logged in members to change the password of their account by enter the correct data in right manner.
9. **Log-out**: This option helps the logged user to log-out of the site, after log-out it redirects to the log-in window.
10. **Error handing**: This site takes user inputs very wisely and raises concern with the user on different scenarios.

### Note:
    A student can issue at max 5 books at a time.

## How to Use Site:
Steps to use site are:

1. **Step one**: Open the project path.

    ![Path In Terminal](static/makedown/terminal_start.png)

2. **Step two**: Type `flask Run` and hit enter.

    ![Run Command](static/makedown/terminal_run_command.png)

3. **Step three**: `Ctrl + Click` on the link.

    ![Link In Terminal](static/makedown/erminal_run_link.png)

## How This Site Works:

1. **Register**: 

    ![Register](static/makedown/register.png)

2. **Enter Details and Register**: 

    ![Register_details](static/makedown/register_details.png)

3. **Home site**: 

    This is the home site, Welcome!

    ![Register successful](static/makedown/register_success.png)

4. **choose books**:

    This show the all the books in the library with its status of being available in the library.

    ![Book list](static/makedown/book_list1.png)

5. **Issue book**:

    This help the logged person to enter book id, and it will be issued to him if the book is available in the library and person's book limit of 5 books at a time is not reached.

    ![Issue book](static/makedown/issue_book.png)

6. **Success**:

    On successful issue success message is displayed.

    ![Successful](static/makedown/success.png)

7. **Updated Book List**:

    This redirects to the book list which on successful issue, shows that the book is unavailable.

    ![Updated book list](static/makedown/book_list2.png)

8. **Return Book**:

    This help the logged person to return the book(if issued) by entering the book id.

    ![Return book](static/makedown/issue_book.png)

9. **Success**:

    On successful issue success message is displayed.

    ![Successful](static/makedown/success.png)

10. **Updated Book List**:

    This redirects to the book list which on successful return, shows that the book is now available.

    ![Updated book list](static/makedown/book_list1.png)

11. **History**:

    This is the section that records the history of the logged user with time and book details.

    ![History list](static/makedown/History_list1.png)

    ![History list](static/makedown/History_list2.png)

12. **Change Password**:

    This option helps user to change password.

    ![Change Password](static/makedown/change_pass_logout.png)

13. **Enter Details and Change**:

    ![Enter Details](static/makedown/password_details.png)

14. **Success**:

    Password Updated

    ![Successful password changed](static/makedown/success_change.png)

15. **logging out**:

    This option helps user to logout.

    ![log_out](static/makedown/change_pass_logout.png)

    ![Login page](static/makedown/login_page.png)

## How Error is Handled:

1. Everything user input is validated first and hence any kind of user error is informed in the following manner:

    example: Book not Available

    ![error page](static/makedown/error.png)


## Credits:
    - Team cs50
    - W3schools
    - Official documents
    - cs50 duck
    - gir-hub 
    - vs-code
    - others