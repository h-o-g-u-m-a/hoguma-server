from flask import Flask, send_from_directory

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

import config

db = SQLAlchemy()
migrate = Migrate()

from hoguma.models.character import Character
from hoguma.models.connection import Connection
from hoguma.models.emotion import Emotion
from hoguma.models.gacha import Gacha
from hoguma.models.overdose import Overdose, OverdoseResult
from hoguma.models.stock import Stock
from hoguma.models.survey import Survey, SurveyResult
from hoguma.models.word import Word

# api
from hoguma.resources.test import Test
from hoguma.resources.character_detail import CharacterDetail
from hoguma.resources.character_connection import CharacterConnection
from hoguma.resources.overdose_result import Virtuoso
from hoguma.resources.overdose_question import OverdoseTest
from hoguma.resources.game import Game


def set_api_resources(api):
    api.add_resource(Test, "/test/<category>")
    api.add_resource(CharacterDetail, "/character/<character_id>")
    api.add_resource(CharacterConnection, "/connection")
    api.add_resource(Virtuoso, "/overdose/<int:user_score>")
    api.add_resource(OverdoseTest, "/overdose")
    api.add_resource(Game, "/game/", "/game/<gacha_id>")


def create_app():
    app = Flask(__name__)

    # app에 config 적용
    app.config.from_object(config)

    CORS(app, supports_credentials=True)

    # api 설정
    api = Api(app)
    set_api_resources(api)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/image/<category>/<file_name>")
    def send_image(category, file_name):
        if category == "character":
            uri = app.config["CHARACTER_DETAIL_URI"]
        elif category == "overdose":
            uri = app.config["OVERDOSE_URI"]
        elif category == "question":
            uri = app.config["SURVEY_QUESTION_URI"]
        elif category == "result":
            uri = app.config["SURVEY_RESULT_URI"]
        elif category == "word":
            uri = app.config["WORD_CLOUD_URI"]
        return send_from_directory(uri, file_name)

    return app
