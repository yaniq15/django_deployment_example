from django import template

register= template.Library()
@register.filter(name='cut')
def cut(value, arg):
    """
    :param value:
    :param arg:
    :return:
    This cuts out all values of "arg" from the sting !
    """
    return value.replace(arg, '')

# register.filter('cut', cut)