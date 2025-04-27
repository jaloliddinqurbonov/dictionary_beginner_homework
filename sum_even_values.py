def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    l=data.values()
    s= sum([i for i in l if i%2==0])
    return s
print(sum_even_values({"a":1,"b":2,"c":4,"d":5}))


# ushbu misolda map() funksiyasidan foydalanish