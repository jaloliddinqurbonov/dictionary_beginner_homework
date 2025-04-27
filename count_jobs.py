def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    return data.count(job)

# yoki

def count_job(data:list,job:str)->int:
    s=0
    for i in data:
        if job in i.values():
            s+=1
    return s

print(count_job(data=[{"ism":"ali","job":"fizik"},{"ism":"murod","job":"fizik"}],job="fizik"))