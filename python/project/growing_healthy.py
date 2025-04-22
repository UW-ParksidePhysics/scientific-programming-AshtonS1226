"""
This module will take different types of positive and negative feedback and analyze it.

Feedback: Plot the change in the feedback. Treat all questions as if they're on equal footing. Take the average of the
first five questions and weigh them against the average of the last two questions. Analyze the standard deviation. Make
bar graphs for the teacher responses and annotate the one critical feedback point.
"""
import numpy

#__author__ = "Ashton Switzer"

#import numpy as np
#import matplotlib.pyplot as plt


#def test_plot():

    # Line
 #   intercepts = [4,3]
  #  x_bounds = np.array([-3,8])
   # x_values = np.linspace(x_bounds[0],x_bounds[1],100)
    # y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
    #y_values = -intercepts[1] *x_values / intercepts[0] + intercepts[1]

    # Circle
    #radius = intercepts[0]
    #angles = np.linspace(0, 2 * np.pi, 100)
    #circle_xs = radius * np.cos(angles)
    #circle_ys = radius * np.sin(angles)

    # plt.plot(x_bounds, y_bounds)
   # plt.plot( x_values, y_values )
    #plt.plot( circle_xs, circle_ys )
    #plt.show()

    #return


#if __name__ == '__main__':
 #   object_data = {'Earth': 9.8, 'Moon': 1.6, 'Mars': 3.7} # surface gravity [m/s/s]
  #  starting_velocity = 10 # m/s
   # times = np.linspace(0,5)
    #for planet_data in object_data.items():
     #   velocities = velocity_in_time(times, initial_velocity=starting_velocity,
      #                                gravitational_acceleration=planet_data[1])
       # plt.plot( times, velocities, lavel=planet_data[0])

    #plt.text(0,-1, f'Initial velocity: {starting_velocity: .0f} m/s')
    #plt.xlabel("Time (s)")
    #plt.ylabel("Velocity (m/s)")
    #plt.legend()
    #plt.show()
# Need to define velociy_in_time outside of class.
    # test_plot()



#### RENAME from growing_healthy.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization


__author__ = "Ashton Switzer"

"""This is the bar graph for the first out of two questions in the teacher responses"""

import numpy as np
import matplotlib.pyplot as plt


def make_teacher_response_graph_1():
    #Bar graph for the question "How much does this trip relate to your curriculum?
    ratings = [1,2,3,4,5]
    responses = [5,5,4,5,5,4,5,5,5,5,2,5,4,5,5,5,5]
    counts = np.bincount(responses)[1:]
    question = "On a scale of 1-5, how much does this field trip relate to your course curriculum?"

    #bar chart
    plt.figure(figsize=(17,5))
    plt.bar(ratings,counts,color='red')

    #labels
    plt.xlabel('Rating')
    plt.ylabel('Response')
    plt.title('Teacher Responses to Question 1')

    plt.show()


if __name__ == '__main__':
    make_teacher_response_graph_1()




"""This is the bar graph for the second out of two questions in the teacher responses"""

import numpy as np
import matplotlib.pyplot as plt

def make_teacher_response_graph_2():
    # Bar graph for the question "How engaging were the activities for your students?"
    ratings = [1,2,3,4,5]
    responses = [5,5,5,5,3,5,5,5,5,4,5,5,5,5,5,5,5]
    counts = np.bincount(responses)[1:]
    question = "On a scale of 1-5, how engaging were the activities for your students?"

    # Bar chart
    plt.figure(figsize=(17,5))
    plt.bar(ratings,counts,color='blue')

    #labels
    plt.xlabel('Rating')
    plt.ylabel('Response')
    plt.title('Teacher Responses to Question 2')

    plt.show()


if __name__ == '__main__':
    make_teacher_response_graph_2()


"""This is going to be the section where the first five questions are plotted against the last two questions to analyze
the change in feedback over time"""


# This data covers 17 of the evaluations that were given. 4 were unable to be used because they had a different format
data = [
    # Evaluation 1
    {
        'before': [(16,2), (14,4), (16,2), (15,3), (17,1)],
        'after': [(17,1), (18,0)]
    },
    # Evaluation 2
    {
        'before': [(18,1), (17,2), (19,0), (16,3), (19,0)],
        'after': [(19,0), (19,0)]
    },
    # Evaluation 3
    {
        'before': [(17,4), (20,1), (20,1), (21,0), (21,0)],
        'after': [(21,0), (21,0)]
    },
    # Evaluation 4
    {
        'before': [(20,1), (18,3), (20,1), (20,1), (20,1)],
        'after': [(20,1), (21,0)]
    },
    # Evaluation 5
    {
        'before': [(14,4), (17,1), (16,2), (15,3), (17,1)],
        'after': [(12,6), (17,1)]
    },
    # Evaluation 6
    {
        'before': [(14,2), (15,1), (14,2), (16,0), (16,0)],
        'after': [(13,3), (14,2)]
    },
    # Evaluation 7
    {
        'before': [(17,0), (17,0), (17,0), (17,0), (17,0)],
        'after': [(15,2), (15,2)]
    },
    # Evaluation 8
    {
        'before': [(15,5), (14,6), (14,6), (17,3), (17,3)],
        'after': [(20,0), (20,0)]
    },
    # Evaluation 9
    {
        'before': [(8,8), (12,4), (13,3), (12,4), (12,4)],
        'after': [(16,0), (16,0)]
    },
    # Evaluation 10
    {
        'before': [(11,2), (11,2), (13,0), (13,0), (13,0)],
        'after': [(12,1), (13,0)]
    },
    # Evaluation 11
    {
        'before': [(17,9), (23,3), (24,2), (25,1), (26,0)],
        'after': [(26,0), (25,1)]
    },
    # Evaluation 12
    {
        'before': [(22,2), (24,0), (23,1), (24,0), (23,1)],
        'after': [(17,7), (19,5)]
    },
    # Evaluation 13
    {
        'before': [(10,8), (9,9), (16,2), (17,1), (17,1)],
        'after': [(18,0), (17,1)]
    },
    # Evaluation 14
    {
        'before': [(18,2), (19,1), (19,1), (19,1), (17,3)],
        'after': [(17,3), (16,4)]
    },
    # Evaluation 15
    {
        'before': [(19,2), (21,0), (21,0), (21,0), (21,0)],
        'after': [(21,0), (21,0)]
    },
    # Evaluation 16
    {
        'before': [(16,6), (22,0), (20,2), (20,2), (22,0)],
        'after': [(20,2), (21,1)]
    },
    # Evaluation 17
    {
        'before': [(14,4), (17,1), (17,1), (16,2), (15,3)],
        'after': [(13,5), (13,5)]
    }
]

"""This next part calculates the average positive feedback (percentage of hands raised) before and after the 
field trip across all 17 papers."""

def average_positive_feedback(data, section):
    totals = []
    for entry in data:
        total_positive = sum([q[0] for q in entry[section]]) # sum of "hands up" for the given section
        total_responses = sum([q[0] + q[1] for q in entry[section]]) # total responses (up + down)
        totals.append(total_positive/total_responses)
    return sum(totals) / len(totals)

# Calculate averages for before and after the field trip
avg_before = average_positive_feedback(data, 'before')
avg_after = average_positive_feedback(data, 'after')

# The averages printed as percentages
print(f"Average Positive Feedback Before Field Trip: {avg_before * 100:.2f}%")
print(f"Average Positive Feedback After Field Trip: {avg_after * 100:.2f}%")

# This next step is the part where I added the visualizations.

import matplotlib.pyplot as plt

labels = ['Before Trip', 'After Trip']
values = [avg_before * 100, avg_after * 100] #This is the conversion to percentages

plt.bar(labels, values, color=['blue', 'green'])
plt.ylabel('Average Positive Feedback (%)')
plt.title('Class Feedback Before and After Field Trip')
plt.ylim(0, 100) # Keeps the y-axis between 0 and 100%

plt.show()

#Note: I want to find a way to incorporate the standard deviation, but I couldn't really figure out how to do that.

# I also need to structure the last part with the if __name__ == '__main__':


