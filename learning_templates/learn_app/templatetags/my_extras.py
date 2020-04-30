from django import template

register= template.library()

def cut(value,arg):

    """"

this cuts out all the values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cut',cut)