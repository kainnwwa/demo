from django.forms import ModelForm
from .models import Request


class RequestForm (ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
def save(self, commit=True):
    instance = super().save(commit= False)
    instance.user = self._user
    return super().instance(commit)
