def create_phone_number(n):
    as_array = list(map(lambda x: str(x), n))
    as_array.insert(0, "(")
    as_array.insert(4, ") ")
    as_array.insert(8, "-")
    return "".join(as_array)
