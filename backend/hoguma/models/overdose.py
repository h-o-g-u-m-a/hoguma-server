from hoguma import db


class Overdose(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question_number = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    select_1 = db.Column(db.String(100), nullable=False)
    select_2 = db.Column(db.String(100), nullable=False)
    select_3 = db.Column(db.String(100), nullable=False)
    select_4 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"""
                Overdose id: {self.id}
                question_number: {self.question_number}
                question: {self.question}
                answer: {self.answer}
                select_1: {self.select_1}
                select_2: {self.select_2}
                select_3: {self.select_3}
                select_4: {self.select_4}
            """


class OverdoseResult(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""
                OverdoseResult id: {self.id}
                rank: {self.rank}
                image: {self.image}
                description: {self.description}
            """
