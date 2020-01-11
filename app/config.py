import os


class Config(object):
    # we will change and not expose the secret key later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'e13a29ec5dde193583893df7cdfa5256'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://localhost/car_spec_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
