from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Category, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        print(model)
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

        placeholders = {
            "category": "",
            "title": "Title",
            "summary": "Summary",
            "author": "Author",
            "isbn": "ISBN",
            "price": "Price",
            "pages": "Pages",
            "series": "Series",
            "number_in_series": "Number in Series",
            "date_published": "Date Published",
            "cover": "Cover Image"
        }
        
        for field_name, field in self.fields.items():
            if field_name in placeholders:
                if field.required:
                    placeholder = f"{placeholders[field_name]} *"
                else:
                    placeholder = placeholders[field_name]
            field.widget.attrs["placeholder"] = placeholders[field_name]
            
            if field_name != "cover":
                field.label = ""
            else:
                field.label = "Cover"

            if field_name == "isbn" or "price":
                field.widget.attrs["class"] = "remove-spinner"

            if field_name == "date_published":
                field.widget = forms.DateInput(attrs={"type": "date"})
            
    def clean_date_published(self):
        date_published = self.cleaned_data.get("date_published")
        if date_published >= datetime.date.today():
            raise forms.ValidationError("The publication date must be in the past!")
        return date_published
