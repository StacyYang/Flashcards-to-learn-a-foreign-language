# File to populate multiple-choice questions and true/false questions into database.
# Each questions will be checked before populating to database, Only new questions will be populated to database.

from .models import Quiz_M, Quiz_TF，Material
from . import db


quizzes_M = [
    {
        'language': 'Chinese',
        'question_text': 'What is the correct translation for "telephone"?',
        'option1': '雨伞',
        'option2': '自行车',
        'option3': '电话',
        'option4': '水',
        'answer': '电话'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "Good morning"?',
        'option1': '再见',
        'option2': '晚上好',
        'option3': '下午好',
        'option4': '早上好',
        'answer': '早上好'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "Goodbye"?',
        'option1': '再见',
        'option2': '晚上好',
        'option3': '下午好',
        'option4': '早上好',
        'answer': '再见'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "Good afternoon"?',
        'option1': '再见',
        'option2': '晚上好',
        'option3': '下午好',
        'option4': '早上好',
        'answer': '下午好'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "Good evening"?',
        'option1': '再见',
        'option2': '晚上好',
        'option3': '下午好',
        'option4': '早上好',
        'answer': '晚上好'
    },
    {   
        'language': 'Chinese',
        'question_text': 'What is the correct translation for "Please"?',
        'option1': '对不起',
        'option2': '请',
        'option3': '你好',
        'option4': '左转',
        'answer': '请'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "Thank you"?',
        'option1': '谢谢',
        'option2': '晚上好',
        'option3': '下午好',
        'option4': '早上好',
        'answer': '谢谢'
    },
    {   
        'language': 'Chinese',
        'question_text': 'What is the correct translation for "Thank you very much“？',
        'option1': '不好意思',
        'option2': '我不知道',
        'option3': '干杯',
        'option4': '非常感谢',
        'answer': '非常感谢'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "water"?',
        'option1': '水',
        'option2': '牛奶',
        'option3': '果汁',
        'option4': '咖啡',
        'answer': '水'
    },
    {   
        'language': 'Chinese',
        'question_text': 'How do you say "hospital"?',
        'option1': '医院',
        'option2': '学校',
        'option3': '动物园',
        'option4': '公园',
        'answer': '医院'
    }
]


quizzes_TF = [
    {   
        'language': 'Chinese',
        "question_text": "when the tone of a chinese character is changed its meaning changes",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "长城是世界上最长的建筑。",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "妈妈是女生。",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "黄河水是黄色的。",
        "answer": 'False'
    },
    {   
        'language': 'Chinese',
        "question_text": "猫咪可以被翻译成 kitty 和 cat.",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "狗可以被翻译成puppy 和 dog.",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "The Chinese language does not require punctuation.",
        "answer": 'False'
    },
    {   
        'language': 'Chinese',
        "question_text": "Tiger 翻译为 ”老虎“。 ",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "有时一个英文单词可以有多个中文翻译。",
        "answer": 'True'
    },
    {   
        'language': 'Chinese',
        "question_text": "可以用汉字来写出数字.",
        "answer": 'True'
    }

]

materials = [
    {'language': 'Chinese', 'title': '过程', 'content': 'process'}, 
    {'language': 'Chinese', 'title': '增加', 'content': 'growth'}, 
    {'language': 'Chinese', 'title': '工艺', 'content': 'technology'}, 
    {'language': 'Chinese', 'title': '理论', 'content': 'theory'}, 
    {'language': 'Chinese', 'title': '经济', 'content': 'economy'}, 
    {'language': 'Chinese', 'title': '行为', 'content': 'behavior'}, 
    {'language': 'Chinese', 'title': '账', 'content': 'account'}, 
    {'language': 'Chinese', 'title': '经济', 'content': 'economic'}, 
    {'language': 'Chinese', 'title': '单独', 'content': 'individual'}, 
    {'language': 'Chinese', 'title': '产品', 'content': 'product'}, 
    {'language': 'Chinese', 'title': '比', 'content': 'rate'}, 
    {'language': 'Chinese', 'title': '创造', 'content': 'create'}, 
    {'language': 'Chinese', 'title': '下降', 'content': 'decline'}, 
    {'language': 'Chinese', 'title': '硬', 'content': 'hard'}, 
    {'language': 'Chinese', 'title': '能力', 'content': 'ability'}, 
    {'language': 'Chinese', 'title': '专业', 'content': 'professional'}, 
    {'language': 'Chinese', 'title': '斑点', 'content': 'spot'}, 
    {'language': 'Chinese', 'title': '倾向', 'content': 'tend'}, 
    {'language': 'Chinese', 'title': '眼界', 'content': 'view'}, 
    {'language': 'Chinese', 'title': '鼓吹', 'content': 'advocate'}, 
    {'language': 'Chinese', 'title': '数量', 'content': 'amount'}, 
    {'language': 'Chinese', 'title': '团体', 'content': 'community'}, 
    {'language': 'Chinese', 'title': '关联', 'content': 'concern'}, 
    {'language': 'Chinese', 'title': '环境', 'content': 'environment'}, 
    {'language': 'Chinese', 'title': '因素', 'content': 'factor'}, 
    {'language': 'Chinese', 'title': '智力', 'content': 'intelligence'}]


for quiz_question in quizzes_M:
    # Check if a question with the same text already exists in the database
    existing_question = Quiz_M.query.filter_by(question=quiz_question["question_text"]).first()
    if existing_question is None:
        new_question = Quiz_M(question=quiz_question["question_text"], option1=quiz_question["option1"], option2=quiz_question["option2"], 
                                option3=quiz_question["option3"], option4=quiz_question["option4"], answer=quiz_question["answer"])
        db.session.add(new_question)

for quiz_question in quizzes_TF:
    # Check if a question with the same text already exists in the database
    existing_question = Quiz_TF.query.filter_by(question=quiz_question["question_text"]).first()
    if existing_question is None:
        new_question = Quiz_TF(question=quiz_question["question_text"], answer=quiz_question["answer"])
        db.session.add(new_question)

for material in materials:
    # Check if a material with the same title already exists in the database
    existing_material = Material.query.filter_by(title=material["title"]).first()
    if existing_material is None:
        new_material = Material(title=material["title"], content=material["content"],language=quiz_question["language"])
        db.session.add(new_material)

# Commit the changes to the database
db.session.commit()

print("Quiz questions added to the database.")

