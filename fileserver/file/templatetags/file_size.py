from django import template

register = template.Library()

@register.filter
def file_size(value):
    
    if value < 1024:
        return f'{value} bytes'
    elif value < 1024 * 1024:
        return f'{value / 1024:.1f} KB'
    elif value < 1024 * 1024 * 1024:
        return f'{value / 1024 / 1024:.1f} MB'
    elif value < 1024 * 1024 * 1024 * 1024:
        return f'{value / 1024 / 1024 / 1024:.1f} GB'
    else:
        return f'{value / 1024 / 1024 / 1024 / 1024:.1f} TB'
