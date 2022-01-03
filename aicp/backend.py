from supabase import create_client, Client
import os
import json


# load json file from home directory
def load_config():
    home_dir = os.path.expanduser("~")
    config_json_path = os.path.join(home_dir, ".aicp", "config.json")
    if os.path.exists(config_json_path):
        with open(config_json_path) as config_json_file:
            return json.load(config_json_file)
    return None


def write_config(url: str, secret: str, username: str, password: str) -> str:
    # create config.json
    home_dir = os.path.expanduser("~")
    config_json_path = os.path.join(home_dir, ".aicp", "config.json")

    if not os.path.exists(os.path.dirname(config_json_path)):
        os.makedirs(os.path.dirname(config_json_path))

    config_json = {
        "url": url,
        "secret": secret,
        "username": username,
        "password": password,
    }
    with open(config_json_path, "w") as config_json_file:
        json.dump(config_json, config_json_file)

    return config_json_path


def get_backend_client() -> Client:
    config = load_config()
    return create_client(config['url'], config['secret'])

def login():
    config = load_config()
    user = get_backend_client().auth.sign_in(email=config['username'], password=config['password'])

    return user