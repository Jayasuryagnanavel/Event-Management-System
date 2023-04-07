from django import template
register = template.Library()
    
  
@register.simple_tag
def time_in_range(start, end, x):
    if str(start) <= x <= str(end):
        return "Event is live now"
    else:
        return "inactive"

