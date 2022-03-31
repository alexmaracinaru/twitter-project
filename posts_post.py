from bottle import get, redirect, request, post, view
import globals
import timeago
import datetime
import uuid

##############################

# posts = [] has been replaced with globals.POSTS

##############################


@post("/posts")
def _():
    user_session_id = request.get_cookie("uuid4")
    # compare the uuid from the cookie to the uuid from the sessions
    if user_session_id not in globals.SESSIONS:
        return redirect("/login")
    user_id = request.get_cookie("user_id", secret=globals.COOKIE_SECRET)

    time = datetime.datetime.now()
    for user in globals.USERS:
        if user["user_id"] == user_id:

            tweet = request.forms.get("tweet")
            post_id = str(uuid.uuid4())
            post = {
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "username": user["username"],
                "createdAt": time,
                "tweet": tweet,
                "post_id": post_id,
                "formattedCreatedAt": time.strftime("%H:%M %d-%m-%Y")
            }
            globals.POSTS.append(post)

            return redirect('/posts')

    return "something went wrong"
