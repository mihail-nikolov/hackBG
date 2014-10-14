string = "/srv/www/htdocs/wtf"


def make_array(path):
    arr_path = path.split("/")
    new_arr = []
    for i, el in enumerate(arr_path):
        if i == len(arr_path)-1 and el != "" and el != "." and el != "..":
            new_arr.append(el)
        elif el != "" and el != "." and el != ".." and arr_path[i+1] != "..":
            new_arr.append(el)
    return new_arr


def reduce_file_path(path):
    arr = make_array(path)
    new_path = ''
    if len(arr) == 0:
        new_path += "/"
    else:
        for j in arr:
            new_path += "/" + j
    return new_path

print(reduce_file_path(string))
