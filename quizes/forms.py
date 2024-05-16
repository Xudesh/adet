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



class LessonTestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tests = kwargs.pop('tests')
        super(LessonTestForm, self).__init__(*args, **kwargs)

        for question in tests:
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



class TestResultQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["lesson"] = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        question = cleaned_data.get("question")

        if question:
            selected_answer = self.data.get(f"question_{question.pk}")
            if selected_answer:
                try:
                    answer = Answer.objects.get(pk=selected_answer)
                    if answer.is_correct:
                        self.instance.score += 1
                except Answer.DoesNotExist:
                    pass

        return cleaned_data