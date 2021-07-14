from hoguma import db
from hoguma.models.word import Word

import csv
from hoguma import create_app


app = create_app()

with open(
    "data_settings/dataset/word_data.csv", "r", encoding="utf-8"
) as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data)
    for row in csv_data:
        word_dict = {"기쁨": row[0], "슬픔": row[1], "분노": row[2]}

        for emotion, value in word_dict.items():
            with app.app_context():
                _word = Word(emotion=emotion, word=value)

                db.session.add(_word)
                db.session.commit()
