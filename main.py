import write_login
link_list_ = []

# TODO: to add country in final_list dic, to make it more clearer
# TODO: to add extra cases of possible portal examples and test it


if __name__ == '__main__':

    link_list_ = write_login.get_link("links1.csv")
    final_list = write_login.check_driver(link_list_)
    write_login.write_login_function(final_list)