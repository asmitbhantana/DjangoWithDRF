from django.forms import Form,ModelForm
from .models import StatusMessage
class StatusMessageModelFOrm(ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['status']
