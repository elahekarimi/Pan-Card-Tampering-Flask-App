from flask import Flask
import os

app = Flask(__name__)
env = os.getenv('ENV', 'development')
app.config['ENV'] = env
if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
