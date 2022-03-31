from bottle import get, request, redirect
import globals


@get("/logout")
def _():
    user_session_id = request.get_cookie("uuid4")
    print("LOGOUT")
    print(user_session_id)
    print(globals.SESSIONS)
    globals.SESSIONS.remove(user_session_id)

    print("AFTER REMOVED")
    print(globals.SESSIONS)
    return redirect("/login")
