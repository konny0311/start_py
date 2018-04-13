h = input("身長(m)を入力")
w = input("体重(kg)を入力")

height = float(h)
weight = float(w)
bmi = weight / (height ** 2)

print("bmiは" + str(bmi) + "です。")
if bmi < 18.5:
    print("痩せ")
elif 18.5 <= bmi < 25:
    print("普通")
elif 25 <= bmi < 35:
    print("ちょっと太い")
else:
    print("めっちゃ太い")
