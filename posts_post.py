from bottle import get, redirect, post, request, response, view
import globals
import datetime
import sqlite3
##############################

# posts = [] has been replaced with globals.POSTS

##############################

sql_post = """
    INSERT INTO posts (text, created_at, user_id) VALUES (?, ?, ?)
"""


@post("/posts")
def _():
    user_session = globals.check_session()

    if (not user_session):
        return redirect('/login')
    if len(request.forms.get("text")) < 1:
        response.status = 400
        return "Your post must be at least 1 character(s) long"
    if len(request.forms.get("text")) > 300:
        response.status = 400
        return "Your post must be less than 300 characters"

    time = datetime.datetime.now()

    text = request.forms.get("text")
    time = int(datetime.datetime.now().timestamp())
    try:
        connection = sqlite3.connect(globals.DB_PATH)
        connection.row_factory = globals.create_json_from_sqlite_result
        cursor = connection.cursor()
        cursor.execute(sql_post, (text, time, user_session["user_id"]))

        connection.commit()

        connection.close()

    except:
        print("Error in database")

    return redirect('/posts')
