from django import forms

from to_do_list.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'start_date', 'end_date')

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'start_date', 'end_date', 'is_completed')