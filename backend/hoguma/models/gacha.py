from hoguma import db


class Gacha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gacha_number = db.Column(db.Integer, nullable=False)
    nickname = db.Column(db.Text, nullable=False)
    quote = db.Column(db.Text, nullable=False)
    question = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    character_id = db.Column(
        db.Integer,
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
    )
    character = db.relationship(
        "Character", backref=db.backref("gachas", lazy=True)
    )

    def __repr__(self):
        return f"""
            Gacha id: {self.id}
            nickname: {self.nickname}
            quote: {self.quote}
            question: {self.question}
            description: {self.description}
            gacha_number: {self.gacha_number}
            character id: {self.character_id}
        """
