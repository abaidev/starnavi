import requests
import random
from socialnet.bot.requester import (signup, token_auth,
                                   create_post, like_post,
                                   dislike_post)

bot_conf = {
    "number_of_users": 0,
    "max_posts_per_user": 0,
    "max_likes_per_user": 0,
}
counter = random.randint(14,255) + random.randint(20, 4528) + random.randint(30, 4587) * 3
with open('rules.txt', 'r') as file:
    for line in file:
        line_vals = line.strip().split(" = ")
        bot_conf[line_vals[0]] = line_vals[1]

request_for_users = requests.get(f"https://random-data-api.com/api/users/random_user?size={bot_conf['number_of_users']}")
users_list = request_for_users.json()

for user in users_list:
    email = user.get("email")
    password = user.get("password")
    first_name = user.get("first_name")
    last_name = user.get("last_name")
    max_posts = int(bot_conf["max_posts_per_user"])

    print(user)

    signup(email, password, first_name, last_name)
    token = token_auth(email, password).get("token")
    user["token"] = token
    create_post(token, counter, max_posts)

posts = requests.get("http://127.0.0.1:8000/api/posts/").json()

for post in posts:
    for user in users_list:
        like_post(user["token"], post)
        dislike_post(user["token"], post)

