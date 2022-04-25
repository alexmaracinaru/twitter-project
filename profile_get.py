from bottle import get, view, request, redirect
import globals
import sqlite3


query_get_profile_posts = """
    SELECT posts.*, users.username, users.id, users.first_name, users.last_name, users.bio, users.picture
    FROM users JOIN posts WHERE users.id = posts.user_id AND users.username = ?
"""

query_get_profile = """
    SELECT users.username, users.id, users.first_name, users.last_name, users.bio, users.picture
    FROM users WHERE users.username = ?
"""


##############################
@get("/profile/<username>")
@view("profile")
def _(username):
    user_session = globals.check_session()

    connection = sqlite3.connect("./database.sqlite")
    connection.row_factory = globals.create_json_from_sqlite_result
    cursor = connection.cursor()

    try:
        profile = cursor.execute(query_get_profile, (username,)).fetchone()

        posts = cursor.execute(query_get_profile_posts, (username,)).fetchall()

        return dict(posts=posts, user=user_session["user"], tabs=globals.TABS, items=globals.ITEMS, trends=globals.TRENDS, profile=profile)
    except:
        print("err")

    return redirect('/login')
