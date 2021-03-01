import requests
import random
from socialnet.bot.requester import (signup, token_auth,
                                   create_posts, like_post,
                                   dislike_post)

from socialnet.bot.hunter import hunter

bot_conf = {
    "number_of_users": 0,
    "max_posts_per_user": 0,
    "max_likes_per_user": 0,
}

with open('rules.txt', 'r') as file:
    for line in file:
        line_vals = line.strip().split(" = ")
        bot_conf[line_vals[0]] = line_vals[1]

request_for_users = requests.get(f"https://random-data-api.com/api/users/random_user/?size={bot_conf['number_of_users']}")
users_list = request_for_users.json()

request_for_data = requests.get(f"https://random-data-api.com/api/hipster/random_hipster_stuff/?size={bot_conf['max_posts_per_user']}")
data_list = request_for_data.json()

for user in users_list:
    email = user.get("email")
    password = user.get("password")
    first_name = user.get("first_name")
    last_name = user.get("last_name")
    max_posts = int(bot_conf["max_posts_per_user"])
    s = hunter.email_verifier(email)

    if s.get("status") == 'invalid':
        continue

    signup(email, password, first_name, last_name)
    token = token_auth(email, password).get("token")
    user["token"] = token
    create_posts(token, data_list, max_posts)

for user in users_list:
    if hasattr(user, 'token'):
        for num in range(int(bot_conf["max_likes_per_user"])):
            posts = requests.get("http://127.0.0.1:8000/api/posts/").json()
            rand_post_like = random.choice(posts)
            like_post(user["token"], rand_post_like)
            rand_post_dis = random.choice(posts)
            dislike_post(user["token"], rand_post_dis)





