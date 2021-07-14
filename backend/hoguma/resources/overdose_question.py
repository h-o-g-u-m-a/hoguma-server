from flask import jsonify
from flask_restful import Resource
from hoguma.models.overdose import Overdose
from hoguma import db

import random


class OverdoseTest(Resource):
    def get(self):
        result = []

        test_set = db.session.query(Overdose).all()
        for test in test_set:
            qnum = test.question_number
            question = test.question
            answer = test.answer

            select_1 = test.select_1
            if answer == select_1:
                select_1_TF = True
            else:
                select_1_TF = False
            select_2 = test.select_2
            if answer == select_2:
                select_2_TF = True
            else:
                select_2_TF = False
            select_3 = test.select_3
            if answer == select_3:
                select_3_TF = True
            else:
                select_3_TF = False
            select_4 = test.select_4
            if answer == select_4:
                select_4_TF = True
            else:
                select_4_TF = False

            select = [
                [select_1, select_1_TF],
                [select_2, select_2_TF],
                [select_3, select_3_TF],
                [select_4, select_4_TF],
            ]

            random.shuffle(select)

            data = {
                "qnum": qnum,
                "question": question,
                "select": select,
            }

            result.append(data)

        return jsonify(message="success", test=result)
