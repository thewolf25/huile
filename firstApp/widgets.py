from django.forms.widgets import TextInput

class DateTimeInput(TextInput):
    input_type = 'datetime-local'
    