from bottle import get, view, request, redirect
import globals
import sqlite3


@get("/posts")
@view("posts")
def _():
    connection = sqlite3.connect("./database.sqlite")
    connection.row_factory = globals.create_json_from_sqlite_result
    cursor = connection.cursor()

    user_session = globals.check_session()

    # database
    posts_from_db = []

    try:
        posts_from_db = cursor.execute(
            "SELECT posts.*, users.first_name, users.last_name, users.username, users.picture FROM posts JOIN users WHERE users.id = posts.user_id ORDER BY posts.created_at DESC").fetchall()
        print(posts_from_db)

        if (not user_session):
            return dict(posts=posts_from_db, tabs=globals.TABS, items=globals.ITEMS, trends=globals.TRENDS)

        print(globals.SESSIONS)

        return dict(posts=posts_from_db, user=user_session["user"], tabs=globals.TABS, items=globals.ITEMS, trends=globals.TRENDS)

    except Exception as ex:
        print(ex)
        print("Error in database")
    finally:
        connection.close()

    print("GET POSTS")

    return dict(posts=posts_from_db, tabs=globals.TABS, items=globals.ITEMS, trends=globals.TRENDS)
