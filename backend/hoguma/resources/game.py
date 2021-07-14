from sqlalchemy.sql.expression import func, select

from flask import jsonify
from flask_restful import Resource
from hoguma.models.gacha import Gacha
from hoguma import db

import random


class Game(Resource):
    def get(self, gacha_id=None):
        result = []

        if gacha_id:
            # 특정 숫자가 url에 포함되어 있으면 그 숫자에 관한 값
            game_set = (
                db.session.query(Gacha).filter(Gacha.id == gacha_id).all()
            )
            for game in game_set:
                game_id = game.id
                nickname = game.nickname
                number = game.gacha_number
                description = game.description
                quote = game.quote
                question = game.question.split("\n")

                data = {
                    "id": game_id,
                    "number": number,
                    "nickname": nickname,
                    "description": description,
                    "quote": quote,
                    "question": question,
                }
                result.append(data)

            return jsonify(message="success", data=result)

        else:
            # 특정 숫자를 넘겨받지 않을 경우에는 랜덤한 값
            game_set = (
                db.session.query(Gacha)
                .filter(Gacha.id == random.randrange(1, 21))
                .all()
            )
            for game in game_set:
                game_id = game.id
                nickname = game.nickname
                number = game.gacha_number
                description = game.description
                quote = game.quote
                question = game.question.split("\n")

                data = {
                    "id": game_id,
                    "number": number,
                    "nickname": nickname,
                    "description": description,
                    "quote": quote,
                    "question": question,
                }
                result.append(data)

            return jsonify(message="success", data=result)
