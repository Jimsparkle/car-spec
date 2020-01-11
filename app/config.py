import os

class Config(object):
    # we will change and not expose the secret key later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'e13a29ec5dde193583893df7cdfa5256'