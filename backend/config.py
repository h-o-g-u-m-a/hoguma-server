db_info = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "port": 3306,
    "database": "hoguma",
}

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "SECRET KEY"
CHARACTER_DETAIL_URI = "character_detail"
OVERDOSE_URI = "overdose"
SURVEY_QUESTION_URI = "survey_question"
SURVEY_RESULT_URI = "survey_result"
WORD_CLOUD_URI = "word_cloud"
