from bottle import get, redirect, re, request, post, view, response
import uuid
import os
import globals
import sqlite3
import imghdr

##############################

# users = [] has been replaced with globals.USERS


##############################

sql_signup = """
	INSERT INTO users (first_name, last_name, username, bio, picture, password, email) VALUES (?, ?, ?, ?, ?, ?, ?)
"""


def save_image(image_file, username):
    file_name, file_extension = os.path.splitext(image_file.filename)
    path = "images/pictures"

    # Validate extension
    if file_extension not in (".png", ".jpeg", ".jpg"):
        return None

    # overwrite jpg to jpeg so imghdr will pass validation
    if file_extension == ".jpg":
        file_extension = ".jpeg"

    image_name = username + "_" + file_name + file_extension

    image_file.save(f"{path}/{image_name}")

    print("imghdr.what", imghdr.what(f"{path}/{image_name}"))

    imghdr_extension = imghdr.what(f"{path}/{image_name}")

    if file_extension != f".{imghdr_extension}":
        print("Hmm, this is not really an image")
        # remove the invalid image from the folder
        os.remove(f"{path}/{image_name}")
        return None

    return image_name


@post("/signup")
def _():

    # VALIDATION
    if not request.forms.get("first_name"):
        response.status = 400
        return "First name is missing"
    if not request.forms.get("last_name"):
        response.status = 400
        return "Last name is missing"
    if not request.forms.get("username"):
        response.status = 400
        return "Username is missing"
    if len(request.forms.get("username")) < 4:
        response.status = 400
        return "Username name must be at least 4 characters"
    if len(request.forms.get("first_name")) < 2:
        response.status = 400
        return "Your first name must be at least 2 characters"
    if len(request.forms.get("last_name")) < 2:
        response.status = 400
        return "Your last name must be at least 2 characters"
    if not request.forms.get("user_email"):
        return "Email is missing"
    if not re.match(globals.REGEX_EMAIL, request.forms.get("user_email")):
        return "Your email address doesn't have the correct format."
    if not request.forms.get("user_password"):
        return "Password is missing."
    if len(request.forms.get("user_password")) < 4:
        return "Password mush be at lest 4 characters"
    if len(request.forms.get("user_password")) > 20:
        return "Password must be less than 20 characters"

    first_name = request.forms.get("first_name")
    last_name = request.forms.get("last_name")
    username = request.forms.get("username")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    bio = request.forms.get("bio")

    print(request.files.get("my_picture"))

    picture_name = save_image(request.files.get("my_picture"), username)

    if (not picture_name):
        return "Bad image"

    try:
        connection = sqlite3.connect(globals.DB_PATH)
        connection.row_factory = globals.create_json_from_sqlite_result
        cursor = connection.cursor()
        cursor.execute(sql_signup, (first_name, last_name,
                       username, bio, picture_name, user_password, user_email))

        connection.commit()

        connection.close()
    except:
        print("Error in database")

    return redirect(f"/signup-ok?user_email={user_email}&first_name={first_name}&username={username}")
