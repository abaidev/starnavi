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
    print("SIGN UP")
    print(signup_req)
    return signup_req

def token_auth(email, password):
    data = {
        "password": password,
        "email": email,
    }
    auth_req = requests.post(f"{host_url}/user/token/", data=data).json()
    print("TOKEN AUTH")
    print(auth_req)
    return auth_req

def create_post(token, counter, max_posts=1):
    headers = {"Content-Type": "application/json", "Authorization": "JWT {}".format(token)}
    data = {"title": f"Ais Ventura - {counter}", "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit."}
    data_json = json.dumps(data).encode("utf8")
    counter += 1
    for num in range(max_posts):
        resp = requests.post(f"{host_url}/posts/", data=data_json, headers=headers)
        print("CREATE POST")
        print(resp)
        print(resp.text)
        return resp

def like_post(token, post):
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
    data = {"likes": int(post["likes"])+1}
    data_json = json.dumps(data).encode("utf8")
    slug = post["slug"]
    resp = requests.patch(f"{host_url}/posts/{slug}/", data=data_json, headers=headers)
    return resp

def dislike_post(token, post):
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
    slug = post["slug"]
    if int(post["likes"]) <= 0:
        return requests.exceptions.BaseHTTPError("Can't be less then zero") # TODO: add validators to model Post
    data = {"likes": int(post["likes"]) - 1}
    data_json = json.dumps(data).encode("utf8")
    resp = requests.patch(f"{host_url}/posts/{slug}/", data=data_json, headers=headers)
    print("DISLIKE POST")
    print(resp)
    print(resp.text)
    return resp