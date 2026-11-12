# 学生成绩管理拓展版
student_dict = {}

def add_student(name, score):
    student_dict[name] = score

def query_score(name):
    if name in student_dict:
        return f"【成绩查询】{name}同学分数为：{student_dict[name]}"
    else:
        return "未查询到该学生信息"

def get_avg_score():
    if len(student_dict) == 0:
        return 0
    return sum(student_dict.values()) / len(student_dict)

if __name__ == "__main__":
    add_student("张三", 85)
    add_student("李四", 92)
    print(query_score("张三"))
    print(f"班级平均分：{get_avg_score():.2f}")
