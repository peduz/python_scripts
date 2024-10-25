def scalar_projection(vector1, vector2):
    """
    Calculates the scalar projection of vector1 onto vector2.
    
    Args:
        vector1 (list): A list representing the first vector.
        vector2 (list): A list representing the second vector.
        
    Returns:
        float: The scalar projection of vector1 onto vector2.
    """
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude_vector2 = sum(x ** 2 for x in vector2) ** 0.5
    if magnitude_vector2 == 0:
        return 0
    else:
        return dot_product / magnitude_vector2
    

v = input("Insert the vector coordinates comma separated: ").split(',')
v = [float(i) for i in v]

c = input("Insert the projection vector: ").split(',')
c = [float(i) for i in c]

scalarc_v = scalar_projection(v, c)

print("The scalar projection is:", scalarc_v)