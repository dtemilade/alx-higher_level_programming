#!/usr/bin/python3

"""Executing the modules as scripts:
    by executing the module as the “main” file:
    """

if __name__ == "__main__":

    import hidden_4

    """initializing value for variable to store module"""
    storevar = dir(hidden_4)

    """program conditional statement"""
    for retval in storevar:
        """printing the names based on condition given"""
        if retval[:2] != "__":
            print("{}".format(retval))
