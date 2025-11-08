def collect_scores():
    print("Please enter the student's scores below. To leaVe input mode and start analysis enter -1.")
 
    #the list all of the scores will be in
    score_list = []

    #continuously asks for scores until -1 is inputted with each inputted score appended into score_list
    while(True):
        #call for user input
        score = input()

        #if exit value is entered break out of the loop
        if(score == "-1"): # note that exit value is "-1" not -1 because input is returned as string
            break
        #try to convert inputted string into integer before appending value into score_list
        try:
            score = int(score)
        #if unable to convert it informs the user and continue the loop
        except ValueError:
            print("Value was unable to be inputted. Please ensure to enter only number values!")
            continue

        #after converting the input from string to integer append value to the list we will return at the end
        score_list.append(score)

    #after exit value is inputted return the list where all the scores have gone into
    return score_list
   
#take in our list into analyze_scores function
def analyze_scores(score_list):
    print("Beginning Analysis...")

    #use built in python functions for lists to find the minimum, maximum, total values and find the number of scores in list
    num_students = len(score_list)
    total_score = sum(score_list)
    min_score = min(score_list)
    max_score = max(score_list)

    #calculate the average score by dividing the sum of all the scores and dividing by total number of scores/students
    average = total_score/num_students

    #print out analysis
    print(f"The average score of the {num_students} students was {average}.\nThe highest score was {max_score} and the lowest was {min_score}.")




print("Starting Analyzing Classroom Data Program...")

#set score list equal to the list that collect_scores will return
score_list = collect_scores()

#call analyze_scores with list that collect_scores returned
analyze_scores(score_list)