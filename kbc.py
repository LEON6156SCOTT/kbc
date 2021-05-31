from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if question['answer'] == answer:
        return 1
    return 0


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

    from random import choice
    print(f'\tQuestion {ques+1}: {QUESTIONS[ques]["name"]}' )
    print(f'\t\tOptions:')
    correct=QUESTIONS[ques]['answer']
    l=[1,2,3,4]
    l.remove(correct)
    x=choice(l)
    if correct>x:
        print(f"\t\t\tOption {x}: {QUESTIONS[ques]['option'+str(x)]}")
        print(f"\t\t\tOption {correct}: {QUESTIONS[ques]['option'+str(correct)]}")
    else:
        print(f"\t\t\tOption {correct}: {QUESTIONS[ques]['option'+str(correct)]}")
        print(f"\t\t\tOption {x}: {QUESTIONS[ques]['option'+str(x)]}")


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
    total_money = 0
    money_won = 0
    lifeline_valid = 1
    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    for i in range(0,15):
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        if ans.lower() == 'lifeline' and lifeline_valid and i != 14:
            lifeLine(i)
            lifeline_valid = 0
            while ans == "lifeline":
                print('No lifeline left')
                ans = input('Your choice ( 1-2) : ')
                if ans.lower() == 'quit':
                    break
        elif ans.lower() == 'lifeline' and lifeline_valid == False and i != 14:
            while ans == "lifeline":
                print('No lifeline left')
                ans = input('Your choice ( 1-4) : ')
                if ans.lower() == 'quit':
                    break



        # check for the input validations

        if ans.lower() == 'quit':
            print("Correct Answer: Option" , QUESTIONS[i]['answer'])
            print("Total Money Won: ", money_won)
            break

        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            total_money = QUESTIONS[i]['money']
            if i == 4:
                money_won = 10000
            elif i == 9:
                money_won = 320000
            print('\nCorrect !')

        else:
            # also print the correct answer
            print('\nIncorrect !')
            print("Correct Answer: Option" , QUESTIONS[i]['answer'])
            print("Total Money Won: ", money_won)
            break

        print("Money Won",total_money)

    # print the total money won in the end.


kbc()
