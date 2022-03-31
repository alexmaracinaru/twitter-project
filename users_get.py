from bottle import get, redirect, request, post, view
import globals

##############################


@get("/users")
@view("users")
def _():
    return dict(users=globals.USERS)

# users is the variable that will be passed in the html template users.html
