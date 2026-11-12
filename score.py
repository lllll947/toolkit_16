# 学生成绩管理基础版
student_dict = {}

def add_student(name, score):
    student_dict[name] = score

def query_score(name):
    if name in student_dict:
        return f"【基础查询】学生{name}，分数：{student_dict[name]}"
    else:
        return "未查询到该学生信息"

if __name__ == "__main__":
    add_student("张三", 85)
    add_student("李四", 92)
    print(query_score("张三"))
     
