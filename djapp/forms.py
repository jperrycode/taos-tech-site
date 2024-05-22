from django import forms
from .models import Reviews, StarRatingIntegerChoices

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"

        widgets = {
            'reviewer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'id': 'reviewer_name'}),
            'review_event_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What Event?', 'id': 'review_event_type'}),
            'date_of_event': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Event', 'id': 'date_of_event', 'type': 'date'}),
            'event_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Where?', 'id': 'event_city'}),
            'star_rating': forms.Select(attrs={'class': 'form-select', 'id': 'star_rating'}),
            'review_pass': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'review_pass'}),
            'rating_message_front': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How did we Do?', 'id': 'rating_message_front', 'rows': 3}),
            'rating_message_dj': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Comment for the DJ's eyes only", 'id': 'rating_message_dj', 'rows': 3}),
        }
