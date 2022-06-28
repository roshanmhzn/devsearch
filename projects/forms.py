from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        '''
        Assign css class to the fields
        '''
        super(ProjectForm, self).__init__(*args, **kwargs)
        # we select the title > go in the widgets > attributes 
        # and we want to update the spefific attribute
        #We told it to update the class and go ahead and
        # add this class to it
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        