from bottle import get, redirect, request, post, view
import uuid
import globals

##############################

# users = [] has been replaced with globals.USERS


##############################

@post("/signup")
def _():
    first_name = request.forms.get("first_name")
    last_name = request.forms.get("last_name")
    username = request.forms.get("username")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    user_id = str(uuid.uuid4())
    user = {"first_name": first_name, "last_name": last_name,
            "user_email": user_email, "user_password": user_password, "user_id": user_id, "username": username}
    globals.USERS.append(user)
    return redirect(f"/signup-ok?user_email={user_email}&first_name={first_name}&username={username}")
