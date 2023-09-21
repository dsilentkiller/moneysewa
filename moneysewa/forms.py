from tinymce.widgets import TinyMCE

class WebsiteForm (forms.Form):
    subject= forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget = TinyMCE(), label="Email content")
