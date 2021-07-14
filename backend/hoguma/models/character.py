from hoguma import db


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(50), nullable=False)
    quote = db.Column(db.Text, nullable=False)
    word_cloud = db.Column(db.String(200), nullable=False)
    youtube = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"""
            Character id: {self.id} 
            name: {self.name}
            age: {self.age}
            job: {self.job}
            quote: {self.quote}
            word_cloud: {self.word_cloud}
            youtube: {self.youtube}
        """
