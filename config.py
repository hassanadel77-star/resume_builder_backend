import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "004f2af45d3a4e161a7dd2d17fdae47f"
    SQLALCHEMY_DATABASE_URI = "postgresql://jkjyprquxyugvo:308235fd6ce417d5da7414dce35a9cde04ebf3c694477adc385c457fd26c1958@ec2-52-54-212-232.compute-1.amazonaws.com:5432/da8vi59flt0oot" #os.environ['DATABASE_URL']