from django.forms import ModelForm
from polls.models import *


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'