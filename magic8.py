import random

name = "Mylo"
question = "Can I become the best software developer/engineer in the world?"
answer = ""

random_number = random.randint(1, 11)


if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "For sure KING"
elif random_number == 11:
  answer = "prolly not bruh"
else:
  answer = "Error"


if question == "":
  print("The Magic 8-Ball can not provide a fortune unless you ask it something.")
else:
  print(name + " asks:\n" + question)
  print("\nMagic 8-Ball's answer:\n" + answer)