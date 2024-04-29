def get_number_of_pages(number_of_page: int)-> list[int]:
    new_list = list()
    for i in range(number_of_page):
        new_list.append(i + 1)
    return new_list
