def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    files = open(csv_file_path, "r")
    res = [ ]
    
    for pair in files:
        pair = pair[:-1]
        component = pair.split(',')
        sublist = [int(component[0]), int(component[1])]
        res.append(sublist)
    
    files.close()
    return res