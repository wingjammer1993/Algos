def create_workflow_stages(precursor_steps):

    new_order_list = []
    new_order_list_inter = []
    master_list = []

    for sublist in precursor_steps:
        for item in sublist:
            if item not in new_order_list:
                new_order_list.append(item)

    length = len(new_order_list)

    list_removed = []
    while length > len(new_order_list_inter):
        pass_list = create_master_list(precursor_steps, new_order_list)
        master_list.append(pass_list)
        for elem in pass_list:
            if elem in new_order_list:
                new_order_list.remove(elem)
        for sublist in master_list:
            for item in sublist:
                if item not in new_order_list_inter:
                    new_order_list_inter.append(item)

    return master_list


def create_master_list(new_list, new_ordering_list):
    order_list = []
    for sublist in new_list:
        for item in sublist:
            if item not in order_list:
                order_list.append(item)

    length = len(new_ordering_list)
    order_weights = [0]*length

    for item in new_ordering_list:
        for sublist in new_list:
            if item in sublist:
                count  = sublist.index(item)
                object = sublist[0]
                if 1 == count:
                    if object not in new_ordering_list:
                        first_term = 0
                    else:
                        first_term = order_list.index(object) + 1
                    weight =  first_term
                else:
                    weight = 0
                item_index = new_ordering_list.index(item)
                order_weights[item_index] = order_weights[item_index] + weight

    pass_list = []
    for elem in new_ordering_list:
        minumum_val = min(order_weights)
        x = order_weights[new_ordering_list.index(elem)]
        if minumum_val == x:
            pass_list.append(elem)

    return pass_list




# START TEST CASES
# You can add test cases in the two lists below. Each test case
# input/expected output should correspond to the same index in the
# respective lists returned.
test_inputs = [
    [["clean", "build"], ["metadata", "binary"], ["build", "link"], ["link", "binary"], ["clean", "metadata"],
     ["build", "resources"]],
    [["boil", "serve"], ["chop", "boil"], ["stir", "boil"], ["set table", "serve"]]
]

test_outputs = [
    [["clean"], ["build", "metadata"], ["resources", "link"], ["binary"]],
    [["chop", "stir", "set table"], ["boil"], ["serve"]]
]


# END TEST CASES

# DO NOT MODIFY MAIN()
def main():
    for test_input, test_output in zip(test_inputs, test_outputs):
        try:
            result = create_workflow_stages(test_input)

            if len(result) == len(test_output) and all(
                    map(lambda k: sorted(result[k]) == sorted(test_output[k]), range(len(result)))):
                print('Pass')
            else:
                print('Fail')
        except Exception as e:
            print('Fail')
            print(e)


#if __name__ == "__main__":
#    main()
