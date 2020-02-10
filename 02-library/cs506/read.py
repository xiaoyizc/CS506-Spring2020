def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path, "r")
    l = [ ]
    
    for pair in f:
        pair = pair[:-1]
        component = pair.split(',')
        subl = [int(component[0]), int(component[1])]
        l.append(subl)
    return l