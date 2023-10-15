from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
admins = env.list("ADMINS")  # admins
ADMINS = [int(admin) for admin in admins]
OWNER_ID = env.int("OWNER_ID")  # Bot owner ID
PATH_TO_DB = env.str("PATH_TO_DB")  # Path to database

