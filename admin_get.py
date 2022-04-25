from bottle import get, redirect, request, post, view
import globals
import sqlite3

##############################
query_get_profile_posts = """
 SELECT posts.*, users.username, users.first_name, users.last_name
 FROM users JOIN posts WHERE users.id = posts.user_id
"""


@get("/admin")
@view("admin")
def _():
    connection = sqlite3.connect(globals.DB_PATH)
    connection.row_factory = globals.create_json_from_sqlite_result
    cursor = connection.cursor()

    user_session = globals.check_session()

    if (not user_session or user_session["user"]["username"] != "admin"):
        redirect('/login')

    posts = cursor.execute(query_get_profile_posts).fetchall()
    users = cursor.execute("SELECT * FROM users").fetchall()

    connection.close()

    return dict(posts=posts, users=users, user=user_session["user"])

# users is the variable that will be passed in the html template users.html
