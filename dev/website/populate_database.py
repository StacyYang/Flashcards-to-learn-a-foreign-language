# File to populate multiple-choice questions and true/false questions into database.
# Each questions will be checked before populating to database, Only new questions will be populated to database.

from .models import Quiz_M, Quiz_TF, Material
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
    {'language': 'Chinese', 'title': '智力', 'content': 'intelligence'},
    {"language": "Chinese", "title": "可能", "content": "likely"},
    {"language": "Chinese", "title": "回来", "content": "return"},
    {"language": "Chinese", "title": "社会", "content": "social"},
    {"language": "Chinese", "title": "结果", "content": "consequence"},
    {"language": "Chinese", "title": "药物", "content": "drug"},
    {"language": "Chinese", "title": "专家", "content": "expert"},
    {"language": "Chinese", "title": "延续", "content": "extend"},
    {"language": "Chinese", "title": "工业", "content": "industrial"},
    {"language": "Chinese", "title": "道德", "content": "moral"},
    {"language": "Chinese", "title": "行为", "content": "action"},
    {"language": "Chinese", "title": "成", "content": "adult"},
    {"language": "Chinese", "title": "雄心", "content": "ambition"},
    {"language": "Chinese", "title": "竞争", "content": "competition"},
    {"language": "Chinese", "title": "容量", "content": "capacity"},
    {"language": "Chinese", "title": " 细节", "content": "detail"},
    {"language": "Chinese", "title": "根据", "content": "evidence"},
    {"language": "Chinese", "title": "进化", "content": "evolution"},
    {"language": "Chinese", "title": "基金", "content": "fund"},
    {"language": "Chinese", "title": "通货膨胀", "content": "inflation"},
    {"language": "Chinese", "title": "当地", "content": "local"},
    {"language": "Chinese", "title": "维持", "content": "maintain"},
    {"language": "Chinese", "title": "经营", "content": "management"},
    {"language": "Chinese", "title": "生产力", "content": "productivity"},
    {"language": "Chinese", "title": "幸免", "content": "survive"},
    {"language": "Chinese", "title": "宇宙", "content": "universe"},
    {"language": "Chinese", "title": "学会", "content": "learn"},
    {"language": "Chinese", "title": "广告宣传", "content": "advertising"},
    {"language": "Chinese", "title": "影响", "content": "affect"},
    {"language": "Chinese", "title": "益处", "content": "benefit"},
    {"language": "Chinese", "title": "辩论", "content": "debate"},
    {"language": "Chinese", "title": "直", "content": "directly"},
    {"language": "Chinese", "title": "要素", "content": "element"},
    {"language": "Chinese", "title": "必不可少", "content": "essential"},
    {"language": "Chinese", "title": "把", "content": "identify"},
    {"language": "Chinese", "title": "想要", "content": "intend"},
    {"language": "Chinese", "title": "投资", "content": "investment"},
    {"language": "Chinese", "title": "合理", "content": "reasonable"},
    {"language": "Chinese", "title": "责任", "content": "responsibility"},
    {"language": "Chinese", "title": "时机", "content": "opportunity"},
    {"language": "Chinese", "title": "人格", "content": "personality"},
    {"language": "Chinese", "title": "私人", "content": "private"},
    {"language": "Chinese", "title": "改变", "content": "alter"},
    {"language": "Chinese", "title": "适当", "content": "appropriate"},
    {"language": "Chinese", "title": "叫喊声", "content": "boom"},
    {"language": "Chinese", "title": "联合", "content": "combine"},
    {"language": "Chinese", "title": "公司", "content": "corporation"},
    {"language": "Chinese", "title": "进取心", "content": "enterprise"},
    {"language": "Chinese", "title": "联邦", "content": "federal"},
    {"language": "Chinese", "title": "煤气", "content": "gas"},
    {"language": "Chinese", "title": "高", "content": "highly"},
    {"language": "Chinese", "title": "问题", "content": "issue"},
    {"language": "Chinese", "title": "团体", "content": "organization"},
    {"language": "Chinese", "title": "原理", "content": "principle"},
    {"language": "Chinese", "title": "计划", "content": "project"},
    {"language": "Chinese", "title": "认出", "content": "recognize"},
    {"language": "Chinese", "title": "特", "content": "specific"},
    {"language": "Chinese", "title": "结构", "content": "structure"},
    {"language": "Chinese", "title": "物质", "content": "substance"},
    {"language": "Chinese", "title": "趋势", "content": "trend"},
    {"language": "Chinese", "title": "活跃", "content": "activity"},
    {"language": "Chinese", "title": "优点", "content": "advantage"},
    {"language": "Chinese", "title": "外表", "content": "aspect"},
    {"language": "Chinese", "title": "态度", "content": "attitude"},
    {"language": "Chinese", "title": "使", "content": "balance"},
    {"language": "Chinese", "title": "特", "content": "characteristic"},
    {"language": "Chinese", "title": "声称", "content": "claim"},
    {"language": "Chinese", "title": "评论", "content": "comment"},
    {"language": "Chinese", "title": "组成", "content": "constitute"},
    {"language": "Chinese", "title": "订", "content": "contract"},
    {"language": "Chinese", "title": "创造", "content": "creative"},
    {"language": "Chinese", "title": "教养", "content": "culture"},
    {"language": "Chinese", "title": "历史", "content": "historical"},
    {"language": "Chinese", "title": "解释", "content": "interpret"},
    {"language": "Chinese", "title": "方式", "content": "manner"},
    {"language": "Chinese", "title": "大量", "content": "mass"},
    {"language": "Chinese", "title": "获得", "content": "obtain"},
    {"language": "Chinese", "title": "强大", "content": "powerful"},
    {"language": "Chinese", "title": "预告", "content": "predict"},
    {"language": "Chinese", "title": "风险", "content": "risk"},
    {"language": "Chinese", "title": "机器人", "content": "robot"},
    {"language": "Chinese", "title": "转移", "content": "shift"},
    {"language": "Chinese", "title": "种", "content": "species"},
    {"language": "Chinese", "title": "接近", "content": "approach"},
    {"language": "Chinese", "title": "争论", "content": "argument"},
    {"language": "Chinese", "title": "假定", "content": "assume"},
    {"language": "Chinese", "title": "计划", "content": "blueprint"},
    {"language": "Chinese", "title": "气候", "content": "climate"},
    {"language": "Chinese", "title": "好", "content": "competitive"},
    {"language": "Chinese", "title": "复杂", "content": "complex"},
    {"language": "Chinese", "title": "概念", "content": "concept"},
    {"language": "Chinese", "title": "使", "content": "confuse"},
    {"language": "Chinese", "title": "危急", "content": "critical"},
    {"language": "Chinese", "title": "天然", "content": "crude"},
    {"language": "Chinese", "title": "出现", "content": "emerge"},
    {"language": "Chinese", "title": "受雇", "content": "employee"},
    {"language": "Chinese", "title": "存在", "content": "existence"},
    {"language": "Chinese", "title": "新方法", "content": "innovation"},
    {"language": "Chinese", "title": "接见", "content": "interview"},
    {"language": "Chinese", "title": "使", "content": "involve"},
    {"language": "Chinese", "title": "定期", "content": "journal"},
    {"language": "Chinese", "title": "连接", "content": "link"},
    {"language": "Chinese", "title": "明显", "content": "manifest"},
    {"language": "Chinese", "title": "运动", "content": "motion"},
    {"language": "Chinese", "title": "显然", "content": "obvious"},
    {"language": "Chinese", "title": "执行", "content": "performance"},
    {"language": "Chinese", "title": "政策", "content": "policy"},
    {"language": "Chinese", "title": "可能", "content": "possibility"},
    {"language": "Chinese", "title": "压", "content": "pressure"},
    {"language": "Chinese", "title": "财产", "content": "property"},
    {"language": "Chinese", "title": "前景", "content": "prospect"},
    {"language": "Chinese", "title": "有", "content": "relate"},
    {"language": "Chinese", "title": "资源", "content": "resource"},
    {"language": "Chinese", "title": "源", "content": "source"},
    {"language": "Chinese", "title": "自杀", "content": "suicide"},
    {"language": "Chinese", "title": "进入", "content": "access"},
    {"language": "Chinese", "title": "取得", "content": "acquire"},
    {"language": "Chinese", "title": "使", "content": "adapt"},
    {"language": "Chinese", "title": "附加", "content": "additional"},
    {"language": "Chinese", "title": "贬", "content": "aggressive"},
    {"language": "Chinese", "title": "业余爱好", "content": "amateur"},
    {"language": "Chinese", "title": "分析", "content": "analysis"},
    {"language": "Chinese", "title": "申请", "content": "apply"},
    {"language": "Chinese", "title": "出现", "content": "arise"},
    {"language": "Chinese", "title": "假定", "content": "assumption"},
    {"language": "Chinese", "title": "使", "content": "assure"},
    {"language": "Chinese", "title": "权威", "content": "authority"},
    {"language": "Chinese", "title": "避免", "content": "avoid"},
    {"language": "Chinese", "title": "偏见", "content": "bias"},
    {"language": "Chinese", "title": "简洁", "content": "brief"},
    {"language": "Chinese", "title": "现金", "content": "cash"},
    {"language": "Chinese", "title": "向", "content": "challenge"},
    {"language": "Chinese", "title": "委员会", "content": "committee"},
    {"language": "Chinese", "title": "冲突", "content": "conflict"},
    {"language": "Chinese", "title": "考虑", "content": "consideration"},
    {"language": "Chinese", "title": "不断", "content": "constant"},
    {"language": "Chinese", "title": "消耗量", "content": "consumption"},
    {"language": "Chinese", "title": "与", "content": "contact"},
    {"language": "Chinese", "title": "大会", "content": "convention"},
    {"language": "Chinese", "title": "使", "content": "convince"},
    {"language": "Chinese", "title": "宇宙", "content": "cosmic"},
    {"language": "Chinese", "title": "资料", "content": "data"},
    {"language": "Chinese", "title": "定义", "content": "definition"},
    {"language": "Chinese", "title": "交付", "content": "delivery"},
    {"language": "Chinese", "title": "说明", "content": "demonstrate"},
    {"language": "Chinese", "title": "否认", "content": "deny"},
    {"language": "Chinese", "title": "数字", "content": "digital"},
    {"language": "Chinese", "title": "纪律", "content": "discipline"},
    {"language": "Chinese", "title": "差别", "content": "distinction"},
    {"language": "Chinese", "title": "教育", "content": "educate"},
    {"language": "Chinese", "title": "有效", "content": "effective"},
    {"language": "Chinese", "title": "电子", "content": "electronic"},
    {"language": "Chinese", "title": "强调", "content": "emphasis"},
    {"language": "Chinese", "title": "使", "content": "enable"},
    {"language": "Chinese", "title": "错误", "content": "error"},
    {"language": "Chinese", "title": "建立", "content": "establish"},
    {"language": "Chinese", "title": "广度", "content": "extent"},
    {"language": "Chinese", "title": "聚焦", "content": "focus"},
    {"language": "Chinese", "title": "功能", "content": "function"},
    {"language": "Chinese", "title": "根本", "content": "fundamental"},
    {"language": "Chinese", "title": "基因", "content": "gene"},
    {"language": "Chinese", "title": "天才", "content": "genius"},
    {"language": "Chinese", "title": "巨人", "content": "giant"},
    {"language": "Chinese", "title": "幽默", "content": "humo"},
    {"language": "Chinese", "title": "含意", "content": "implication"},
    {"language": "Chinese", "title": "增进", "content": "improvement"},
    {"language": "Chinese", "title": "独立自主", "content": "independent"},
    {"language": "Chinese", "title": "影响", "content": "influence"},
    {"language": "Chinese", "title": "本能", "content": "instinct"},
    {"language": "Chinese", "title": "意图", "content": "intention"},
    {"language": "Chinese", "title": "发明", "content": "invention"},
    {"language": "Chinese", "title": "条款", "content": "item"},
    {"language": "Chinese", "title": "机械", "content": "mechanism"},
    {"language": "Chinese", "title": "注意", "content": "observation"},
    {"language": "Chinese", "title": "古怪", "content": "odd"},
]


for quiz_question in quizzes_M:
    # Check if a question with the same text already exists in the database
    existing_question = Quiz_M.query.filter_by(question=quiz_question["question_text"]).first()
    if existing_question is None:
        new_question = Quiz_M(question=quiz_question["question_text"], option1=quiz_question["option1"], option2=quiz_question["option2"], 
                                option3=quiz_question["option3"], option4=quiz_question["option4"], answer=quiz_question["answer"], language=quiz_question['language'])
        db.session.add(new_question)

for quiz_question in quizzes_TF:
    # Check if a question with the same text already exists in the database
    existing_question = Quiz_TF.query.filter_by(question=quiz_question["question_text"]).first()
    if existing_question is None:
        new_question = Quiz_TF(question=quiz_question["question_text"], answer=quiz_question["answer"], language=quiz_question['language'])
        db.session.add(new_question)

for material in materials:
    # Check if a material with the same title already exists in the database
    existing_material = Material.query.filter_by(title=material["title"]).first()
    if existing_material is None:
        new_material = Material(title=material["title"], content=material["content"],language=quiz_question["language"])
        db.session.add(new_material)

for user in users:
    # Check if a user with the same username already exists in the database
    existing_user = User.query.filter_by(username=user["username"]).first()
    if existing_user is None:
        new_user = User(username=user["username"], email=user["email"], password=user["password"])
        db.session.add(new_user)

for s in scores:
    existing_s = Score.query.filter_by(id = s["id"]).first()
    if existing_s is None:
        new_score = Score(score=s["score"], user_id=s["user_id"])
        db.session.add(new_score)

# Commit the changes to the database
db.session.commit()

print("Quiz questions added to the database.")

