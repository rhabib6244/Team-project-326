

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
    homeworks2 = [18, 20, 19, 10]
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
    assert test.drop_score == dict2
    
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