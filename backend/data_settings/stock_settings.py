from hoguma import db
from hoguma.models.stock import Stock
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

with open(
    "data_settings/dataset/character_stock.json", "r", encoding="utf-8"
) as json_file:
    stock_dict = json.load(json_file)

    for ch in character_set:
        with app.app_context():
            character_id = (
                db.session.query(Character.id)
                .filter(Character.name == ch[1])
                .all()[0][0]
            )
            stock_set = stock_dict[ch[0]]
            for episode, weight in stock_set.items():
                stock = Stock(
                    episode=episode, weight=weight, character_id=character_id
                )
                db.session.add(stock)
                db.session.commit()

