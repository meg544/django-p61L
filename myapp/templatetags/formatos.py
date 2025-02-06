from django import template

register = template.Library()

@register.filter
def formato_pesos(value):
    """Formatea un valor numérico como pesos mexicanos"""
    try:
        value = float(value)
        return "${:,.2f}".format(value)
    except (ValueError, TypeError):
        return value  # Retorna el valor original si no es un número
