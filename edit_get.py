from bottle import get, view, redirect
import globals
import sqlite3


@get("/edit/<post_id>")
@view("edit")
def _(post_id):

    try:
        connection = sqlite3.connect(globals.DB_PATH)
        connection.row_factory = globals.create_json_from_sqlite_result
        cursor = connection.cursor()

        post_from_db = cursor.execute(
            "SELECT posts.*, users.first_name, users.last_name, users.username, users.picture FROM posts JOIN users WHERE users.id = posts.user_id AND posts.id = ?", (post_id, )).fetchone()

        return dict(post=post_from_db)
    except Exception as ex:
        print(ex)
        print("Error in database")
    finally:
        connection.close()

    return redirect('/posts')
