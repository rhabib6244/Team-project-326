
import sys

def drop_score(self, quizzes, homeworks, assignments, midterm, final):
        
        
        
        quizzes = [23, 34, 1, 98, 44]
        homeworks = [24, 24, 454, 56, 3]
        assignments = [0, 23, 98, 45]
        midterm = [34, 44, 23, 65]
        final = [123]
        
        lower_quizzes = min(float(x) for x in quizzes)
        lower_homeworks = min(float(x) for x in homeworks)
        lower_assignments = min(float(x) for x in assignments)
        
        
        for i in quizzes:
            if i == lower_quizzes:
                quizzes.remove(i)
        
        for j in homeworks:
            if j == lower_homeworks:
                homeworks.remove(j)
                
        for k in assignments:
            if k == lower_assignments:
                assignments.remove(k)
                
        return quizzes