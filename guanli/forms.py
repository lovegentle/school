from django import forms

class SearchForm(forms.Form):
    CHOICES = [
        (u'大学学历', u'大学学历'),
        (u'大学名称', u'大学名称')
    ]

    search_by = forms.ChoiceField(
        label='',
        choices=CHOICES,
        widget=forms.RadioSelect(),
        initial=u'大学学历',
    )

    keyword = forms.CharField(
        label='',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': u'请输入需要检索的校院信息',
            'name': 'keyword',
        })
    )
