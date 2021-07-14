from flask import jsonify
from flask_restful import Resource
from hoguma import db

from hoguma.models.overdose import OverdoseResult


class Virtuoso(Resource):
    def get(self, user_score):
        user_rank = 0
        if user_score == 10:
            user_rank = 1
        elif 8 <= user_score <= 9:
            user_rank = 2
        elif 5 <= user_score <= 7:
            user_rank = 3
        elif 3 <= user_score <= 4:
            user_rank = 4
        elif 1 <= user_score <= 2:
            user_rank = 5
        elif user_score == 0:
            user_rank = 6

        user_result = (
            db.session.query(OverdoseResult)
            .filter(OverdoseResult.rank == user_rank)
            .all()[0]
        )

        result = {
            "id": user_result.id,
            "image": user_result.image,
            "description": user_result.description.split("\n"),
        }

        return jsonify(message="success", data=result)
