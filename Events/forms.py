from datetime import date
from django import forms
from .models import Event

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

today = date.today()


events = Event.objects.filter(mode="OFFLINE", date=today).all()


class EventForm(forms.ModelForm):
    def clean(self):
        venue = self.cleaned_data['venue']
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        date = self.cleaned_data['date']

        events = Event.objects.filter(mode="OFFLINE", date=date, venue=venue).all()
        for e in events:
            if bool(start_time == end_time):
                raise forms.ValidationError("Start time and End time cannot be same")
            if bool(start_time < e.start_time and end_time <= e.start_time) or bool(start_time >= e.end_time and end_time > e.end_time):
                pass
            else:
                raise forms.ValidationError(f"Place already booked for this time {e.start_time} to {e.end_time} on {e.date} at {e.venue}")
        return self.cleaned_data

# class StatusForm(forms.Form):

#     # status = forms.BooleanField(required=False
#         # widget=forms.CheckboxInput(
#         #     # attrs={'onclick':'this.form.submit();'}),
#         #     required=False, 
#         #     label="Get live events"
#         # )

#     status = forms.BooleanField(
#         widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}),
#         required=False, label="Status"
#         )

