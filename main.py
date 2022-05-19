# Project #1: Flight Time
flight_speed = int(input())
flight_distance = int(input())

def flight_time(dist, sp): 
  # print(flight_distance/flight_speed)
  return (dist / sp)

print(flight_time(flight_distance, flight_speed))

# Project #2: Leaderboard
def leaderboard(): 
  print('''1.
2.
3.
4.
5.
6.
7.
8.
9.''')

print(leaderboard())

# Project #3: Tip Calculator
bill = int(input())
tip_amount = int(input())
tip_per = (tip_amount / 100)

def tip_calc(amt, tip): 
  result = (amt * tip)
  # print(result) 
  return result

print(tip_calc(bill, tip_per))

# Project #4: BMI Calculator
weight = int(input())
height = float(input())

def bmi_calc(w, h):

  bmi = (w / float(h * h))

  if bmi < 18.5:
    return
    # print('Underweight')
  if bmi >= 18.5 and bmi < 25:
    return "Normal"
    # print("Normal")
  if bmi >= 25 and bmi < 30:
    return "Overweight"
    # print("Overweight")
  if bmi >= 30:
    return "Obesity"
    # print("Obesity")

print(bmi_calc(weight, height))

# Project #5: Sum of Consecutive Numbers
N = int(input())
B = sum(range(0, N+1))

def consec_nums():
  print(y)

print(consec_nums(N, B))

# Project #6: Search Engine
text = input()
word = input()
def search(text, word):
	if word in text:
		return "Word found"
	else:
		return "Word not found"

print(search(text, word))