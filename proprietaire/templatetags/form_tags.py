from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={"class": css_class})
    except AttributeError:
        # Si ce n’est pas un champ, retourne tel quel (évite l’erreur)
        return field
