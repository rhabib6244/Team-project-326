from argparse import ArgumentParser
import sys


class CalculateGrades:
    """The purpose of this class is to calculate the grades from the default file.
    It will assign attributes that will be used in other methods. 

    Attributes:
    -Name (str): Represents the name of the student
    -Course (str): Represents the name of the course the student is in
    -Grade (int): Number representing the percentage/grade student has
    -Assignments (list): list of the assignments category scores
    -Homework (list): list of the homework category scores
    -Quizzes (list): list of the quizzes category scores
    -Exams (list): list of the exam category scores
    """
    
    
    def __init__(self, scores): 
        """ The purpose of this method is to assign attributes that will
        be used in other methods.
        """
        self.quizzes = scores["quizzes"]
        self.homeworks = scores["homeworks"]
        self.assignments = scores["assignments"]
        self.midterm = scores["midterm"]
        self.final = scores["final"]
        #final_grade = self.final_grade
        
        
        
        #self.new_ans = user_answer()
        
    
    def drop_score(self):
        """The purpose of this method is to drop the lowest score from each
        list/category excluding the exam category. Looks through each list and 
        deletes/pops the lowest score. Then calculates the average score of 
        each category after.
        
        Arguments:
        Assignments (list): contains all assignment grades (list of integers)
        Homework (list): contains all homework grades (list of integers)
        Quizzes (list): contains all quiz grades (list of integers)
        
        Return:
        New_scores(dict): Dictionary where the keys are the categories and 
        the values are the average scores for each category
        after the lowest score has been dropped. 
        """
        
        scores = {}
        
        lower_quizzes = min(self.quizzes)
        lower_homeworks = min(self.homeworks)
        lower_assignments = min(self.assignments)
        lower_midterm = min(self.midterm)
        
        quizzes = self.quizzes[:]
        homeworks = self.homeworks[:]
        assignments = self.assignments[:]
        midterm = self.midterm[:]
        final = self.final[:]
        
        quizzes.remove(lower_quizzes)
        homeworks.remove(lower_homeworks)
        assignments.remove(lower_assignments)
        midterm.remove(lower_midterm)
                
        scores["quizzes"] = quizzes
        scores["homeworks"] = homeworks
        scores["assignments"] = assignments
        scores["midterm"] = midterm
        scores["final"] = final
        
        return scores
                
        
        
    def final_grade(self):
        """The purpose of this method is to calculate the user's final 
        grade based on their average score for each category and weight of each
        category.

        Argument:
        New_scores (dict): Dictionary where the keys are the categories and 
        the values are the average scores for each category
        after the lowest score has been dropped.
    
        Returns:
        Final_grade (int): The students final grade for the course. 
        Letter_grade (str): The students letter grade for the course, based
        on final_grade

        """
        #score = self.score
        quizzes = self.scores["quizzes"]
        homeworks = self.scores["homeworks"]
        assignments = self.scores["assignments"]
        midterm = self.scores["midterm"]
        final = self.scores["final"]
        
        #Finding the average of quizzes
        total_quizzes = 0
        for i in range(0, len(quizzes)):
            total_quizzes = total_quizzes + quizzes[i]
        average_quizzes = total_quizzes / len(quizzes)
        
        #finding the average of homeworks
        total_homeworks = 0
        for j in range(0, len(homeworks)):
            total_homeworks = total_homeworks + homeworks[i]
        average_homeworks = total_homeworks / len(homeworks)
        
        #Finding the average of assignments
        total_assignments = 0
        for i in range(0, len(assignments)):
            total_assignments = total_assignments + assignments[i]
        average_assignments = total_assignments / len(assignments)
        
        #Finding the average of midterm
        total_midterm = 0
        for i in range(0, len(midterm)):
            total_midterm = total_midterm + midterm[i]
        average_midterm = total_midterm / len(midterm)
      
        
        #The multiplier is because average score for quizzes is given out of 10, so to obtain the result out of 100, we
        #have to multiply by 10. Same for homeworks (out of 20), assignments (out of 25), and midtern (out of 50).
        new_quizzes = average_quizzes[quizzes] * 10
        new_homeworks = average_homeworks[homeworks] * 5
        new_assignments = average_assignments[assignments] * 4
        new_midterm = average_midterm[midterm] * 2
        #final = average_scores[final]
        
        final_grade = ((new_quizzes*0.10) + (new_homeworks*0.20) + (new_assignments*0.30) + (new_midterm*0.15) + (final*0.25))
        
        return final_grade
        
    def letter_grade(self): 
        """The purpose of this method is to calculate what letter grade the 
        student has for the course based on their final grade percentage.
        
        Argument:
        final_grade (int): The percentage of their final grade for the course
        
        Returns:
        letter_grade (str): Their letter grade for the course
        
        """
        #grade = self.final_grade
        letter_grade = ""
        
        if final_grade >= 97:
            letter_grade = "A+"
        elif final_grade >= 93:
            letter_grade = "A"
        elif final_grade >= 90:
            letter_grade = "A-"
        elif final_grade >= 87:
            letter_grade = "B+"
        elif final_grade >= 83:
            letter_grade = "B"
        elif final_grade >= 80:
            letter_grade = "B-"
        elif final_grade >= 77:
            letter_grade = "C+"
        elif final_grade >= 73:
            letter_grade = "C"
        elif final_grade >= 70:
            letter_grade = "C-"
        elif final_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
            
        return letter_grade
            
       
    #End of the class

def read_file(filename): 
        """The purpose of this method is to open a file and convert each
        grade description in it to a dictionary using the parse_grade 
        function. scores_word is the name of the file
    
        Argument: 
        -Path to the file containing grades per line
    
        Return:
        Dictionary: keys are the categories. Values are
        lists of the grades for each key.
        """ 
        category_scores = {}
        with open(filename, "r", encoding = "utf-8") as f:
            for line in f:
                line = line.strip()
                line = line.split(",")
                category_scores[line[0]] = line[1:]
                
    
        return category_scores
            
    
def user_scores(): #add a try catch block, if user doesn't enter correct 
        #number of grades, the program will return an error (while loop)
        #Instead of using a try catch bloc, I used a while loop that seems to be
        
        """
        The purpose of this method is to prompt the user to enter grades
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
        
        #Prompting the user to enter scores manually
        #Defining empty lists for categories
        
        quizzes = []
        homeworks = []
        assignments = []
        midterm = []
        final = []
        
        my_scores = {}
        
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
            
        my_scores["quizzes"] = quizzes
        my_scores["homeworks"] = homeworks
        my_scores["assignments"] = assignments
        my_scores["midterm"] = midterm
        my_scores["final"] = final
            
        return my_scores
       
       
       
 
#def write_file(my_scores):
    
        """The purpose of this method is to write a file that contains 
        the arguments the user passes in.
        
        Arguments:
        Filename (str)- the name the user wants to give the file

        Side-effect: Creates file or overrides it if it already exists.
        """
        """
                       
        #new_dictionary = user_scores()
        
        quizzes = my_scores["quizzes"]
        
        
        df = pd.DataFrame()
        quizzes = ['Quizzes']
        for score in self.quizzes:
        quizzes.append(score)
        df.append(quizzes)
        hw = ['Homeworks']
        for score in self.homeworks:
        hw.append(score)
        df.append(hw)
        assignments = ['Assignments']
        for score in self.assignments:
        assignments.append(score)
        df.append(assignments)
        midterm = ['Midterms']
        for score in self.midterm:
        midterm.append(score)
        df.append(midterm)
        final = ['Finals']
        for score in self.final:
        hw.append(score)
        df.append(final)
        df.to_excel(self.course_name+'.xlsx')
        
    """
    
    
"""
        
def user_answer(self, answer):
    print(" This program is to help user calculate their final grade based on their scores.")
    answer = input("Would you like to manually enter scores or calculate from a default file (YES or NO)? ")


    while answer != "NO" and answer != "YES":
        print("Please enter YES or NO.")
        answer = input("Would you like to manually enter grades or calculate from a default file (YES or NO)? ")
        
    return answer
"""


    
   
def main():
    """ The purpose of this method is to prompt the user
    and ask if they want to manually enter their grades or 
    calculate from the default file. Using an instance of the class.
    
    Argument:
    Response (string): The users answer (Yes or No)
    If the user answers 'yes', they will enter their grades 
    If the user answers 'no', the program will run using the default file.
    """
    
    print(" This program is to help user calculate their final grade based on their scores.")
    answer = input("Would you like to manually enter scores or calculate from a default file (YES or NO)? ")


    while answer != "NO" and answer != "YES":
        print("Please enter YES or NO.")
        answer = input("Would you like to manually enter grades or calculate from a default file (YES or NO)? ")

    #ans = user_answer()
    #scores = user_scores()
    ans = answer
    
    if ans == "YES":
        scores = user_scores()
       # write_file()
        
    elif ans == "NO":
        new_ans = print("enter the file name")
        scores = read_file(new_ans)
        
    print(scores)
    final_scores = CalculateGrades(scores)
    
    """
    drop = final_scores.drop_score()
    final_grade = float(final_scores.final_grade(drop))
    letter_grade = final_scores.final_grade(final_grade)
    """
    
    drop_score = final_scores.drop_score()
    final_grade = final_scores.final_grade()
    letter_grade = final_scores.letter_grade()
    

    
    if letter_grade == "A+" or letter_grade == "A" or letter_grade == "A-":
        print( ("Awesome, you passed with " + final_grade + " as a final grade. Your letter grade is " + letter_grade + "."))
    elif letter_grade == "B+" or letter_grade == "B" or letter_grade == "B-":
        print ("Good job, you passed with " + final_grade + " as a final grade. Your letter grade is " + letter_grade + ".")
    elif letter_grade == "C+" or letter_grade == "C" or letter_grade == "C-":
        print ("Not too bad, you passed with " + final_grade + " as a final grade. Your letter grade is " + letter_grade + ".")
    else:
        print ("Sorry, you failled with " + final_grade + " as a final grade. Your letter grade is " + letter_grade + ".")
        
if __name__ == "__main__":
    main()
     