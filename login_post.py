from bottle import error, get, post, redirect, request, response, run, static_file, view
import uuid
import globals


@post("/login")
def _():
    username = request.forms.get("username")
    user_password = request.forms.get("user_password")
    print(username)

    for user in globals.USERS:
        if user["username"] == username:
            if user["user_password"] == user_password:
                response.set_cookie("user_id", user["user_id"],
                                    secret=globals.COOKIE_SECRET)
                user_session_id = str(uuid.uuid4())
                globals.SESSIONS.append(user_session_id)
                response.set_cookie("uuid4", user_session_id)

                print("LOGIN")
                print(user_session_id)

                return redirect("/posts")

    return 'password or username incorrect'
