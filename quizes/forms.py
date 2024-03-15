from .models import *
from django import forms

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(TestForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = [(a.id, a.text) for a in question.answer_set.all()]
            self.fields[str(question.id)] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect,
                required=True,
                label=question.text
            )

    def calculate_score(self):
        score = 0
        for field_name, selected_answer_id in self.cleaned_data.items():
            selected_answer = Answer.objects.get(id=selected_answer_id)
            if selected_answer.is_correct:
                score += 1
        return score
