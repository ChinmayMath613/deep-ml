def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    columns = len(a[0])

    trans_a = []
    for i in range(columns):
        column = [x[i] for x in a]
        trans_a.append(column)

    return trans_a
