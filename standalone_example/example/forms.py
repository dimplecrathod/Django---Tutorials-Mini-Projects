from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    my_date_field= forms.DateField(widget=DateInput)


class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field': DateInput()}


def is_anagram(x,y):
    return sorted(x) == sorted(y)

class AnagramForm(forms.Form):
    test_value = forms.CharField(
        label='Your name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "input"})
    )

    def clean_test_value(self):
        data = self.cleaned_data.get('test_value')

        if not is_anagram(data, 'listen'):
            raise forms.ValidationError('This is not an anagram of listen.')

        return data