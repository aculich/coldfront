from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


# settings value
@register.simple_tag
def settings_value(name):
    allowed_names = [
        'LOGIN_FAIL_MESSAGE',
        'ACCOUNT_CREATION_TEXT',
        'CENTER_NAME',
        'CENTER_HELP_URL',
        'EMAIL_PROJECT_REVIEW_CONTACT',
    ]
    return mark_safe(getattr(settings, name, '') if name in allowed_names else '')


@register.filter
def get_icon(expand_accordion):
    if expand_accordion == 'show':
        return 'fa-minus'
    else:
        return 'fa-plus'


@register.filter
def convert_boolean_to_icon(boolean):
    if boolean == False:
        return mark_safe('<span class="badge badge-success"><i class="fas fa-check"></i></span>')
    else:
        return mark_safe('<span class="badge badge-danger"><i class="fas fa-times"></i></span>')


@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict_data.get(key)
