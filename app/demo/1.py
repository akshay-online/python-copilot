def process(file):  
    with open(file) as f:  
        data = f.readlines()  
    return [line for line in data if 'ERROR' in line]  
