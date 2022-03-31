from bottle import post, redirect, request
import globals


@post("/delete-post")
def _():

    post_id = request.forms.get("post_id")

    # Delete the post for if enumerate
    for index, post in enumerate(globals.POSTS):
        if post["post_id"] == post_id:
            globals.POSTS.pop(index)
            return redirect("/posts")
    return redirect("/posts")
