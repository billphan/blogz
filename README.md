# blogz
LC101 assignment
http://education.launchcode.org/web-fundamentals/assignments/blogz

- A Python/Flask based web app implementation of a blog.  
- Builds upon build-a-blog assignment. Refactor to expand our codebase to make this a multi-user blog site. Add user authentication and verification, users will have individual blog page displaying all posts by that user. Vistors can view blogs by authors, or view all blog posts on the site. We will still maintain the ability to view individual blog entry.

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

* **Given** Anonymous Visitor (not logged in)
* **When** Arrive at the site (route _"/"_)
* **Then** See list of blog users and nav bar
  - **If** Visitor clicks a blog user
  - **Then** Visitor redirected "_/blog?user=[selecteduser]_" with blog posts of selected user
  - **If** Visitor clicks Home (_/_)
  - **Then** Redirect to "_/_"
  - **If** Visitor clicks All Posts ("_/blog_")
  - **Then** See list of previous posts by registered users
  - **If** Visitor clicks New Post ("_/newpost_")
  - **Then** Visitor is redirected to _/login_ page
  - **If** Visitor clicks Login ("_/login_")
  - **Then** Arrive at Login page
  - **If** Visitor attempts to login
  - **If** Visitor enters a username that is stored in the database w/ the correct pw
  - **Then** Redirected to the "_/newpost_" with username stored in a session
  - **Then** Visitor is logged in (see **Scenario B**)
  - **If** Visitor enters a username that is stored in the databate BUT w/ the wrong pw
  - **Then** Redirected to "_/login_" with msg that pw is wrong
  - **If** Visitor enters a username NOT stored in database
  - **Then** Redirected to "_/login_" with msg that username does not exist
  - **If** Visitor does not have an account and clicks Create Account
  - **Then** Redirected to the "_/signup_" page
  - **If** Visitor enters new, valid username, valid pw, and verifies pw correctly
  - **Then** Redirected to "_newpost_" page with their username stored in session
  - **Then** Visitor is logged in (see **Scenario B**)
  - **If** Visitor leaves any of username, pw, or verify fields blank
  - **Then** Gets Error msg that one or more fields invalid
  - **If** Visitor enters a pre-existing username
  - **Then** Receive error msg that user exists already
  - **If** Visitor enters different strings into pw and verify field
  - **Then** Receive an error that pw doesn't match
  - **If** Visitor enters pw or username less than 3 characters long
  - **Then** Receive an invalid username or an invalid pw msg
  - **If** Visitor clicks Log Out ("_/logout_")
  - **Then** Redirect to "_/blog_"
                 
## Scenario B: When Logged In

* **Given** Registerd User (logged in)
* **When** Arrive at the site (route _"/"_)
* **Then** See list of blog users and nav bar
  - **If** User clicks a blog user
  - **Then** User redirected "_/blog?user=[selecteduser]_" with blog posts of selected user
  - **If** User clicks Home (_/_)
  - **Then** Redirect to "_/_"
  - **If** User clicks All Posts ("_/blog_")
  - **Then** See list of previous posts by registered users
  - **If** User clicks New Post ("_/newpost_")
  - **Then** User is redirected to _/newpost_ page
  - **If** User inputs content into title and body forms and clicks submit
  - **Then** Redirected to _"blog?id=[blog_id]"_ with submitted blog post 
  - **If** User does not input content into title or body forms and clicks submit
  - **Then** Redirected to _"/newpost"_ with error message that need to put content into title or body forms
  - **If** User clicks Login ("_/login_")
  - **Then** Redirect to "_/blog_"
  - **If** User clicks Log Out ("_/logout_")
  - **Then** Redirect to "_/blog_"

## User accessible command (the menu items):
* Home ("/index")
* Add New Post ("/newpost")
* View All Posts ("/blog")
* Login ("/login")
* Logout ("/logout")

## Bonus Missions and Additions to Program
* Add Pagination
* Add Hashing
* Add Date timestamps to posts
* Add CSS Styling, Bootstrap 
* Add and Implement Flask Login module: https://flask-login.readthedocs.io/en/latest/

## Routes
* **"/"** - GET: redirect to "/blog"
* **"/blog"** - GET: Display list of all entries with default sort order (oldest-first)
* **"/blog?id=#"** GET: Display entry with id=ID
* **"/post"** - GET: Display new entry form; POST: Process new entry
* **"/login"** - GET: Display login screen with form and verification.
* **"/logout"** - GET: Deletes current user session.

