#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        ret = fct(*args)
    except Exception as err:
        ret = None
        message = "Exception: " + str(err) + "\n"
        stderr.write(message)
    finally:
        return ret
