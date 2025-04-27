def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    l=[i["age"] for i in data]
    a=l.index(max(l))
    return data[a]['job']
print(get_max_age_user_name([{'job':'fizik',"age":32},{"job":'ani',"age":90}]))

# tushuntirish