"""
This file plots a y=x^2 line and signs my name at the bottom left corner of the graph. Or at least the test block does.
"""

__author__ = "Ashton Switzer"

import matplotlib.pyplot as plt

def annotate_plot(annotations: dict) -> None:
    for text, opts in annotations.items():
        x, y = opts['position']
        ha, va = opts['alignment']
        fs = opts['fontsize']
        plt.text(x, y, text,
                 horizontalalignment=ha,
                 verticalalignment=va,
                 fontsize=fs)


if __name__ == "__main__":
    import datetime

    # Simple test plot
    x = [0, 1, 2, 3]
    y = [0, 1, 4, 9]
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Demo of annotate_plot()")

   #signature + timestamp in bottom-left corner
    date_str = datetime.date.today().isoformat()
    signature = f"Created by Ashton Switzer {date_str}"

    ax = plt.gca()
    x_min, y_min = ax.get_xlim()[0], ax.get_ylim()[0]

    annotations = {
        signature: {
            'position': (x_min, y_min),
            'alignment': ['left', 'bottom'],
            'fontsize': 10
        }
    }

    annotate_plot(annotations)
    plt.show()