import numpy as np

def calculate_vectorial_position(initial_position,
                    velocity, time):
    """
    Calculates the position of an object at a given time,
    based on its initial position, velocity, and acceleration.

    Parameters
    ----------
    initial_position : vector
        The initial position of the object.
    velocity : vector
        The velocity of the object.
    time : float
        The time at which the position is to be calculated.

    Returns
    -------
    vector
        The position of the object at the given time.
    """
    position = initial_position + velocity * time
    return position

p = input("Insert the vector coordinates comma separated: ").split(',')
p = [float(i) for i in p]

v = input("Insert the vector coordinates comma separated: ").split(',')
v = [float(i) for i in v]

t = float(input("Insert the time: "))

msl = calculate_vectorial_position(np.array(p), np.array(v), t)

print("The position is:", msl)
