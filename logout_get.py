from bottle import get, redirect
import globals


@get("/logout")
def _():
    user_session = globals.check_session()

    print("LOGOUT")
    print(user_session)
    print(globals.SESSIONS)

    for index, session in enumerate(globals.SESSIONS):
        if session["session_id"] == user_session["session_id"]:
            globals.SESSIONS.pop(index)
            return redirect("/posts")

    print(globals.SESSIONS)
    return redirect("/login")
