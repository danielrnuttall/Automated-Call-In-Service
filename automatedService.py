import winsound

option = ""

def leaveQueries():
    winsound.PlaySound("leave_queries.wav", winsound.SND_FILENAME)
    option = input("")
    while (option == "9"):
        winsound.PlaySound("leave_queries.wav", winsound.SND_FILENAME)
        option = input("")

    if option == "0":
        welcomeVoice()
    elif option == "1":
        winsound.PlaySound("two_point_one.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("two_point_one.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            leaveQueries()

    elif option == "2":
        winsound.PlaySound("two_point_two.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("two_point_two.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            leaveQueries()

    elif option == "3":
        winsound.PlaySound("two_point_three.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("two_point_three.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            leaveQueries()

    elif option == "4":
        winsound.PlaySound("two_point_four.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("two_point_four.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            leaveQueries()

    elif option == "5":
        winsound.PlaySound("two_point_five.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("two_point_five.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            leaveQueries()
    

def unemploymentQueries():
    winsound.PlaySound("unemployment.wav", winsound.SND_FILENAME)
    winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
    option = input("")
    while (option == "9"):
        winsound.PlaySound("unemployment.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")

    if option == "0":
        welcomeVoice()
    elif option == "1":
        winsound.PlaySound("3_1.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("3_1.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            unemploymentQueries()

    elif option == "2":
        winsound.PlaySound("3_2.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("3_2.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            unemploymentQueries()

    elif option == "3":
        winsound.PlaySound("3_3.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("3_3.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            unemploymentQueries()

    elif option == "4":
        winsound.PlaySound("3_4.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("3_4.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            unemploymentQueries()
            
def healthAndSafetyQuerries():
    winsound.PlaySound("healthAndSafety.wav", winsound.SND_FILENAME)

    option = input("")
    while (option == "9"):
        winsound.PlaySound("healthAndSafety.wav", winsound.SND_FILENAME)
        option = input("")

    if option == "0":
        welcomeVoice()
    elif option == "1":
        winsound.PlaySound("4_1.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("4_1.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            healthAndSafetyQuerries()

    elif option == "2":
        winsound.PlaySound("4_2.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("4_2.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            healthAndSafetyQuerries()

    elif option == "3":
        winsound.PlaySound("4_3.wav", winsound.SND_FILENAME)
        winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
        option = input("")
        while (option == "9"):
            winsound.PlaySound("4_3.wav", winsound.SND_FILENAME)
            winsound.PlaySound("repeat_or_back.wav", winsound.SND_FILENAME)
            option = input("")
        if option == "0":
            healthAndSafetyQuerries()
    
def contactQuery():
    winsound.PlaySound("contact_details.wav", winsound.SND_FILENAME)
    option = input("")
    while (option == "9"):
        winsound.PlaySound("contact_details.wav", winsound.SND_FILENAME)
        option = input("")
    if option == "0":
        welcomeVoice()

def welcomeVoice():
    print("Welcome")
    winsound.PlaySound("welcome.wav", winsound.SND_FILENAME)
    option = input("")
    
    while option == "9":
        winsound.PlaySound("welcome.wav", winsound.SND_FILENAME)
        option = input("")

    if option == "1":
        leaveQueries()
            
    elif option == "2":
        unemploymentQueries()
    
    elif option == "3":   
        healthAndSafetyQuerries()

    elif option == "4":
        contactQuery()

        
        
def main():
    welcomeVoice()

if __name__ == "__main__":
    main()