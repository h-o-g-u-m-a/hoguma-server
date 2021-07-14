from hoguma import db


class Word(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.String(50), nullable=False)
    word = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"""
            Word id: {self.id} 
            emotion: {self.emotion}
            word: {self.word}
        """
