def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    s=0
    for i in data:
        s+=i["age"]
    return s