from django.forms import ModelForm, widgets, CharField
from sport.models import QuestionModel
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuestionForms(ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder': _("Your name"), 'name': 'name'}),
            'telenumber': widgets.TextInput(attrs={'class': 'telInput', 'type': 'tel', 'placeholder': _('Phone number'),
                                                   'name': 'tel'}),
            'email': widgets.EmailInput(attrs={'placeholder': _('Your mail'), 'type': 'email'}),
            'msg': widgets.Textarea(attrs={'name': 'text', 'style': 'resize: none', 'placeholder': _('Message')})
        }


class RegisterForms(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForms, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    username = CharField(label='Логин', widget=widgets.TextInput())
    password1 = CharField(label='Пароль', widget=widgets.PasswordInput())
    password2 = CharField(label='Повтор пароля', widget=widgets.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
