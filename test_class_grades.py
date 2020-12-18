
import unittest
from class_grades import CalculateGrades, read_file, user_scores, write_file, main
from pathlib import Path


def test_user_scores():
    """ Test all the methods and function considering that the user manually entered scores.
        To do that, a dictionary is created with scores entered by users, and every methods/functions
        are tested using that dictionary.
    """
    
    #Creating a new dictionary
    quizzes = [10, 8, 10, 7, 9]
    homeworks = [18, 20, 15, 19, 10]
    assignments = [22, 25, 20, 25]
    midterm = [48, 44]
    final = [92]
    
    dict1 = {}
    dict1["quizzes"] = quizzes
    dict1["homeworks"] = homeworks
    dict1["assignments"] = assignments
    dict1["midterm"] = midterm
    dict1["final"] = final
    
    quizzes2 = [10, 8, 10, 9]
    homeworks2 = [18, 20, 15, 19]
    assignments2 = [22, 25, 25]
    midterm2 = [48]
    final2 = [92]
    
    dict2 = {}
    dict2["quizzes"] = quizzes2
    dict2["homeworks"] = homeworks2
    dict2["assignments"] = assignments2
    dict2["midterm"] = midterm2
    dict2["final"] = final2
    
    test = CalculateGrades(dict1)
    assert test.drop_score() == dict2
    
    """
    assert m.opponent == opponent
    assert m.home == home
    assert m.md_score == md_score
    assert m.other_score == other_score
    assert not m.win()
    """
    
def test_read_file():  
    scores_dictionary = {'quizzes':[7,10,5,8,10,8,8,6,10,9,10],
                         'homeworks':[18,15,8,20,16,19],
                         'assignments':[25,23,20,24,25],
                         'midterm':[45,40],
                         'final':[92]}
    
    assert scores_dictionary == read_file("newscores.csv")
    
def test_drop_scores():
    #sorted_quizzes = [5,6,7,8,8,8,9,10,10,10,10]
    #sorted_homeworks = [8,15,16,18,19,20]
    #sorted_assignments = [20,23,24,25,25]
    #sorted_midterm = [40,45]
    #assert sorted_quizzes == drop_score(self).get(lower_quizzes)
    
    scores = {'quizzes':[7,10,5,8,10,8,8,6,10,9,10],
                         'homeworks':[18,15,8,20,16,19],
                         'assignments':[25,23,20,24,25],
                         'midterm':[45,40],
                         'final':[92]}
    scores_dropped = {'quizzes':[7,10,8,10,8,8,6,10,9,10],
                      'homeworks':[18,15,20,16,19],
                      'assignments':[25,23,24,25],
                      'midterm':[45],
                      'final':[92]}
    c= CalculateGrades(scores)
    assert scores_dropped == c.drop_score()



def test_init():
    #Defining scores argument
    scores = {"quizzes": [7, 10, 5, 8, 8, 6, 10, 9, 10],
              "homeworks": [18, 15, 8, 20, 16, 19],
              "assignments": [25, 23, 20, 24, 25],
              "midterm": [45, 40],
              "final": [92]}
    
    #Creating class object
    p1 = CalculateGrades(scores)
    print(p1.scores["quizzes"])
    print(p1.scores["homeworks"])
    print(p1.scores["assignments"])
    print(p1.scores["midterm"])
    print(p1.scores["final"])
    
    assert p1.scores["quizzes"] == scores["quizzes"]
    assert p1.scores["homeworks"] == scores["homeworks"]
    assert p1.scores["assignments"] == scores["assignments"]
    assert p1.scores["midterm"] == scores["midterm"]
    assert p1.scores["final"] == scores["final"]
    
    
def test_write_file():
    scores = {"quizzes": [7, 10, 5, 8, 8, 6, 10, 9, 10],
              "homeworks": [18, 15, 8, 20, 16, 19],
              "assignments": [25, 23, 20, 24, 25],
              "midterm": [45, 40],
              "final": [92]}
    write_file(scores)
    test_scores = read_file('scoresheet.csv')
    assert scores == test_scores


class TestCalculateGrades(unittest.TestCase):
    
    def test_final_grade(self):
        
        #First Case
        score1 = {}
        
        quizzes2 = [10, 8, 10, 9, 3]
        homeworks2 = [18, 20, 15, 19, 10]
        assignments2 = [22, 25, 25, 20]
        midterm2 = [48, 45]
        final2 = [92]
        
        score1["quizzes"] = quizzes2
        score1["homeworks"] = homeworks2
        score1["assignments"] = assignments2
        score1["midterm"] = midterm2
        score1["final"] = final2
        
        score2 = CalculateGrades(score1)
        score2.drop_score()
        
        self.assertEqual(score2.final_grade(), 93.44999999999999)
        
        #Second Case
        score = {}
        
        quizzes3 = [8.7, 8.7, 8.7, 8.7, 3]
        homeworks3 = [17.4, 17.4, 15, 17.4]
        assignments3 = [21.75, 20, 21.75, 21.75]
        midterm3 = [43.5, 40]
        final3 = [87]
        
        score["quizzes"] = quizzes3
        score["homeworks"] = homeworks3
        score["assignments"] = assignments3
        score["midterm"] = midterm3
        score["final"] = final3
        
        score3 = CalculateGrades(score)
        score3.drop_score()
        self.assertEqual(score3.final_grade(), 87)
        
    def test_letter_grade(self):
        
        #First case
        score1 = {}
        
        quizzes2 = [10, 8, 10, 9, 3]
        homeworks2 = [18, 20, 15, 19, 10]
        assignments2 = [22, 25, 25, 20]
        midterm2 = [48, 45]
        final2 = [92]
        
        score1["quizzes"] = quizzes2
        score1["homeworks"] = homeworks2
        score1["assignments"] = assignments2
        score1["midterm"] = midterm2
        score1["final"] = final2
        
        score2 = CalculateGrades(score1)
        score2.drop_score()
        
        self.assertEqual(score2.letter_grade(), "A")
        
        #Second case
        score = {}
        
        quizzes3 = [8.7, 8.7, 8.7, 8.7, 3]
        homeworks3 = [17.4, 17.4, 15, 17.4]
        assignments3 = [21.75, 20, 21.75, 21.75]
        midterm3 = [43.5, 40]
        final3 = [87]
        
        score["quizzes"] = quizzes3
        score["homeworks"] = homeworks3
        score["assignments"] = assignments3
        score["midterm"] = midterm3
        score["final"] = final3
        
        score3 = CalculateGrades(score)
        score3.drop_score()
        
        self.assertEqual(score3.letter_grade(), "B+")
             
if __name__ == '__main__':
    unittest.main()