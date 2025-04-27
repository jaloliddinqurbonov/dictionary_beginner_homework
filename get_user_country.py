def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    a=''
    for i in data:
        if name in i["name"]:
            a=i["country"]
    return a if len(a)>0 else "bunday ism yo'q"
print(get_user_country([{"country":"uzbekistan","name":"Zafar"},{"country":"tojikiston","name":"Murod"},{"country":"qozoqiston","name":"ali"}],name="Murod"))