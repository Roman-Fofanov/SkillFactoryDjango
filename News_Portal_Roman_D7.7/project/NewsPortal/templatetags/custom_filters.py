from django import template

register = template.Library()
@register.filter()
def censor(value):
    censor_list = ['вонючка', 'козлина']
    new_list = list(value.split())
    if isinstance(value, str):
        for i in range(len(new_list)):
            if new_list[i].lower() in censor_list:
                s = new_list[i]
                new_list[i] = s[0] + '*' * len(s)
        return ''.join(new_list)
    else:
        raise TypeError('Объект не является строкой')