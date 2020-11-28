
class calculateGrades():
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
    def __init__(self, name, course, grade): 
        """ The purpose of this method is to assign attributes that will
        be used in other methods.
        """
    

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
        
    def letter_grade(self, final_grade): 
        """The purpose of this method is to calculate what letter grade the 
        student has for the course based on their final grade percentage.
        
        Argument:
        final_grade (int): The percentage of their final grade for the course
        
        Returns:
        letter_grade (str): Their letter grade for the course
        
        """

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
                line.splits(",")
                length = len(line)
                scores = []
                for i in line(range(2,length)):
                    scores.append(i)
                    category_scores{str(line[0]): scores}
                
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
    
def user_scores(self): #add a try catch block, if user doesn't enter correct 
        #number of grades, the program will return an error (while loop)
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
        
def write_file(self):
        """The purpose of this method is to write a file that contains 
        the arguments the user passes in.
        
        Arguments:
        Filename (str)- the name the user wants to give the file

        Side-effect: Creates file or overrides it if it already exists.
        
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

