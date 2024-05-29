from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Category, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(category.id, category.get_friendly_name()) for category in categories]
        self.fields["category"].choices = friendly_names
        
        for field_name, field in self.fields.items():
            if field_name == "isbn" or "price":
                field.widget.attrs["class"] = "remove-spinner"

            if field_name == "date_published":
                field.widget = forms.DateInput(attrs={"type": "date"})
            
            if field_name == "bookmark":
                field.widget.attrs["class"] = "hide"
                field.label = ""
             
    def clean_date_published(self):
        """Ensures only past dates are selected in the date picker"""
        date_published = self.cleaned_data.get("date_published")
        if date_published >= datetime.date.today():
            raise forms.ValidationError("The publication date must be in the past!")
        return date_published
