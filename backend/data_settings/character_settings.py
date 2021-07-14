from hoguma import db
from hoguma.models.character import Character
from hoguma import create_app

app = create_app()

import csv

with open(
    "data_settings/dataset/highkick_character_data.csv", "r", encoding="utf-8",
) as file:
    csv_data = csv.reader(file)
    for i in range(3):
        next(csv_data)
    for row in csv_data:
        with app.app_context():
            character = Character(
                name=row[2],
                image=f"{row[2]}.png",
                age=row[4],
                job=row[3],
                quote=row[5],
                word_cloud=f"{row[2]}.png",
                youtube=row[6],
            )
            db.session.add(character)
            db.session.commit()
