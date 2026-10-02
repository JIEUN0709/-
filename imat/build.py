import html
Q = [
# (type, question, [options], answer_letter, explanation)
("문장 논리 · 부정", "“It is not true that every doctor in the hospital works at night.” Which of the following must be true?",
 ["No doctor in the hospital works at night.","At least one doctor in the hospital does not work at night.","At least one doctor in the hospital works at night.","Most doctors in the hospital work during the day.","Every doctor in the hospital works during the day."],
 "B","“모든 X가 Y이다”의 부정은 “적어도 하나의 X는 Y가 아니다”입니다. ‘아무도 ~하지 않는다(A)’는 지나치게 강한 진술이라 함정입니다."),
("문장 논리 · 필요조건", "“Marco takes the bus only if it is raining.” Today Marco took the bus. Which statement is certainly true?",
 ["It was raining today.","It was not raining today.","Whenever it rains, Marco takes the bus.","Marco never walks to work.","Nothing can be concluded."],
 "A","“Q only if P” = Q → P (P는 필요조건). 버스를 탔으므로(Q) 비가 왔다(P). C는 역(P → Q)이라 확정할 수 없습니다."),
("문장 논리 · 대우", "“If a patient has a fever, the patient is given paracetamol.” Which statement is logically equivalent?",
 ["If a patient is given paracetamol, the patient has a fever.","If a patient has no fever, the patient is not given paracetamol.","If a patient is not given paracetamol, the patient has no fever.","A patient either has a fever or is given paracetamol.","Only patients with a fever are given paracetamol."],
 "C","P → Q와 동치는 대우 ¬Q → ¬P 뿐입니다. A·E는 역, B는 이(裏)로 동치가 아닙니다."),
("삼단논법 · 집합", "All cardiologists are physicians. No physician is a pharmacist. Which statement must be true?",
 ["No cardiologist is a pharmacist.","Some pharmacists are cardiologists.","All physicians are cardiologists.","Some pharmacists are physicians.","No physician is a cardiologist."],
 "A","벤 다이어그램: 심장내과의 ⊂ 의사, 의사 ∩ 약사 = ∅ → 심장내과의 ∩ 약사 = ∅."),
("배열 추론", "Five students A, B, C, D and E sit in seats 1–5 (left to right). C sits in seat 3. A sits immediately to the left of B. D is not at either end. E sits somewhere to the right of C. Who sits in seat 1?",
 ["Student A","Student B","Student D","Student E","It cannot be determined."],
 "A","C=3 고정. D는 끝이 아니므로 2 또는 4, E는 4 또는 5. A-B 연속 쌍은 (1,2) 또는 (4,5)인데 (4,5)면 E 자리가 없음 → A=1, B=2, D=4, E=5."),
("수열", "What is the next number in the sequence?  2, 6, 12, 20, 30, …",
 ["36","40","42","44","48"],
 "C","차이가 4, 6, 8, 10 → 다음 차이 12. 또는 n(n+1): 6×7 = 42."),
("수열", "What is the next number in the sequence?  3, 5, 9, 17, 33, …",
 ["49","57","63","65","66"],
 "D","규칙: ×2 − 1 (차이 2, 4, 8, 16 → 다음 32). 33 + 32 = 65."),
("비율 · 퍼센트", "The price of a textbook is increased by 20% and then the new price is decreased by 20%. Compared with the original price, the final price is:",
 ["the same","4% higher","4% lower","2% lower","20% lower"],
 "C","1.2 × 0.8 = 0.96 → 4% 감소. 연속 퍼센트 변화는 더하지 말고 곱합니다."),
("작업량", "Pump A fills a tank in 6 hours; pump B fills the same tank in 3 hours. Working together, how long do they take?",
 ["1.5 hours","2 hours","2.5 hours","4.5 hours","9 hours"],
 "B","시간당 1/6 + 1/3 = 1/2 → 2시간. 빠른 펌프(3시간)보다 짧아야 하므로 C~E는 즉시 소거."),
("나이 문제", "Today a mother is three times as old as her son. In 12 years she will be twice as old as him. How old is the mother now?",
 ["24","30","36","42","48"],
 "C","M = 3S, M + 12 = 2(S + 12) → 3S + 12 = 2S + 24 → S = 12, M = 36. 선택지 대입(역산)이 더 빠를 때가 많습니다."),
("비례 · 의학 맥락", "A drug is prescribed at 15 mg per kg of body weight per day, divided into 3 equal doses. A child weighs 18 kg. How much is each dose?",
 ["45 mg","60 mg","90 mg","135 mg","270 mg"],
 "C","하루 총량 15 × 18 = 270 mg → 3회 분할 = 90 mg. E(하루 총량)는 단계 생략 함정."),
("확률", "A bag contains 3 red and 2 blue balls. Two balls are drawn without replacement. What is the probability that both are red?",
 ["3/10","9/25","2/5","3/5","6/25"],
 "A","3/5 × 2/4 = 6/20 = 3/10. B(9/25)는 복원추출로 착각한 함정."),
("자료 해석", "A clinic recorded the number of patients: January 120, February 150, March 180, April 150. Which statement is correct?",
 ["The largest percentage increase was from February to March.","The fall from March to April was 20%.","The mean monthly number of patients over the four months was 150.","April had 30% more patients than January.","The percentage rise from January to February equals the percentage fall from March to April."],
 "C","합 600 ÷ 4 = 150. 증가율: 1→2월 25%, 2→3월 20%, 3→4월 감소 16.7%. 절대값이 같아도(30명) 기준값이 다르면 %가 달라집니다."),
("비판적 사고 · 오류", "“People who drink green tea every day have lower rates of heart disease. Therefore, drinking green tea prevents heart disease.” Which best describes the flaw?",
 ["It relies on an unreliable source.","It assumes that a correlation shows a causal relationship.","It generalises from a single case.","It contradicts its own premise.","It uses a term in two different senses."],
 "B","상관관계 ≠ 인과관계. 녹차를 마시는 사람이 운동·식단 등 다른 건강 습관을 가졌을 수 있습니다(교란변수)."),
("비판적 사고 · 약화", "“Since the hospital introduced a new hand-washing policy, infection rates have fallen by 30%. So the policy caused the fall.” Which statement most weakens this argument?",
 ["Most staff say they support the policy.","At the same time, the hospital introduced a new sterilisation system for surgical instruments.","Infection rates in nearby hospitals rose during the same period.","The WHO recommends frequent hand washing.","The policy was cheap to introduce."],
 "B","같은 시기 다른 원인(대체 원인)의 존재가 인과 주장을 가장 약화. C는 오히려 강화, A·D·E는 무관."),
("요일 계산", "If 1 March of a certain year is a Tuesday, what day of the week is 1 April of the same year?",
 ["Wednesday","Thursday","Friday","Saturday","Sunday"],
 "C","3월은 31일 → 31 mod 7 = 3 → 화요일 + 3 = 금요일."),
("진실·거짓 퍼즐", "Of A, B and C, exactly one always lies and the other two always tell the truth. A: “B is the liar.” B: “C is not the liar.” C: “I am not the liar.” Who is the liar?",
 ["Person A","Person B","Person C","Either A or C","It cannot be determined."],
 "A","가정법: B가 거짓말쟁이면 B의 말이 거짓 → C도 거짓말쟁이(모순). C가 거짓말쟁이면 A의 말이 거짓(모순). A가 거짓말쟁이면 모든 진술이 일관됨."),
("집합 · 벤 다이어그램", "In a class of 40 students, 25 study Biology, 18 study Chemistry and 7 study neither. How many study both subjects?",
 ["3","7","10","11","15"],
 "C","40 − 7 = 33 = 25 + 18 − x → x = 10. 공식: |A∪B| = |A| + |B| − |A∩B|."),
("평균 속력", "A car travels 60 km at 30 km/h and returns the same 60 km at 60 km/h. What is its average speed for the whole journey?",
 ["40 km/h","42 km/h","45 km/h","48 km/h","50 km/h"],
 "A","총거리 120 km ÷ 총시간(2 + 1 = 3 h) = 40 km/h. 속력의 단순 평균(45)은 대표 함정. 조화평균 2ab/(a+b)."),
("코딩 · 패턴", "In a code, CAT is written as DBU. How is DOG written in the same code?",
 ["EPH","CNF","EPG","DPH","FQI"],
 "A","각 글자를 알파벳 +1 이동: D→E, O→P, G→H."),
]

def qhtml(i, q):
    t, s, opts, a, e = q
    li = "".join(f"<li><b>{chr(65+k)}</b>&nbsp; {html.escape(o)}</li>" for k, o in enumerate(opts))
    return f'<div class="q"><div class="qh"><span class="num">{i}</span><span class="tag">{t}</span></div><p>{html.escape(s)}</p><ol class="opts">{li}</ol></div>'

def ahtml(i, q):
    t, s, opts, a, e = q
    return f'<div class="a"><span class="num">{i}</span><span class="ans">정답 {a}</span><span class="tag">{t}</span><p>{e}</p></div>'

questions = "".join(qhtml(i+1, q) for i, q in enumerate(Q))
answers = "".join(ahtml(i+1, q) for i, q in enumerate(Q))
grid = "".join(f"<td><b>{i+1}</b> {q[3]}</td>" + ("</tr><tr>" if (i+1) % 10 == 0 and i+1 < len(Q) else "") for i, q in enumerate(Q))

tpl = open("template.html", encoding="utf-8").read()
out = tpl.replace("{{QUESTIONS}}", questions).replace("{{ANSWERS}}", answers).replace("{{GRID}}", grid)
open("imat_logic.html", "w", encoding="utf-8").write(out)
print("ok", len(Q))
