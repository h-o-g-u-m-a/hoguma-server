from hoguma import db
from hoguma.models.emotion import Emotion
from hoguma.models.character import Character
import json
from hoguma import create_app

app = create_app()

character_dict = {
    "문희": "나문희",
    "순재": "이순재",
    "준하": "이준하",
    "민용": "이민용",
    "민호": "이민호",
    "윤호": "이윤호",
    "해미": "박해미",
    "범": "김범",
    "유미": "강유미",
    "찬성": "황찬성",
    "개성댁": "개성댁",
    "신지": "신지",
    "민정": "서민정",
    "교감": "홍순창(교감)",
}

with open(
    "data_settings/dataset/character_emotion_count.json", "r", encoding="utf-8"
) as json_file:
    emotion_dict = json.load(json_file)
    for key, value in emotion_dict.items():
        with app.app_context():
            character_id = (
                db.session.query(Character.id)
                .filter(Character.name == character_dict[key])
                .all()[0][0]
            )
            joy = round(value["기쁨"])
            sadness = round(value["슬픔"])
            anger = round(value["분노"])

            emotion = Emotion(
                joy=joy,
                anger=anger,
                sadness=sadness,
                character_id=character_id,
            )
            db.session.add(emotion)
            db.session.commit()

