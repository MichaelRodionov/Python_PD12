import json


picture_format = ['png', 'jpeg']


def load_posts(posts) -> list[dict]:
    with open(posts) as file:
        posts_list = json.load(file)
        return posts_list


def get_post(all_posts, word) -> list[dict]:
    search_post_list = []
    for post in all_posts:
        if word in post['content']:
            search_post_list.append(post)
    return search_post_list


def add_post(picture, cont, posts) -> dict:
    data = load_posts(posts)
    with open('./posts.json', 'w') as file:
        post = {
            'pic': picture,
            'content': cont,
        }
        data.append(post)
        json.dump(data, ensure_ascii=False, fp=file, indent=4)
        return post


def check_format(filename) -> bool:
    if filename.split('.')[1] in picture_format:
        return True
    return False
