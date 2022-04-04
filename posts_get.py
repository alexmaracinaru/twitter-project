from bottle import get, view, request, redirect
import globals


@get("/posts")
@view("posts")
def _():
    user_session_id = request.get_cookie("uuid4")
    # compare the uuid from the cookie to the uuid from the sessions

    print("GET POSTS")
    print(user_session_id)
    print(globals.SESSIONS)

    if user_session_id not in globals.SESSIONS:
        return redirect("/login")

    user_id = request.get_cookie("user_id", secret=globals.COOKIE_SECRET)

    for user in globals.USERS:
        if user["user_id"] == user_id:
            return dict(posts=globals.POSTS, user=user, tabs=globals.TABS, items=globals.ITEMS, trends=globals.TRENDS, people=globals.PEOPLE, tweets=globals.TWEETS)

    return redirect('/login')
