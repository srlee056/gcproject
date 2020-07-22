from djongo import models
from django import forms

class Party(models.Model):
    title = models.CharField(max_length=100)
    '''
    class Meta:
        abstract = True

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = (
            'title',
        )
'''
class Player(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level = models.IntegerField()
    '''
    party_embed = models.EmbeddedField(
        model_container=Party,
        #model_form_class=PartyForm,
    )
'''