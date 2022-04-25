from bottle import post, redirect, request, response
import globals
import sqlite3


@post("/delete-post")
def _():
    post_id = request.forms.get("post_id")
    user_session = globals.check_session()

    isAdmin = request.query.admin

    if (not user_session):
        return redirect('/login')

    print("POSTTT IIDD")

    print(post_id)
    try:
        connection = sqlite3.connect(globals.DB_PATH)
        cursor = connection.cursor()

        if isAdmin and user_session["user"]["username"] == "admin":
            cursor.execute("DELETE FROM posts WHERE posts.id = ?", (post_id, ))
        else:
            cursor.execute("DELETE FROM posts WHERE posts.id = ? AND posts.user_id = ?",
                           (post_id, user_session["user_id"]))

        connection.commit()

    except Exception as ex:
        print(ex)
        print("Error in database")
    finally:
        connection.close()

    if isAdmin:
        return redirect("/admin")
    else:
        return redirect("/posts")
