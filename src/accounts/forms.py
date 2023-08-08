from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})