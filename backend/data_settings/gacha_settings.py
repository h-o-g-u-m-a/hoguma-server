from hoguma import db
from hoguma.models.gacha import Gacha
from hoguma.models.character import Character

import csv
from hoguma import create_app


app = create_app()

with open(
    "data_settings/dataset/gacha_data.csv", "r", encoding="utf-8",
) as file:
    csv_data = csv.reader(file)
    next(csv_data)
    for row in csv_data:
        with app.app_context():
            gacha_number = row[8]
            nickname = row[4]
            quote = row[3]
            question = row[5]
            description = row[6]
            character_id = (
                db.session.query(Character.id)
                .filter(Character.name == row[2])
                .all()[0][0]
            )

            gacha = Gacha(
                gacha_number=gacha_number,
                nickname=nickname,
                quote=quote,
                question=question,
                description=description,
                character_id=character_id,
            )
            db.session.add(gacha)
            db.session.commit()
