from django import forms


from .models import *


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = [

            'Wish_Text',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user',
            'wish',
            'comment_text',
        ]