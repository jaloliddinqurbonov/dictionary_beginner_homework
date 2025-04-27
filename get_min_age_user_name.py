def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    l=[i["age"] for i in data]
    a=l.index(min(l))
    return data[a]['name'] 
