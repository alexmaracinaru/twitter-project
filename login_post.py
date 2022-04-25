from bottle import error, get, post, redirect, re, request, response, run, static_file, view
import uuid
import globals
import sqlite3

sql_login = """
SELECT * FROM users WHERE users.username = ? AND users.password = ?
"""


@post("/login")
def _():
    username = request.forms.get("username")
    user_password = request.forms.get("user_password")
    print(username)

    user = None

    try:
        connection = sqlite3.connect("./database.sqlite")
        connection.row_factory = globals.create_json_from_sqlite_result
        cursor = connection.cursor()
        user = cursor.execute(sql_login, (username, user_password)).fetchone()

        connection.commit()
        connection.close()

    except:
        print("Error in database")
        response.status = 500
        return 'Something went wrong'

    if (user):
        user_session_id = str(uuid.uuid4())

        globals.SESSIONS.append(
            {
                "session_id": user_session_id,
                "username": user["username"],
                "user_id": user["id"],
                "user": {
                    "id": user["id"],
                    "username": user["username"],
                    "email": user["email"],
                    "picture": user["picture"],
                    "first_name": user["first_name"],
                    "last_name": user["last_name"]
                }
            })

        response.set_cookie("uuid4", user_session_id)

        print("LOGIN")
        print(user_session_id)
        return redirect("/posts")
    else:
        response.status = 404
        return "Username or password is incorrect"
