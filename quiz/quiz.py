import json
import random
import sys

global answer

game_start = 1
points = 0
difficulity = ""
start = ""
answer = ""
bonus_1 = 1
bonus_2 = 1
bonus_3 = 1
########################################################### BONUSES FUNCTIONS ################################################################
########### BONUS 1 ###########
def bonus_1_function(question):
    global value_error_checker
    global bonus_1
    global answer
    #print("BONUSIK 1:", bonus_1)
    if bonus_1 != 2:
        bonus_1 = 0
    global answer_50_50_1
    global answer_50_50_2
    bonus_3_choice_yes_no = ""
    answer_50_50_1 = -1
    answer_50_50_2 = -2
    if question["prawidlowa_odpowiedz"] == "a":
        id_correct_answer = 1
    if question["prawidlowa_odpowiedz"] == "b":
        id_correct_answer = 2
    if question["prawidlowa_odpowiedz"] == "c":
        id_correct_answer = 3
    if question["prawidlowa_odpowiedz"] == "d":
        id_correct_answer = 4

    answer_50_50_random = random.randint(1, 2)
    if answer_50_50_random == 1:
        answer_50_50_1 = id_correct_answer
        while True:
            answer_50_50_2 = random.randint(1, 4) 
            if answer_50_50_2 != answer_50_50_1:
                break
    else: 
        answer_50_50_2 = id_correct_answer
        while True:
            answer_50_50_1 = random.randint(1, 4) 
            if answer_50_50_1 != answer_50_50_2:
                break 

    print("Użyto koła ratunkowego nr 1.|50 na 50|")
    print("-------------------------------------------------------------------")
    print()
    print(question["pytanie"])
    if answer_50_50_1 == 1 or answer_50_50_2 == 1:
        print("a:", question["a"])
    if answer_50_50_1 == 2 or answer_50_50_2 == 2:
        print("b:", question["b"])
    if answer_50_50_1 == 3 or answer_50_50_2 == 3:
        print("c:", question["c"])
    if answer_50_50_1 == 4 or answer_50_50_2 == 4:
        print("d:", question["d"])
    print()
    print("-------------------------------------------------------------------")

    if answer_50_50_1 == 1:
        answer_50_50_1 = "a"
    if answer_50_50_1 == 2:
        answer_50_50_1 = "b"
    if answer_50_50_1 == 3:
        answer_50_50_1 = "c"
    if answer_50_50_1 == 4:
        answer_50_50_1 = "d"

    if answer_50_50_2 == 1:
        answer_50_50_2 = "a"
    if answer_50_50_2 == 2:
        answer_50_50_2 = "b"
    if answer_50_50_2 == 3:
        answer_50_50_2 = "c"
    if answer_50_50_2 == 4:
        answer_50_50_2 = "d"

    value_error_checker = -1

    while(value_error_checker == -1):
            answer = input("Wybierz odpowiedź lub użyj koła: ")
            if answer == answer_50_50_1 or answer == answer_50_50_2 or (answer == "2" and bonus_2 == 1) or (answer == "3" and bonus_3 == 1):
                if answer != "3":
                    value_error_checker = 1
                if answer == answer_50_50_1 or answer == answer_50_50_2:
                    return answer
                if answer == "2" and bonus_2 == 1:
                    bonus_1 = 2
                    bonus_2_function(question)
                    return answer
                if answer == "3" and bonus_3 == 1:
                    print("Czy na pewno chcesz użyć koła ratunkowego nr 3.|Pominięcie pytania|?")
                    bonus_3_choice_yes_no = input('Wpisz "tak" lub "nie": ')
                    if bonus_3_choice_yes_no == "tak":
                        bonus_3_function()
                        return answer
                    else:
                        continue
            elif (answer == "1" and bonus_1 == 0) or (answer == "2" and bonus_2 == 0) or (answer == "3" and bonus_3 == 0):
                print('Wpisane koło ratunkowe zostało już użyte!')
            else:
                print('Wpisano nieprawidłową wartość. Proszę wybrać odpowiedź spośród: "' + answer_50_50_1 + '" "' + answer_50_50_2 + '" lub użyć dostępnych kół ratunkowych: "2, 3".')
########### BONUS 2 ###########
def bonus_2_function(question):
    global value_error_checker
    global bonus_2
    global bonus_1
    global answer
    global answer_50_50_1
    global answer_50_50_2
    bonus_3_choice_yes_no = ""
    bonus_2 = 0
    for i in range(1, 3):
        #print("ANSWER1:", answer)
        #print(type(answer))
        #print("BONUS_1:", bonus_1)
        #print("BONUS_2:", bonus_2)
        if i == 2 and answer != "1" and answer != "3":
            print("Niestety to zła odpowiedź. Masz jeszcze jedną próbę")
        answer = ""
        print("-------------------------------------------------------------------")
        print()
        # if i == 2 and answer != "1" and answer != "3" and (bonus_1 == 2 or bonus_1 != 2):
        #     print("Niestety to zła odpowiedź. Masz jeszcze jedną próbę()")
        # answer = ""
        # print("-------------------------------------------------------------------")
        # print()
        if i == 1 and bonus_1 != 2 :
            print("Użyto koła ratunkowego nr 2.|2 próby na odpowiedź|")
        if bonus_2 != 2:
            print(question["pytanie"])
            print("a:", question["a"])
            print("b:", question["b"])
            print("c:", question["c"])
            print("d:", question["d"])
            print()                 
            print("-------------------------------------------------------------------")

        if bonus_1 == 2 or bonus_2 == 2:
            if i == 1:
                print("Użyto koła ratunkowego nr 2.|2 próby na odpowiedź|")
                print("Użyto koła ratunkowego nr 1.|50 na 50|")
            print("-------------------------------------------------------------------")
            print()
            print(question["pytanie"])
            if answer_50_50_1 == "a" or answer_50_50_2 == "a":
                print("a:", question["a"])
            if answer_50_50_1 == "b" or answer_50_50_2 == "b":
                print("b:", question["b"])
            if answer_50_50_1 == "c" or answer_50_50_2 == "c":
                print("c:", question["c"])
            if answer_50_50_1 == "d" or answer_50_50_2 == "d":
                print("d:", question["d"])
            print()
            print("-------------------------------------------------------------------")
            while(value_error_checker == -1):
                answer = input("Wybierz odpowiedź lub użyj koła: ")
                #print("TU?")
                if answer == answer_50_50_1 or answer == answer_50_50_2 or (answer == "3" and bonus_3 == 1):
                    value_error_checker = 1
                    if answer == answer_50_50_1 or answer == answer_50_50_2:
                        return answer
                    if answer == "3" and bonus_3 == 1:
                        bonus_3_function()
                        return answer

        value_error_checker = -1

        while(value_error_checker == -1):
            answer = input("Wybierz odpowiedź lub użyj koła: ")
            #print("ANSWER:", answer)
            if answer == "a" or answer == "b" or answer == "c" or answer == "d" or (answer == "1" and bonus_1 == 1) or (answer == "3" and bonus_3 == 1):
                if answer != "3":
                    value_error_checker = 1
                #print("TUTAJ?")
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if(answer == question["prawidlowa_odpowiedz"]):
                        return answer
                    else: 
                        break
            if answer == "1" and bonus_1 == 1:
                bonus_2 = 2
                bonus_1_function(question) 
                if answer == question["prawidlowa_odpowiedz"]:
                    return answer
            if answer == "3" and bonus_3 == 1:
                print("Czy na pewno chcesz użyć koła ratunkowego nr 3.|Pominięcie pytania|?")
                while(bonus_3_choice_yes_no != "tak" or bonus_3_choice_yes_no != "nie"):
                    bonus_3_choice_yes_no = input('Wpisz "tak" lub "nie": ')
                    if bonus_3_choice_yes_no == "tak":
                        bonus_3_function()
                        return answer
                    elif bonus_3_choice_yes_no == "nie": 
                        break  
                    else:
                        print('Proszę wpisać "tak" lub "nie": ')    
            elif (answer == "1" and bonus_1 == 0) or (answer == "2" and bonus_2 == 0) or (answer == "3" and bonus_3 == 0):
                print('Wpisane koło ratunkowe zostało już użyte!')
            else:
                print('Wpisano nieprawidłową wartość. Proszę wybrać odpowiedź spośród: "a, b, c, d" lub użyć dostępnych kół ratunkowych: "1, 3".')
########### BONUS 3 ###########
def bonus_3_function():
    global bonus_3
    bonus_3 = 0
    print("Użyto koła ratunkowego nr 3.|Pominięcie pytania|")
########################################################### ################ ###########################################################
def show_question(question):
    global points
    global bonus_1
    global bonus_2
    global bonus_3
    value_error_checker = -1

    print("-------------------------------------------------------------------")
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()
    print("Koła ratunkowe: ")
    print("1.|50 na 50|   2.|2 próby na odpowiedź|   3.|Pominięcie pytania|")
    print()
    print("-------------------------------------------------------------------")

    while(value_error_checker == -1):
        answer = input("Wybierz odpowiedź lub użyj koła: ")
        if answer == "a" or answer == "b" or answer == "c" or answer == "d" or (answer == "1" and bonus_1 == 1) or (answer == "2" and bonus_2 == 1) or (answer == "3" and bonus_3 == 1):
            value_error_checker = 1
        elif (answer == "1" and bonus_1 == 0) or (answer == "2" and bonus_2 == 0) or (answer == "3" and bonus_3 == 0):
            print('Wpisane koło ratunkowe zostało już użyte!')
        elif (answer == "1" and bonus_1 == 2) or (answer == "2" and bonus_2 == 2):
            print('Wpisane koło ratunkowe zostało już użyte!')
        else:
            print('Wpisano nieprawidłową wartość. Proszę wybrać odpowiedź spośród: "a, b, c, d" lub użyć dostępnych kół ratunkowych: "1, 2, 3".')
        if difficulity == "classic":
            if answer == "1" and bonus_1 == 1:
                answer = bonus_1_function(question)

            if answer == "2" and bonus_2 == 1:
                answer = bonus_2_function(question)

            if answer == "3" and bonus_3 == 1:
                bonus_3_function()
        if difficulity == "hard" or difficulity == "hardcore":
            if answer == "1" or answer == "2" or answer == "3":
                value_error_checker = -1
                print("Nie możesz używać kół ratunkowych!")
    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedź! Liczba posiadanych punktów:", points)
    if answer != question["prawidlowa_odpowiedz"] and answer != "1" and answer != "2" and answer != "3":
        if difficulity == "hardcore":
            print(str(answer) + " to niestety zła odpowiedź. Prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")
            print("  ------------ ")
            print("|              |")
            print("| Przegrywasz! |")
            print("|              |")
            print("  ------------ ") 
            sys.exit(0)
        if difficulity != "hardcore":
            points -= 1
            print(str(answer) + " to niestety zła odpowiedź. Prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")

with open("quiz.json", encoding='utf-8') as json_file:
    questions = json.load(json_file)
    
    
    print()
    print()
    print()
    print()
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Witaj w quizie!")
    print("<> Za każdą prawidłową odpowiedź otrzymujesz 1 punkt, zaś za źle udzieloną odpowiedź tracisz 1 punkt.")
    print('<> Przy każdym pytaniu należy wpisać odpowiedź sposród: "a, b, c ,d" lub użyć dostępnych kół ratunkowych: "1, 2, 3".')
    print("<> Masz do dyspozycji 3 jednorazowe koła ratunkowe: 1.|50 na 50|   2.|2 próby na odpowiedź|   3.|Pominięcie pytania|. Koła można ze sobą łączyć.")
    print()
    print("     Wybierz poziom trudności:")
    print("     1. Classic (Masz dostępne wszystkie koła ratunkowe).")
    print("     2. Hard (Nie masz dostępnych kół ratunkowych).")
    print("     3. Hardcore (Nie masz dostępnych kół ratunkowych, za błędnie udzieloną odpowiedź natychmiast PRZEGRYWASZ).")
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    while(difficulity != "classic" and difficulity != "hard" and difficulity != "hardcore"):
        difficulity = input("Wpisz nazwę (classic, hard, hardcore): ")
        if difficulity == "1":
            difficulity = "classic"
        if difficulity == "2":
            difficulity = "hard"
        if difficulity == "3":
            difficulity = "hardcore"
        #start = input('Wpisz "start", aby rozpocząć quiz: ')
        if(difficulity != "classic" and difficulity != "hard" and difficulity != "hardcore"):
            print("Wpisano nieprawidłową wartość!")
        if(difficulity == "classic" or difficulity == "hard" or difficulity == "hardcore"):
            if difficulity == "classic":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                             Wybrano poziom Classic!"                                                               ) 
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("")
            if difficulity == "hard":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                             Wybrano poziom Hard!"                                                                  ) 
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("")
            if difficulity == "hardcore":
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                             Wybrano poziom Hardcore!"                                                              ) 
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("")
            for i in range(0, len(questions)):
                show_question(questions[i])
                    
print()
if difficulity != "hardcore":
    print("To koniec gry, zdobyta liczba punktów to " + str(points) + ".")
print()