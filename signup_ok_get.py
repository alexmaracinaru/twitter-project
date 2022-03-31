from bottle import get, request, view


@get("/signup-ok")  # query string expected with user-email
@view("signup-ok")
def _():
    user_email = request.params.get("user_email")
    first_name = request.params.get("first_name")
    username = request.params.get("username")
    return dict(user_email=user_email, first_name=first_name, username=username)
