from django import template

register = template.Library()

def add_plus(value):
    return int(value) + 1

def add_minus(value):
    return int(value) - 1

register.filter("add_plus", add_plus)
register.filter("add_minus", add_minus)