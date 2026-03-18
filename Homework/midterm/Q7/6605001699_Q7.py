answer_sheet = input("Choose your solution file: ").strip()
exam_sheet = input("Choose your exam file: ").strip()

def read_answer(filename):
	with open(filename, "r", encoding="utf-8") as file:
		content = file.read().strip()
	
	answers = content.split()
	return answers


def read_exam(filename):
	with open(filename, "r", encoding="utf-8") as file:
		lines = file.readlines() # อ่านทุกบรรทัดในไฟล์และเก็บไว้ในรูปแบบของ list ของ string
		# print(f"Exam lines: {lines}")  แสดงบรรทัดที่อ่านมาเพื่อการตรวจสอบ
		# Exam lines: ['A A D A D C C D A B\n', 'C A C A D C C D B C\n', 'A A B A D C B D A B\n', 
		# 'B A B A D C C C A B\n', 'A A D B D C B D A B\n', 'B A B A D C C C A C\n', 'A A D A D C C D A B\n', 
		# 'A A B A C C C D B B'] 
	result = []
	for line in lines:
		exam = line.strip().split() # ลบช่องว่างที่ไม่จำเป็นและแยกคำในแต่ละบรรทัดเป็น list ของ string
		result.append(exam)
	return result


def score_students(answer_key, students):
	scores = [] 
	for answers in students:
		correct = 0
		for i in range(len(answers)):
			if answers[i] == answer_key[i]:
				correct += 1
		scores.append(correct)
	return scores


answer_key = read_answer(answer_sheet)
students = read_exam(exam_sheet)
scores = score_students(answer_key, students)

print(f"Student score:{scores}")



