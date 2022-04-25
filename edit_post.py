from bottle import post, view, redirect, request
import globals
import sqlite3


@post("/edit/<post_id>")
def _(post_id):
    text = request.forms.get("text")
    user_session = globals.check_session()

    if (not user_session):
        return redirect('/login')

    try:
        connection = sqlite3.connect("./database.sqlite")
        cursor = connection.cursor()
        cursor.execute("UPDATE posts SET text = ? WHERE id = ? AND user_id = ?;",
                       (text, post_id, user_session["user_id"]))

        connection.commit()
    except Exception as ex:
        print(ex)
        print("Error in database")
    finally:
        connection.close()

    return redirect('/posts')
