from hoguma import db
from hoguma.models.connection import Connection
from hoguma.models.character import Character

import json
from hoguma import create_app


app = create_app()

character_set = [
    ("문희", "나문희"),
    ("순재", "이순재"),
    ("준하", "이준하"),
    ("민용", "이민용"),
    ("민호", "이민호"),
    ("윤호", "이윤호"),
    ("해미", "박해미"),
    ("범", "김범"),
    ("유미", "강유미"),
    ("찬성", "황찬성"),
    ("개성댁", "개성댁"),
    ("신지", "신지"),
    ("민정", "서민정"),
    ("교감", "홍순창(교감)"),
]

connection_keys = []
for i in range(len(character_set) - 1):
    for j in range(i + 1, len(character_set)):
        connection_keys.append(
            (
                character_set[i][0],
                character_set[j][0],
                character_set[i][1],
                character_set[j][1],
            )
        )

with open(
    "data_settings/dataset/highkick_merged.txt", encoding="utf-8"
) as file:
    scripts = file.read()

scrips_per_scene = scripts.split("씬")

connection_weight = dict()
for scene in scrips_per_scene:
    for connection in connection_keys:
        character_1 = connection[0]
        character_2 = connection[1]
        if character_1 in scene and character_2 in scene:
            if connection not in connection_weight:
                connection_weight[connection] = 1
            else:
                connection_weight[connection] += 1

for key, value in connection_weight.items():
    source, target = key[2], key[3]
    weight = value
    if weight == 0:
        continue
    with app.app_context():
        source_id = (
            db.session.query(Character.id)
            .filter(Character.name == source)
            .all()[0][0]
        )
        target_id = (
            db.session.query(Character.id)
            .filter(Character.name == target)
            .all()[0][0]
        )
        connection = Connection(
            target=target_id, source=source_id, connection_weight=weight
        )
        db.session.add(connection)
        db.session.commit()

with open(
    "data_settings/dataset/origin_connection_data.json", "r", encoding="utf-8"
) as json_file:
    json_data = json.load(json_file)
    character_labels = dict()
    labels = json_data["node"]
    for label in labels:
        character_labels[label["data"]["id"]] = label["data"]["label"]
    character_labels["12"] = "홍순창(교감)"
    for con_data in json_data["edge_origin"]:
        data = con_data["data"]
        with app.app_context():
            target_id = (
                db.session.query(Character.id)
                .filter(Character.name == character_labels[data["target"]])
                .all()[0][0]
            )
            source_id = (
                db.session.query(Character.id)
                .filter(Character.name == character_labels[data["source"]])
                .all()[0][0]
            )
            origin_type = data["type"]

            connection = Connection(
                target=target_id, source=source_id, origin_type=origin_type,
            )
            db.session.add(connection)
            db.session.commit()

