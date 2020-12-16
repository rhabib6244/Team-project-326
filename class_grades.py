from argparse import ArgumentParser
import sys
import pandas as pd
from base64 import main


class CalculateGrades:
    """Calculates the grades from the default file.
    It will assign attributes that will be used in other methods. 

    Attributes:
    -Assignments (list): list of the assignments category scores
    -Homeworks (list): list of the homework category scores
    -Quizzes (list): list of the quizzes category scores
    -Midterm(list): list of the midterm category scores
    -Final(list): list of the final category scores
    """
    
    
    def __init__(self, scores): 
        """ Assigns attributes that will
        be used in other methods.
        """
        
        self.scores = scores
        self.quizzes = scores["quizzes"]
        self.homeworks = scores["homeworks"]
        self.assignments = scores["assignments"]
        self.midterm = scores["midterm"]
        self.final = scores["final"]
        self.scores_dropped = {}
        
    
    def drop_score(self):
        """Drops the lowest score from each
        list/category excluding the exam category. Looks through each list and 
        deletes/pops the lowest score. Then calculates the average score of 
        each category after.
        
        Arguments:
        Assignments (list): contains all assignment grades (list of integers)
        Homework (list): contains all homework grades (list of integers)
        Quizzes (list): contains all quiz grades (list of integers)
        Midterm (list): contains all midterm grades (list of integers)
        
        Return:
        New_scores(dict): Dictionary where the keys are the categories and 
        the values are the average scores for each category
        after the lowest score has been dropped. 
        """
        
        scores_dropped = self.scores_dropped
        
        #Converting string to integer
        for quiz in self.quizzes:
            quiz=float(quiz)
            
        for home in self.homeworks:
             home=float(home)
        
        for assign in self.assignments:
            assign = float(assign)
            
        for midt in self.midterm:
            midt = float(midt)

        
        
        quizzes = self.quizzes[:]
        homeworks = self.homeworks[:]
        assignments = self.assignments[:]
        midterm = self.midterm[:]
        final = self.final[:]
        
        #Sorting each category
        lower_quizzes = sorted(quizzes)
        lower_homeworks = sorted(homeworks)
        lower_assignments = sorted(assignments)
        lower_midterm = sorted(midterm)
        
        #dropping the lower score of each category
        quizzes.remove(lower_quizzes[0])
        homeworks.remove(lower_homeworks[0])
        assignments.remove(lower_assignments[0])
        midterm.remove(lower_midterm[0])
            
        #Adding each list into the dictionary    
        scores_dropped["quizzes"] = quizzes
        scores_dropped["homeworks"] = homeworks
        scores_dropped["assignments"] = assignments
        scores_dropped["midterm"] = midterm
        scores_dropped["final"] = final
        
        return scores_dropped
                
        
        
    def final_grade(self):
        """Calculates the user's final 
        grade based on their average score for each category and weight of each
        category.

        Argument:
        New_scores (dict): Dictionary where the keys (strings) are the categories and 
        the values are the average scores (integers) for each category
        after the lowest score has been dropped.
    
        Returns:
        Final_grade (int): The students final grade for the course. 
        Letter_grade (str): The students letter grade for the course, based
        on final_grade

        """
        #score = self.score
        quizzes = self.scores_dropped["quizzes"]
        homeworks = self.scores_dropped["homeworks"]
        assignments = self.scores_dropped["assignments"]
        midterm = self.scores_dropped["midterm"]
        final = self.scores_dropped["final"]
 
        #Finding the average of each category
        average_quizzes = sum(quizzes)/len(quizzes)
        average_homeworks = sum(homeworks)/len(homeworks)
        average_assignments = sum(assignments)/len(assignments)
        average_midterm = sum(midterm)/len(midterm)
        
        
        another_final = float(final[0])
      
      
        #The multiplier is because average score for quizzes is given out of 10, so to obtain the result out of 100, we
        #have to multiply by 10. Same for homeworks (out of 20), assignments (out of 25), and midtern (out of 50).
        new_quizzes = average_quizzes * 10
        new_homeworks = average_homeworks * 5
        new_assignments = average_assignments * 4
        new_midterm = average_midterm * 2
        
        myfinal = ((new_quizzes*0.10) + (new_homeworks*0.20) + (new_assignments*0.30) + (new_midterm*0.15) + (another_final*0.25))
        
        return myfinal
        
    def letter_grade(self): 
        """Calculates what letter grade the 
        student has for the course based on their final grade percentage.
        
        Argument:
        final_grade (int): The percentage of their final grade for the course
        
        Returns:
        letter_grade (str): Their letter grade for the course
        
        """
        #Defining letter grade as an empty string
        letter_grade = ""
        final_grade = self.final_grade
        
        if final_grade() >= 97:
            letter_grade = "A+"
        elif final_grade() >= 93:
            letter_grade = "A"
        elif final_grade() >= 90:
            letter_grade = "A-"
        elif final_grade() >= 87:
            letter_grade = "B+"
        elif final_grade() >= 83:
            letter_grade = "B"
        elif final_grade() >= 80:
            letter_grade = "B-"
        elif final_grade() >= 77:
            letter_grade = "C+"
        elif final_grade() >= 73:
            letter_grade = "C"
        elif final_grade() >= 70:
            letter_grade = "C-"
        elif final_grade() >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
            
        return letter_grade
            
       
    #End of the class

def read_file(filename): 
        """Reads in the default file 
        (since the user selected that option) and return a dictionary 
        with the categories and scores from the file.
        
        Argument(s): 
        -filename: Path to the default file (newscores.csv) containing grades 
        for the class per category per line
    
        Side Effects:
        It removes any empty strings in a category's list of scores. Makes
        the dictionary cleaner.
        
        Return:
        category_scores (dictionary): The keys (strings) are 
        the names of the categories (quizzes, homeworks, assignments, etc.).
        The values are lists containing the scores (integers) 
        for each category.
        """ 
        category_scores = {}
        
        with open(filename, "r", encoding = "utf-8") as f:
            for line in f:
                line = line.strip().rstrip(",").split(",")
                int_scores = [int(number) for number in line[1:]]
                category_scores[line[0]] = int_scores
        return category_scores
            
    
def user_scores(): #add a try catch block, if user doesn't enter correct 
        #number of grades, the program will return an error (while loop)
        #Instead of using a try catch bloc, I used a while loop that seems to be
        
        """
        Prompts the user to enter grades
        for assignments, homework, quizzes, exams. Creates lists that contain 
        the grades for each category. 
        
        Arguments:
        Assignments (list): contains all assignment grades (list of integers)
        Homework (list): contains all homework grades (list of integers)
        Quizzes (list): contains all quiz grades (list of integers)
        Exams (list): contains all exam grades (list of integers)
        
        Return:
        Score (dict): Dictionary where the keys are the name of the lists and the
        values are the scores in each list.
        
        """
        
        
        #Defining empty lists for categories
        
        quizzes = []
        homeworks = []
        assignments = []
        midterm = []
        final = []
        
        #Defining empty dictionary to save lists of categories
        my_scores = {}
        
        #Prompting the user to enter scores manually
        #For quizzes score
        num_quizz = input("Enter the number of quizzes you took during the semester: ")
        num_quizz = int(num_quizz)
        while num_quizz < 0:
            print("Wrong value entered. Please enter an integer.")
            num_quizz = input("Enter the number of quizzes you took during the semester: ")
            num_quizz = int(num_quizz)
        i = 1   
        while i <= num_quizz:
            quizz = input("Enter the quizz score number " + str(i) + ": ")
            quizz = int(quizz)
            
            while quizz < 0 or quizz > 10:
                print("Wrong value entered. Please enter an integer from 0 to 10.")
                quizz = input("Enter the quizz score number " + str(i) + ": ")
                quizz = int(quizz)
            i += 1
            quizzes.append(quizz)
                
        #For Homeworks score
        num_hom = input("Now enter the number of homeworks you took during the semester: ")
        num_hom = int(num_hom)
        while num_hom < 0:
            print("Wrong value entered. Please enter an integer more than 0.")
            num_hom = input("Enter the number of homeworks you took during the semester: ")
            num_hom = int(num_hom)
        j = 1   
        while j <= num_hom:
            hom = input("Enter the homework score number " + str(j) + ": ")
            hom = int(hom)
            
            while hom < 0 or hom > 20:
                print("Wrong value entered. Please enter an integer from 0 to 20.")
                hom = input("Enter the homework score number " + str(j) + ": ")
                hom = int(hom)
            j += 1
            homeworks.append(hom)
                
        #For Assignments score
        num_assig = input("Now enter the number of assignments you took during the semester: ")
        num_assig = int(num_assig)
        while num_assig < 0:
            print("Wrong value entered. Please enter an integer more than 0.")
            num_assig = input("Enter the number of assignments you took during the semester: ")
            num_assig = int(num_assig)
        l = 1   
        while l <= num_assig:
            assig = input("Enter the assignments score number " + str(l) + ": ")
            assig = int(assig)
            
            while assig < 0 or assig > 25:
                print("Wrong value entered. Please enter an integer from 0 to 25.")
                assig = input("Enter the assignments number " + str(l) + ": ")
                assig = int(assig)
            l += 1
            assignments.append(assig)
                
        #For midterms score
        num_midterms = input("Now enter the number of midterms you took during the semester: ")
        num_midterms = int(num_midterms)
        while num_midterms < 0:
            print("Wrong value entered. Please enter an integer more than 0.")
            num_midterms = input("Enter the number of midterms you took during the semester: ")
            num_midterms = int(num_midterms)
        k = 1   
        while k <= num_midterms:
            mid = input("Enter the midterms score number " + str(k) + ": ")
            mid = int(mid)
            
            while mid < 0 or mid > 50:
                print("Wrong value entered. Please enter an integer from 0 to 50.")
                mid = input("Enter the midterms score number " + str(k) + ": ")
                mid = int(mid)
            k += 1
            midterm.append(mid)
                
        #For final exam
        final_exam = input("Enter your final exam score: ")
        final_exam = int(final_exam)
        while final_exam < 0 or final_exam > 100:
            print("Wrong value entered. Please enter an integer from 0 to 100.")
            final_exam = input("Enter your final exam score: ")
            final_exam = int(final_exam)
        
        final.append(final_exam)
        
        #Adding category lists to dictionary    
        my_scores["quizzes"] = quizzes
        my_scores["homeworks"] = homeworks
        my_scores["assignments"] = assignments
        my_scores["midterm"] = midterm
        my_scores["final"] = final
            
        return my_scores
       
       
       
 
def write_file(my_scores):
    
    """
    Writes a file that contains 
    the arguments the user passes in.
    
    Arguments:
    Filename (str)- the name the user wants to give the file

    Side-effect: Creates file or overrides it if it already exists.
    """
    
    
    """   
        df = pd.DataFrame()
        quizzes = ['Quizzes']
        for score in my_scores['quizzes']:
            quizzes.append(score)
        df.append(quizzes)
        hw = ['Homeworks']
        for score in my_scores['homeworks']:
            hw.append(score)
        df.append(hw)
        assignments = ['Assignments']
        for score in my_scores['assignments']:
            assignments.append(score)
        df.append(assignments)
        midterm = ['Midterms']
        for score in my_scores['midterm']:
            midterm.append(score)
        df.append(midterm)
        final = ['Finals']
        for score in my_scores['final']:
            hw.append(score)
        df.append(final)
        df.to_excel('Sprdsheet.xlsx')
    """
   
def main():

    """
    Prompts the user and ask if they want to manually enter their grades 
    for a class or calculate grades from the default file. Using an instance of
    the class.
    
    Argument:
    answer (string): The users answer (Yes or No)
    If the user answers 'yes', they will enter their grades for each category
    If the user answers 'no', the program will run using the default file.
    
    Side-effects:
    If the user wants to use the default file, main will call read_file by
    passing in the filename and get the dictionary. 
    
    Return:
    scores (dictionary): contains the categories and scores for each category.
    The keys (strings) are the names of the categories (quizzes, exams, etc.).
    The values are lists containing the scores for each category.
    
    """
    
    print(" This program is to help user calculate their final grade based on their scores.")
    answer = input("Would you like to manually enter scores or calculate from a default file (YES or NO)? ")

    if isinstance(answer,str):
        answer = answer.upper()
    
    while answer != "NO" and answer != "YES":
        if isinstance(answer,str):
            answer = answer.upper()
        print("Please enter YES or NO.")
        answer = input("Would you like to manually enter grades or calculate from a default file (YES or NO)? ")

    ans = answer
    
    if ans == "YES":
        scores = user_scores()
        
    elif ans == "NO":
        scores = read_file("newscores.csv")
        
    print(scores)
    final_scores = CalculateGrades(scores)
    
    drop_score = final_scores.drop_score()
    final_grade = final_scores.final_grade()
    letter_grade = final_scores.letter_grade()
    

    
    if letter_grade == "A+" or letter_grade == "A" or letter_grade == "A-":
        print( ("Awesome, you passed with " + str(final_grade) + " as a final grade. Your letter grade is " + letter_grade + "."))
        print("Your lower score of all categories has been dropped. Here are your new scores:")
        print(drop_score)
    elif letter_grade == "B+" or letter_grade == "B" or letter_grade == "B-":
        print ("Good job, you passed with " + str(final_grade) + " as a final grade. Your letter grade is " + letter_grade + ".")
        print("Your lower score of all categories has been dropped. Here are your new scores:")
        print(drop_score)
    elif letter_grade == "C+" or letter_grade == "C" or letter_grade == "C-":
        print ("Not too bad, you passed with " + str(final_grade) + " as a final grade. Your letter grade is " + letter_grade + ".")
        print("Your lower score of all categories has been dropped. Here are your new scores:")
        print(drop_score)
    else:
        print ("Sorry, you failled with " + str(final_grade) + " as a final grade. Your letter grade is " + letter_grade + ".")
        
if __name__ == "__main__":
    main()
     
