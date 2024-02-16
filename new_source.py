
check_list = []

def list_update(list):
    global check_list
    check_list = list[:]


def img_name():
    name = check_list[0]
    check_list.pop(0)
    return name 

def img_job():
    name = check_list[0]
    check_list.pop(0)
    return name 

def img_match_data(input):
    for x in check_list:
        if input in x:
            check_list.pop(check_list.index(x))
            return x
        
def check_address(input):
     if input not in check_list[0]:
        check_list.pop(0)   

def img_first_value():
    if not check_list:
        return None
    else:
        tmp = check_list[0]
        check_list.pop(0)
        return tmp        

def img_all_detail(input):
    my_dic = {}
    list_update(input)

    my_dic["name"] = img_name()
    my_dic["job"] = img_job()
    my_dic["mail"] = img_match_data("@")
    my_dic["web"] = img_match_data("com")
    my_dic["num1"] = img_match_data("-")
    my_dic["num2"] = img_match_data("-")
    check_address("123")
    my_dic["address_1"] = img_first_value()
    my_dic["address_2"] = img_first_value()
    my_dic["address_3"] = img_first_value()
    my_dic["address_4"] = img_first_value()

    return my_dic

def dictionary_compare(dict1, dict2):
    output = {}
    for key in dict2:
        print(key)
        if key in dict2:
                if dict1[key] != dict2[key]:
                    output[key] = dict2[key]
        else:
            return 1
    
    return output