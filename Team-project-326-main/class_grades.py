from argparse import ArgumentParser
import sys


class calculateGrades:
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
    
    new_ans = user_answer()
    first_score = user_scores()
    second_score = parse_grade()
    
    def __init__(self, course_name, quizzes, homeworks, assignments, midterm, final): 
        """ The purpose of this method is to assign attributes that will
        be used in other methods.
        """
        self.course_name = course_name
        self.quizzes = quizzes
        self.homeworks = homeworks
        self.assignments = assignments
        self.midterm = midterm
        self.final = final
        
    
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
        
        score = {}
        quizzes = []
        homeworks = []
        assignments = []
        midterm = []
        final = []
        
        lower_quizzes = min(float(x) for x in quizzes)
        lower_homeworks = min(float(x) for x in homeworks)
        lower_assignments = min(float(x) for x in assignments)
        lower_midterm = min(float(x) for x in midterm)
        
        
        for i in quizzes:
            if i == lower_quizzes:
                quizzes.remove(i)
        
        for j in homeworks:
            if j == lower_homeworks:
                homeworks.remove(j)
                
        for k in assignments:
            if k == lower_assignments:
                assignments.remove(k)
                
        for l in midterm:
            if l == lower_midterm:
                midterm.remove(l)
                
        score["quizzes"] = quizzes
        score["homeworks"] = homeworks
        score["assignments"] = assignments
        score["midterm"] = midterm
        score["final"] = final
        
        return score
                
                
        """
        new_scores = {}
        low_assign = min(self.assignments)
        self.assignments.remove(lowest_assign)
        average_assign = sum(self.assignments)/len(self.assignments)
        low_homework = min(self.homework)
        self.homework.remove(low_homework)
        average_homework = sum(self.homework)/len(self.homework)
        low_quizzes = min(self.homework)
        self.quizzes.remove(low_quizzes)
        average_quizzes = sum(self.quizzes)/len(self.quizzes)
        new_scores = {'Assignments': average_assign, 'Homework':average_homework,
                      'Quizzes':average_quizzes}

        Return new_scores
        """
        
        
    def final_grade(self, final_grade):
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
        
        quizzes = self.score["quizzes"]
        homeworks = self.score["homeworks"]
        assignments = self.score["assignments"]
        midterm = self.score["midterm"]
        final = self.final["final"]
        
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
        
    def letter_grade(self, final_grade): 
        """The purpose of this method is to calculate what letter grade the 
        student has for the course based on their final grade percentage.
        
        Argument:
        final_grade (int): The percentage of their final grade for the course
        
        Returns:
        letter_grade (str): Their letter grade for the course
        
        """
        grade = self.final_grade
        letter_grade = ""
        
        if grade >= 97:
            letter_grade = "A+"
        elif grade >= 93:
            letter_grade = "A"
        elif grade >= 90:
            letter_grade = "A-"
        elif grade >= 87:
            letter_grade = "B+"
        elif grade >= 83:
            letter_grade = "B"
        elif grade >= 80:
            letter_grade = "B-"
        elif grade >= 77:
            letter_grade = "C+"
        elif grade >= 73:
            letter_grade = "C"
        elif grade >= 70:
            letter_grade = "C-"
        elif grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
            
        if letter_grade == "A+" or letter_grade == "A" or letter_grade == "A-":
            return ("Awesome, you passed with " + final_grade() + " as a final grade. Your letter grade is " + letter_grade + ".")
        elif letter_grade == "B+" or letter_grade == "B" or letter_grade == "B-":
            return ("Good job, you passed with " + final_grade() + " as a final grade. Your letter grade is " + letter_grade + ".")
        elif letter_grade == "C+" or letter_grade == "C" or letter_grade == "C-":
            return ("Not too bad, you passed with " + final_grade() + " as a final grade. Your letter grade is " + letter_grade + ".")
        else:
            return ("Sorry, you failled with " + final_grade() + " as a final grade. Your letter grade is " + letter_grade + ".")
        
    #End of the class

def read_file(self, filename): 
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
                line = line.split(",")
                length = len(line)
                scores = []
                for i in line(range(2,length)):
                    scores.append(i)
                    category_scores[str(line[0])] = scores
                
        return category_scores
        
def parse_grade(self, line):  
        """The purpose of this method is to parse the file and extract the 
        scores from the file for each category.
        
        Argument: 
        file: the file that contains the user's grades for the course.
        
        Return:
        assignment_list (list): contains all of the scores for assignments
        homework_list (list): contains all of the scores for homeworks
        quizzes_list (list): contains all of the scores for quizzes
        exams_list (list): contains all of the scores for exams

        """ 
        
        """
        scores = re.search(r"^([A-Z,a-z]{1,15})(.*)(\d*)", line)
        
        if scores:
            grades = [
                "assignment_list": scores.group(1),
                "homework_list": scores.group(2),
                "quizzes_list": scores.group(3),
                "exams_list": scores.group(4)
            ]
            
            return grades
        else:
            return("None")
            """
    
def user_scores(self): #add a try catch block, if user doesn't enter correct 
        #number of grades, the program will return an error (while loop)
        #Instead of using a try catch bloc, I used a while loop that seems to be
        
        """The purpose of this method is to prompt the user to enter grades
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
       
        
def write_file(self):
        """The purpose of this method is to write a file that contains 
        the arguments the user passes in.
        
        Arguments:
        Filename (str)- the name the user wants to give the file

        Side-effect: Creates file or overrides it if it already exists.
        
        """
        
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
        
def user_answer(self, answer):
    print(" This program is to help user calculate their final grade based on their scores.")
    answer = input("Would you like to manually enter scores or calculate from a default file (YES or NO)? ")


    while answer != "NO" and answer != "YES":
        print("Please enter YES or NO.")
        answer = input("Would you like to manually enter grades or calculate from a default file (YES or NO)? ")
        
    return answer
    
   
def main(self):
    """ The purpose of this method is to prompt the user
    and ask if they want to manually enter their grades or 
    calculate from the default file. Using an instance of the class.
    
    Argument:
    Response (string): The users answer (Yes or No)
    If the user answers 'yes', they will enter their grades 
    If the user answers 'no', the program will run using the default file.
    """

    ans = user_answer()
    if ans == "YES":
        user_scores()
        write_file()
        calculateGrades()
    elif ans == "NO":
        read_file()
        parse_grade()
        calculateGrades()
     