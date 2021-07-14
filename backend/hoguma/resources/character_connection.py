from flask import jsonify
from flask_restful import Resource
from hoguma.models.character import Character
from hoguma.models.connection import Connection
from hoguma import db


class CharacterConnection(Resource):
    def get(self):
        nodes = dict()
        characters = db.session.query(Character).all()
        for character in characters:
            ch_id = character.id
            name = character.name
            nodes[ch_id] = name

        edge_origin = []
        edge_DA = []

        connections = db.session.query(Connection).all()
        for connection in connections:
            temp = dict()
            temp["target"] = connection.target
            temp["source"] = connection.source
            if connection.origin_type:
                temp["origin_type"] = connection.origin_type
                edge_origin.append(temp)
            else:
                temp["connection_weight"] = connection.connection_weight
                if 0 <= temp["connection_weight"] <= 160:
                    weight_tag = "none"
                elif 161 <= temp["connection_weight"] <= 320:
                    weight_tag = "light"
                elif 321 <= temp["connection_weight"] <= 480:
                    weight_tag = "normal"
                elif 481 <= temp["connection_weight"] <= 640:
                    weight_tag = "hard"
                elif 641 <= temp["connection_weight"] <= 801:
                    weight_tag = "extreme"
                temp["weight_tag"] = weight_tag
                edge_DA.append(temp)
        result = {
            "nodes": nodes,
            "edge_origin": edge_origin,
            "edge_DA": edge_DA,
        }
        return jsonify(message="success", data=result)
