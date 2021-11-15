"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваш никнейм', min_length=2, max_length=100)
    city = forms.CharField(label='Какую игру купили', min_length=2, max_length=100)
    
    gender = forms.ChoiceField(label='Для какого сервиса вы взяли ключ?', 
                             choices=[('1', 'Steam'), ('2', 'Gog'), ('3', 'Epic games store')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='С какими проблемаами столкнулись?',
                                 choices=(('1', 'Не было проблем'),
                                          ('2', 'Ключ долго не приходил'),
                                          ('3', 'Пришел ключ не от той игры'),
                                          ('4', 'Ключ оказался нерабочим')), initial=1)
    notice = forms.BooleanField(label='Хотите получать нашу новостную рассылку на скидки и акции?',
                                required=False)
    email = forms.EmailField(label='Email', min_length=7)
    message = forms.CharField(label='Ваши впечатления от сайта',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':40}))
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}