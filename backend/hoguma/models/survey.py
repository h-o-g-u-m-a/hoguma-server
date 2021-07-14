from hoguma import db


class Survey(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question_number = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    select_1 = db.Column(db.String(200), nullable=False)
    select_2 = db.Column(db.String(200), nullable=False)
    select_3 = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"""
                Survey id: {self.id}
                question_number: {self.question_number}
                question: {self.question}
                image: {self.image}
                select_1: {self.select_1}
                select_2: {self.select_2}
                select_3: {self.select_3}
            """


class SurveyResult(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    nick_name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pair = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""
                SurveyResult id: {self.id}
                nick_name: {self.nick_name}
                name: {self.name}
                image: {self.image}
                description: {self.description}
                pair: {self.pair}
            """
