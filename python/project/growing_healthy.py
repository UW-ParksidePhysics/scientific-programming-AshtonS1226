"""
This module will take different types of positive and negative feedback and analyze it.
"""

# This project produced three visualizations. One was a bar graph that showed the teacher responses to a question. The
# second was another bar graph that showed the teacher responses to a second question. Lastly, there was a third bar
# chart that compared results of the student evaluations before and after the field trip. This was to help determine
# whether the feedback was more positive after the field trip was over.



__author__ = "Ashton Switzer"

import numpy as np
import matplotlib.pyplot as plt
from data import student_data, teacher_data

#Needed to use ChatGPT to refine function (o4-mini-high, "How do I improve this combined function so that it shows
# both graphs instead of just one?)
def make_teacher_response_graph(ratings, responses, question, color):
    """
    Bar graphs for teacher responses.
    """
    counts = np.bincount(responses)[1:]
    plt.figure(figsize=(17, 5))
    plt.bar(ratings, counts, color=color)
    plt.xlabel('Rating')
    plt.ylabel('Response')
    plt.title(question)
    plt.show()


def average_positive_feedback(data, section):
    totals = []
    for entry in data:
        positive = sum(q[0] for q in entry[section])
        total    = sum(q[0] + q[1] for q in entry[section])
        totals.append(positive / total)
    return sum(totals) / len(totals)


def std_dev_positive_feedback(data, section):
    ratios = []
    for entry in data:
        positive = sum(q[0] for q in entry[section])
        total    = sum(q[0] + q[1] for q in entry[section])
        ratios.append(positive / total)
    return np.std(ratios, ddof=1)


def make_student_feedback_graph(data):
    """
    Plots before/after average positive feedback with error bars and percent-change.
    """
    avg_before = average_positive_feedback(data, 'before')
    avg_after  = average_positive_feedback(data, 'after')
    std_before = std_dev_positive_feedback(data, 'before') * 100
    std_after  = std_dev_positive_feedback(data, 'after') * 100

    labels = ['Before Trip', 'After Trip']
    values = [avg_before * 100, avg_after * 100]
    errors = [std_before, std_after]

    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color=['blue', 'green'], yerr=errors, capsize=10, width=0.6)

    # percent change annotation
    percent_change = ((avg_after - avg_before) / avg_before) * 100
    x_mid = (bars[0].get_x() + bars[1].get_x() + bars[0].get_width() + bars[1].get_width()) / 2
    y_mid = max(values) + 10
    ax.text(x_mid, y_mid, f'{percent_change:+.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_ylabel('Average Positive Feedback (%)')
    ax.set_title('Class Feedback Before and After Field Trip')
    ax.set_ylim(0, max(values) + 20)

    # fuzzy blocks for standard deviation
    for bar, err in zip(bars, errors):
        ax.add_patch(plt.Rectangle(
            (bar.get_x(), bar.get_height()),
            bar.get_width(), err,
            alpha=0.2, color=bar.get_facecolor()
        ))

    plt.show()


if __name__ == '__main__':
    for qid, info in teacher_data.items():
        make_teacher_response_graph(
            info['ratings'],
            info['responses'],
            info['question'],
            info.get('color', 'blue')
        )   # Used ChatGPT for dictionary(o4-mini-high, "How do I implement this dictionary into my code")

# Plot student feedback summary
    make_student_feedback_graph(student_data)

