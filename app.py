#TOPIC: TYPE CONVERSION
# birth_year = int(input('Enter birth year to know your age: '))
# print(type(birth_year))
# age = 2025 - birth_year
# print(type(age))
# print(f'Your age is {age}')

#CLASSWORK
# print('To convert your weight in pounds to kilogram')
# weight = float(input(f'Enter your weights in pounds '))
# kilograms = weight * 0.453592
# print(f'Your weight in kilogram is {kilograms}')

#TEST1
# print('To calculate the time taken for your trip')
# distance = int(input('Enter your distance in km: '))
# speed = int(input('Enter your speed in km/h: '))
# time = distance / speed
# hour = int(time)
# minutes = int((time - hour) * 60)
# print(f'Time taken is {hour} hours {minutes} minutes')

#Project
# print('To calculate your body mass index')
# weight = float(input('Enter your weight in kg: '))
# height = float(input('Enter your height in meters: '))
# bmi = weight / height ** 2
# print(f'Your bmi is {bmi:.2f}')


#PROJECT2
print('To calculate your average score')
name = input('Enter your name ').capitalize()
first_subject = input('Enter your first subject ').capitalize()
first_score = int(input(f'Enter your {first_subject} score '))
sec_subject = input('Enter your second subject ').capitalize()
sec_score = int(input(f'Enter your {sec_subject} score '))
third_subject = input('Enter your third subject ').capitalize()
third_score = int(input(f'Enter your {third_subject} score '))
total_score = first_score + sec_score + third_score
average = total_score / 3
print(f'{name} your average score for {first_subject}, {sec_subject} and {third_subject} is {average:.2f}')