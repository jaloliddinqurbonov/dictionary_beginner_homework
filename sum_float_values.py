def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    l=sum(i for i in data.values() if type(i).__name__=="float")
    return l
print(sum_float_values({"a":5.9,"b":5,"c":6.9}))