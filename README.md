# blogz
LC101 assignment

http://education.launchcode.org/web-fundamentals/assignments/blogz

* A Python/Flask based web app implementation of a blog.  
* Addition on Build-a-Blog project. Refactor to expand our codebase to make this a multi-user blog site. Add user authentication and verification, users will have individual blog page displaying all posts by that user. Vistors can view blogs by authors, or view all blog posts on the site. We will still maintain the ability to view individual blog entry.

## Changes made to Build-a-Blog:

* Make a Home Page ("/")
* Display all blog users
* Use index.html template
* Registered User Integration
* Adding the following templates: signup.html, login.html, index.html.
* Add the following route handler functions: signup, login, and index.
* Add a User class.
* Add a login function.
* Add a logout function.
* Handles a POST request to "/logout" and redirects user to "/blog" after deleting user from session.
* Creating Dynamic User Pages
* Add a singleUser.html template that will be used to display only the blogs associated with a single given poster. It will be used when we dynamically generate a page using a GET request with a user query parameter on the "/blog" route.

# User Scenarios

## Scenario A: When Not Logged In:

* **Given** Anonymous Visitor (not logged in).
* **When** Arrive at index. Route ("/").
* **Then** Sees home page with full list of users.
  - **If** Visitor clicks a "username".
  - **Then** Visitor redirected ("/blog?user=[id]") with blog posts of selected user.
  - **If** Visitor clicks "home" ("/").
  - **Then** Redirect to ("/").
  - **If** Visitor clicks "view all posts" and redirects to ("/blog").
  - **Then** See list of previous posts by registered users.
  - **If** Visitor clicks "create new post" ("/newpost").
  - **Then** Visitor is redirected to ("/login") page.
  - **If** Visitor clicks "login" ("/login").
  - **Then** Arrive at login screen.
  - **If** Visitor attempts to login to account.
  - **If** Visitor enters a username that is stored in the database with the correct password.
  - **Then** Redirected to ("/newpost") with username stored in current session.
  - **Then** Visitor is currently logged in (see **Scenario B**).
  - **If** Visitor enters a username that is stored in the databate BUT with incorrect password.
  - **Then** Redirected to ("/login") with error indicating a wrong password was entered.
  - **If** Visitor enters a username NOT stored in database.
  - **Then** Redirected to ("/login") with error indicating that username does not exist.
  - **If** Visitor does not have an account and clicks "create account".
  - **Then** Redirected to the ("/signup") page.
  - **If** Visitor enters a valid username, valid password, and verifies password.
  - **Then** Redirected to ("/newpost") page with their username stored in current session.
  - **Then** Visitor is logged in (see **Scenario B**).
  - **If** Visitor leaves any of signup fields blank.
  - **Then** Gets an error that one or more fields invalid and/or filled in incorrectly.
  - **If** Visitor enters a pre-existing username.
  - **Then** Receive error that the user already exists.
  - **If** Visitor enters different password and incorrect verification password.
  - **Then** Receives an error that passwords don't match.
  - **If** Visitor enters password or username that is less than 3 characters long.
  - **Then** Receives an invalid username or an invalid password error.
  - **If** Visitor clicks "logout" ("/logout").
  - **Then** Redirect to ("/blog").
                 
## Scenario B: When Logged In

* **Given** Registered User (Logged In)
* **When** Arrive at the site index route ("/").
* **Then** See index and list of users.
  - **If** User clicks a blog username.
  - **Then** User redirected ("/blog?user=[id]") with all blog posts of selected user.
  - **If** User clicks "home" ("/").
  - **Then** Redirect to ("/").
  - **If** User clicks "view all posts" ("/blog").
  - **Then** See list of previous posts by registered users.
  - **If** User clicks "new post" ("/newpost").
  - **Then** User is redirected to ("/newpost") page.
  - **If** User inputs content into title and body forms and clicks submit.
  - **Then** Redirected to ("blog?id=[id]") with submitted blog post.
  - **If** User does not input content into title or body forms and submits.
  - **Then** Redirected to ("/newpost") with error message that either title, content, or both needs to be filled in.
  - **If** User clicks "login" ("/login").
  - **Then** Redirect to ("/blog").
  - **If** User clicks "logout" ("/logout").
  - **Then** Redirect to ("/blog").

## User accessible command (the menu items):
* Home ("/index")
* Add New Post ("/newpost")
* View All Posts ("/blog")
* Login ("/login")
* Logout ("/logout")

## Bonus Missions and Additions to Program
* Add Hashing
* Add Pagination

## Routes
* **"/"** - GET: redirect to "/blog"
* **"/blog"** - GET: Display list of all entries with default sort order (oldest-first)
* **"/blog?id=#"** GET: Display entry with id=ID
* **"/post"** - GET: Display new entry form; POST: Process new entry
* **"/login"** - GET: Display login screen with form and verification.
* **"/logout"** - GET: Deletes current user session.

## Screenshots

![Alt text](/../master/static/screenshots/1.png?raw=true "Optional Title")
![Alt text](/../master/static/screenshots/2.png?raw=true "Optional Title")
![Alt text](/../master/static/screenshots/3.png?raw=true "Optional Title")
![Alt text](/../master/static/screenshots/4.png?raw=true "Optional Title")
