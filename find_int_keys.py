def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    l=[]
    for i in data.keys():
        if type(i).__name__=='int':
            l.append(i)
    return l
print(find_int_keys({1:"efa","4":"ffawf",5:"asfasdfa",4.2:"wfarfrrrrrrrrrrrrr"}))

# a=34
# print(type(a).__name__)