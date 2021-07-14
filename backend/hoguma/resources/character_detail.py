from flask import jsonify
from flask_restful import Resource
from hoguma.models.character import Character
from hoguma.models.emotion import Emotion
from hoguma.models.stock import Stock
from hoguma import db


class CharacterDetail(Resource):
    def get(self, character_id=1):
        character = (
            db.session.query(Character)
            .filter(Character.id == character_id)
            .all()[0]
        )
        name = character.name
        age = character.age
        job = character.job
        qoute = character.quote
        word_clound = character.word_cloud
        youtube = character.youtube

        emotion_dict = {}
        emotions = (
            db.session.query(Emotion)
            .filter(Emotion.character_id == character_id)
            .all()
        )
        for emotion in emotions:
            emotion_dict["기쁨"] = emotion.joy
            emotion_dict["분노"] = emotion.anger
            emotion_dict["슬픔"] = emotion.sadness

        omission_set = {87, 88, 98, 107, 137}
        stock_arr = []
        stocks = (
            db.session.query(Stock)
            .filter(Stock.character_id == character_id)
            .all()
        )
        stocks.sort(key=lambda x: x.episode)
        for stock in stocks:
            stock_arr.append(stock.weight)

        result = {
            "id": character_id,
            "name": name,
            "age": age,
            "job": job,
            "qoute": qoute,
            "word_cloud": word_clound,
            "youtube": youtube,
            "emotion_dict": emotion_dict,
            "stock_arr": stock_arr,
        }

        return jsonify(message="success", data=result)
