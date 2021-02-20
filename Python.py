# Date: 20 Feb 2021
# Multiple Choice Questions for Python Class Participants of "Hour of Code (Hong Kong)"

# Formats (Space, line, divider, etc)
space1 = " "
space2 = "  "
space3 = "   "
space4 = "    "
space5 = "     "
space6 = "      "
space7 = "       "
space8 = "        "
line5  = "====="
divider = space7*2 + line5*19 + "\n"
                                                                                                                                  
# Banner
first_row  = space5*9 + "Hour of Code (Hong Kong) - Python \n\n"
second_row = space5*6 + "\"Multiple Choice\", \"True or False\" & \"Fill in Blank\" Type Questions \n"
print("\n" + first_row + second_row)
print(divider)
name = input(space7*3 + "Please input your name:" + space5)
print("\n" + divider)

# Checking answers
score = 0
response = 0
def check_guess(guess, answer):
    global score
    global response
    response = response + 1   
    if guess.lower() == answer.lstrip('0123456789.') :
        score = score + 1
        print(space7*6 + "Correct! \n\n" + divider)
    else:
        print(space7*6 + "Incorrect!  The correct answer is \"" + answer + "\".\n\n" + divider)

# Questions, choices and answers
q_file     = open("Python_1_Questions.txt")
mc_file    = open("Python_2_Choices.txt")
a_file     = open("Python_3_Answers.txt")
q_content  = q_file.read()
mc_content = mc_file.read()
a_content  = a_file.read()
question   = q_content.splitlines()
choice     = mc_content.splitlines()
answer     = a_content.splitlines()

for i in range(len(question)):
   question_part =  space7*2 + question[i]                     + "\n\n"
   choice_part   =  space7*2 + choice[i].lstrip('0123456789')  + "\n\n"
   answer_part   =  space7*6 + "Your answer is :"              + space5
   guess = input(question_part + choice_part + answer_part)
   check_guess(guess, answer[i].lstrip('0123456789.'))

# Scoring 
print(space7*3 + "Your total score:" , score , "out of" , response, "\n")

if score == response:
    print (space7*3 + name +":" + space3 + "Perfect!")
elif score >= float(response * 8/10):
    print (space7*3 + name +":" + space3 + "Well done!")
elif score >= float(response * 6/10):
    print (space7*3 + name +":" + space3 + "Pass!")
else:
    print (space7*3 + name +":" + space3 + "Keep practising more!")

mark_perfect   =  space7*3 + " 100% - Perfect \n"
mark_well_done =  space7*3 + ">=80% - Well done \n"
mark_pass      =  space7*3 + ">=60% - Pass \n"
mark_more      =  space7*3 + " <60% - Keep practising more \n"

print("\n" + mark_perfect + mark_well_done + mark_pass + mark_more)
print(divider)

# For termination in Python console
input( space7*2 + "Please press \"ENTER\" key to exit (N.B. Only applicable to Python Console Mode) :)")
