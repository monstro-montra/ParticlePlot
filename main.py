import matplotlib.pyplot as plt
import numpy as np


def p(time):  # particle's position over time
    return (time ** 3) + (3 * time ** 2) + 3 * time + 1


def v(time):  # particle's velocity over time
    return (3 * time ** 2) + (6 * time) + 3


def a(time):  # particle's acceleration over time
    return 6 * time + 6


def plot_display():
    # Time values: setting the range of t between 0 and 10 seconds, with a granularity of 400 (granularity) which is
    # how many points between say t = 0 and t = 1. A lower number will make the graph look jagged and a higher number
    # will make it more accurate.
    t = np.linspace(-2, 10, 400)  # start at -2,stop at 10, granularity 400

    # Functions
    position = p(t)
    velocity = v(t)
    acceleration = a(t)

    figure, axis = plt.subplots(3, figsize=(8, 15))  # create a figure with three subplots

    # plot and label the position function
    axis[0].plot(t, position, label="p(t) = t³ + 3t² + 3t + 1")
    axis[0].set_xlabel('Time (t)')
    axis[0].set_ylabel('Position (p)')
    axis[0].set_title('Particle Position over Time')
    axis[0].legend()
    axis[0].grid(True)

    # plot and label the velocity function
    axis[1].plot(t, velocity, label="v(t) = 3t² + 6t +3")
    axis[1].set_xlabel('Time (t)')
    axis[1].set_ylabel('Position (p)')
    axis[1].set_title('Particle Velocity over Time')
    axis[1].legend()
    axis[1].grid(True)

    # plot and label the acceleration function
    axis[2].plot(t, acceleration, label="a(t) = 6t + 6")
    axis[2].set_xlabel('Time (t)')
    axis[2].set_ylabel('Position (p)')
    axis[2].set_title('Particle Acceleration over Time')
    axis[2].legend()
    axis[2].grid(True)

    plt.subplots_adjust(hspace=1)  # adjust the space between plots

    plt.show()  # show the plot


def main():
    plot_display()  # call the plot_display function


if __name__ == "__main__":  # set the main function as the execution point
    main()
