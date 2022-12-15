from django import template
from firstApp.models import DegustateursNotes,Commande
register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.filter(name='has_group') 
def has_group(user, group_name):
    group = group_name[1:-1].split(',')  # ['1', '3', '5', '7']
    print(group)
    return user.groups.filter(name__in=group).exists()

@register.filter(name="degustateur_note")
def getNote(user,commande):
    notes = DegustateursNotes.objects.filter(user=user, commande=Commande.objects.get(pk=int(commande))).first()
    return notes.note