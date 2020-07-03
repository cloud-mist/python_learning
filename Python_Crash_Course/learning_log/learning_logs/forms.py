from django import forms

from .models import Topic
#定义了一个class，继承于ModelForm
class TopicForm(forms.ModelForm): 
    class Meta:
        model = Topic
        fields = ['text']
        labels =  {'text': ''}