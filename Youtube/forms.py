from django import forms
from django.forms.widgets import NumberInput



class SearchForm(forms.Form):
    channel_id_choises = (('', ''), ('completed', 'completed'), ('live', 'live'), ('upcoming', 'upcoming'),)
    v_type_choises = (('', ''), ('channel', 'channel'), ('playlist', 'playlist'), ('video', 'video'),)
    order_choises = (('', ''), ('date', 'date'), ('rating', 'rating'), ('relevance', 'relevance'),
                     ('title', 'title'), ('videoCount', 'videoCount'), ('viewCount', 'viewCount'),)
    duration_choises = (('', ''), ('any', 'any'), ('long', 'long'), ('medium', 'medium'), ('short', 'short'),)

    q = forms.CharField(label='search_text', max_length=100)
    channelId = forms.CharField(label='channelId', max_length=100, required=False)
    eventType = forms.ChoiceField(label='eventType', choices=channel_id_choises, required=False)
    type = forms.ChoiceField(label='v_type', choices=v_type_choises, required=False)
    order = forms.ChoiceField(label='order', choices=order_choises, required=False)
    location = forms.CharField(max_length=38, required=False,
                                widget=forms.TextInput(attrs={'placeholder': '49.62204323535563, 34.5206964068785'}))
    location_radius = forms.IntegerField(min_value=0, max_value=1000, required=False)
    maxResults = forms.IntegerField(min_value=1, max_value=50, initial=5)
    videoDuration = forms.ChoiceField(label='order', choices=duration_choises, required=False)
    publishedAfter = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required=False)
    publishedBefore = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required=False)
    relatedToVideoId = forms.CharField(label='relatedToVideoId', max_length=100, required=False)

    def clean(self):
        data = super().clean()
        location = data.get('location')
        location_radius = data.get('location_radius')
        published_after = data.get('publishedAfter')
        published_before = data.get('publishedBefore')

        if location and not location_radius:
            raise forms.ValidationError('you need to set location_radius if you want to use location')
        if published_after and published_before:
            if published_after >= published_before:
                raise forms.ValidationError('published_after should be less then published_before')
        return data


