from django.forms import ModelForm
from .models import Request

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['service', 'comment']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        instance.status = 0
        if commit:
            instance.save()
        return instance