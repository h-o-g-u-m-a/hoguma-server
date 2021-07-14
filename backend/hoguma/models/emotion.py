from hoguma import db


class Emotion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    joy = db.Column(db.Integer, nullable=False)
    anger = db.Column(db.Integer, nullable=False)
    sadness = db.Column(db.Integer, nullable=False)
    character_id = db.Column(
        db.Integer,
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
    )
    character = db.relationship(
        "Character", backref=db.backref("emotions", lazy=True)
    )

    def __repr__(self):
        return f"""
            Emotion id: {self.id}
            happy: {self.happy}
            anger: {self.anger}
            sadness: {self.sadness}
            character id: {self.character_id}
        """
