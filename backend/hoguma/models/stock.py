from hoguma import db


class Stock(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    episode = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    character_id = db.Column(
        db.Integer,
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
    )
    character = db.relationship(
        "Character", backref=db.backref("stocks", lazy=True)
    )

    def __repr__(self):
        return f"""
            Stock id: {self.id}
            episode: {self.episode}
            weight: {self.weight}
            character id: {self.character_id}
        """
