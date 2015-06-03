from django import template
register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, args):
	if args is None:
		return False
	args_list = [arg.strip() for arg in args.split(',')]
	attr_name = args_list[0]
	css = args_list[1]
	return field.as_widget(attrs={ attr_name:css})