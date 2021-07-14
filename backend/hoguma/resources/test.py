from flask import jsonify
from flask_restful import Resource, reqparse
from hoguma.models.survey import Survey, SurveyResult
from hoguma.models.word import Word
from hoguma.models.emotion import Emotion
from hoguma.models.character import Character
from hoguma import db

import random


parser = reqparse.RequestParser()
parser.add_argument("joy")
parser.add_argument("sadness")
parser.add_argument("anger")


class Test(Resource):
    def get(self, category):
        args = parser.parse_args()
        result = []
        if category == "survey":
            survey_set = db.session.query(Survey).all()
            for survey in survey_set:
                q_num = survey.id
                question = survey.question
                image_url = survey.image
                select = [
                    survey.select_1.split("\n"),
                    survey.select_2.split("\n"),
                    survey.select_3.split("\n"),
                ]

                data = {
                    "q_num": q_num,
                    "question": question,
                    "image_url": image_url,
                    "select": select,
                }
                result.append(data)

            return jsonify(message="success", data=result)
        elif category == "word":
            words = db.session.query(Word.id, Word.emotion, Word.word).all()
            for word in words:
                result.append(list(word))
            random.shuffle(result)
            return jsonify(message="success", data=result)
        elif category == "result":
            user_emotion_dict = dict()
            user_total = sum(
                [int(args["joy"]), int(args["sadness"]), int(args["anger"])]
            )
            user_joy = round(int(args["joy"]) / user_total * 100)
            user_sadness = round(int(args["sadness"]) / user_total * 100)
            user_anger = round(int(args["anger"]) / user_total * 100)
            user_emotion = sorted(
                [
                    ["anger", user_anger],
                    ["joy", user_joy],
                    ["sadness", user_sadness],
                ],
                key=lambda x: x[1],
                reverse=True,
            )
            emotions = db.session.query(Emotion).all()
            character_emotion_arr = []
            banned_character = {8, 12, 13, 14}
            for emotion in emotions:
                character_id = emotion.character_id
                if character_id in banned_character:
                    continue
                joy = emotion.joy
                anger = emotion.anger
                sadness = emotion.sadness
                ch_emotion_dict = {
                    "joy": joy,
                    "anger": anger,
                    "sadness": sadness,
                }
                character_emotion = [character_id, ch_emotion_dict]
                character_emotion_arr.append(character_emotion)
            character_emotion_arr.sort(
                key=lambda x: (
                    abs(x[1][user_emotion[0][0]] - user_emotion[0][1]),
                    abs(x[1][user_emotion[1][0]] - user_emotion[1][1]),
                    abs(x[1][user_emotion[2][0]] - user_emotion[2][1]),
                )
            )
            min_character = character_emotion_arr[0][0]
            target_character = (
                db.session.query(Character.name)
                .filter(Character.id == min_character)
                .all()[0][0]
            )
            survey_result = (
                db.session.query(SurveyResult)
                .filter(SurveyResult.name == target_character)
                .all()[0]
            )
            result = {
                "id": survey_result.id,
                "image": survey_result.image,
                "nick_name": survey_result.nick_name,
                "emotion": {
                    "기쁨": character_emotion_arr[0][1]["joy"],
                    "슬픔": character_emotion_arr[0][1]["sadness"],
                    "분노": character_emotion_arr[0][1]["anger"],
                },
                "name": survey_result.name,
                "description": survey_result.description,
                "pair": survey_result.pair.split("\n"),
            }
            return jsonify(message="success", data=result)
