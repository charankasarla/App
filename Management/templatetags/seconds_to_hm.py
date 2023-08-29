from django import template

register = template.Library()

@register.simple_tag(takes_context=True)

def seconds_to_hm(context, seconds, day=''):
    if seconds == '' or seconds is None:
        return ''

    if type(seconds) == str:
        return seconds

    if seconds >= 86400:
        days = int(seconds / 86400)
        hours = int((seconds % 86400) / 3600)
        return ("%d.%02d" % (days, hours))

    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    return ("%02d:%02d" % (hours, minutes % 60))
