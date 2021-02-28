import requests
import json

host_url = "http://127.0.0.1:8000/api"

def signup(email, password, first_name, last_name):
    data = {
        "password": password,
        "password2": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
    }
    signup_req = requests.post(f"{host_url}/user/signup/", data=data)
    return signup_req

def token_auth(email, password):
    data = {
        "password": password,
        "email": email,
    }
    auth_req = requests.post(f"{host_url}/user/token/", data=data).json()
    return auth_req

def create_posts(token, data_list, max_posts=1):
    headers = {"Content-Type": "application/json", "Authorization": "JWT {}".format(token)}
    for count, post in enumerate(data_list):
        if count < max_posts:
            post = {"title": post["sentence"], "content": post["paragraph"]}
            post_json = json.dumps(post).encode("utf8")
            resp = requests.post(f"{host_url}/posts/", data=post_json, headers=headers)

def like_post(token, post):
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
    data = {"likes": int(post["likes"])+1}
    data_json = json.dumps(data).encode("utf8")
    id = post["id"]
    resp = requests.patch(f"{host_url}/posts/{id}/", data=data_json, headers=headers)
    return resp

def dislike_post(token, post):
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
    id = post["id"]
    if int(post["likes"]) <= 0:
        return requests.exceptions.BaseHTTPError("Can't be less then zero") # TODO: add validators to model Post
    data = {"likes": int(post["likes"]) - 1}
    data_json = json.dumps(data).encode("utf8")
    resp = requests.patch(f"{host_url}/posts/{id}/", data=data_json, headers=headers)
    return resp