from bottle import get, view, redirect
import globals


@get("/edit/<post_id>")
@view("edit")
def _(post_id):
    for index, post in enumerate(globals.POSTS):
        if post["post_id"] == post_id:
            return dict(post=post)
    return redirect('/posts')
