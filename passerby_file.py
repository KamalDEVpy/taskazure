def del_upd_ret_func(json_datas):
    data_key = ["appid","action","uid","model","qty","price"]
    data_list_2=[]
    for i in json_datas:
        data_list_1 = []
        for j in data_key:
            data_list_1.append(i[j])
        data_list_2.append(data_list_1)
    data_list_tuple=[]      
    for l in data_list_2:
        data_tuple = tuple(l)
        data_list_tuple.append(data_tuple)
    return(data_list_tuple)

def create_func(json_datas):
    data_key = ["appid","action","model","qty","price"]
    data_list_2=[]
    for i in json_datas:
        data_list_1 = []
        for j in data_key:
            data_list_1.append(i[j])
        data_list_2.append(data_list_1)
    data_list_tuple=[]      
    for l in data_list_2:
        data_tuple = tuple(l)
        data_list_tuple.append(data_tuple)
    return(data_list_tuple)