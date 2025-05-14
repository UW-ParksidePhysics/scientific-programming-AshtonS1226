# Student feedback data: list of evaluations with before/after positive (hands up) and negative (hands down) counts
student_data = [
    {'before': [(16, 2), (14, 4), (16, 2), (15, 3), (17, 1)],
     'after':  [(17, 1), (18, 0)]},
    {'before': [(18, 1), (17, 2), (19, 0), (16, 3), (19, 0)],
     'after':  [(19, 0), (19, 0)]},
    {'before': [(17, 4), (20, 1), (20, 1), (21, 0), (21, 0)],
     'after':  [(21, 0), (21, 0)]},
    {'before': [(20, 1), (18, 3), (20, 1), (20, 1), (20, 1)],
     'after':  [(20, 1), (21, 0)]},
    {'before': [(14, 4), (17, 1), (16, 2), (15, 3), (17, 1)],
     'after':  [(12, 6), (17, 1)]},
    {'before': [(14, 2), (15, 1), (14, 2), (16, 0), (16, 0)],
     'after':  [(13, 3), (14, 2)]},
    {'before': [(17, 0), (17, 0), (17, 0), (17, 0), (17, 0)],
     'after':  [(15, 2), (15, 2)]},
    {'before': [(15, 5), (14, 6), (14, 6), (17, 3), (17, 3)],
     'after':  [(20, 0), (20, 0)]},
    {'before': [(8, 8),  (12, 4), (13, 3), (12, 4), (12, 4)],
     'after':  [(16, 0), (16, 0)]},
    {'before': [(11, 2), (11, 2), (13, 0), (13, 0), (13, 0)],
     'after':  [(12, 1), (13, 0)]},
    {'before': [(17, 9), (23, 3), (24, 2), (25, 1), (26, 0)],
     'after':  [(26, 0), (25, 1)]},
    {'before': [(22, 2), (24, 0), (23, 1), (24, 0), (23, 1)],
     'after':  [(17, 7), (19, 5)]},
    {'before': [(10, 8), (9, 9),  (16, 2), (17, 1), (17, 1)],
     'after':  [(18, 0), (17, 1)]},
    {'before': [(18, 2), (19, 1), (19, 1), (19, 1), (17, 3)],
     'after':  [(17, 3), (16, 4)]},
    {'before': [(19, 2), (21, 0), (21, 0), (21, 0), (21, 0)],
     'after':  [(21, 0), (21, 0)]},
    {'before': [(16, 6), (22, 0), (20, 2), (20, 2), (22, 0)],
     'after':  [(20, 2), (21, 1)]},
    {'before': [(14, 4), (17, 1), (17, 1), (16, 2), (15, 3)],
     'after':  [(13, 5), (13, 5)]}
]

# Teacher responses organized by question ID
d = teacher_data = {
    '1': {
        'question': "Teacher Responses to Question 1: On a scale of 1-5, how much does this field trip relate to your course curriculum?",
        'ratings': [1, 2, 3, 4, 5],
        'responses': [5, 5, 4, 5, 5, 4, 5, 5, 5, 5, 2, 5, 4, 5, 5, 5, 5],
        'color': 'red'
    },
    '2': {
        'question': "Teacher Responses to Question 2: On a scale of 1-5, how engaging were the activities for your students?",
        'ratings': [1, 2, 3, 4, 5],
        'responses': [5, 5, 5, 5, 3, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5],
        'color': 'blue'
    }
}    # Used ChatGPT for dictionary(o4-mini-high, "How do I implement this dictionary into my code")
