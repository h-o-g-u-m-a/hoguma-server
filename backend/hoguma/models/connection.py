from hoguma import db


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(
        db.Integer,
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
    )
    source = db.Column(
        db.Integer,
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
    )
    origin_type = db.Column(db.String(50))
    connection_weight = db.Column(db.Integer)

    def __repr__(self):
        return f"""
            Connection id: {self.id}
            target: {self.target}
            source: {self.source}
            origin_flag: {self.origin_flag}
            origin_type: {self.origin_type}
            connection_weight: {self.connection_weight}
        """
