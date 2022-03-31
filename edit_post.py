from bottle import post, view, redirect, request
import globals


@post("/edit")
def _():
    post_id = request.forms.get("post_id")
    for index, post in enumerate(globals.POSTS):
        if post["post_id"] == post_id:
            new_value = {"tweet": request.forms.get("tweet")}

            post.update(new_value)

            return redirect('/posts')
    return redirect('/posts')
