import datetime as dt
import calendar
from datetime import date, datetime, timedelta
from django.views.generic.list import ListView
from .utils import Calendar
from django.utils.safestring import mark_safe

from django.shortcuts import get_object_or_404, render
from .models import (
    Event,
)

# global variables
num_days = calendar.monthrange(date.today().year, date.today().month)[1]
currentMonth = datetime.now().month

ndate = dt.datetime.today()
nxtDate = ndate.strftime('%d')
start_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+nxtDate
res = calendar.monthrange(datetime.now().year, currentMonth)[1]
end_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+str(res)
currentDate = dt.date.today() 
p_start_date = dt.date(currentDate.year, currentDate.month, 1)
p_end_date = dt.date.today() - dt.timedelta(days=1)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# -------------------------------------------- home view --------------------------------------------

def home(request):
            
    # ndate = dt.datetime.today() + dt.timedelta(days=1)
    try:
        #upcoming events
        fdp = Event.objects.filter(eventtype__name__contains="FDP",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date])
        seminar = Event.objects.filter(eventtype__name__contains="Seminar",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date])
        clubevent = Event.objects.filter(eventtype__name__contains="Club Event",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date])
        competition = Event.objects.filter(eventtype__name__contains="Competition",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date])
        otherevents = Event.objects.filter(eventtype__name__contains="Other",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date])
            
        #past events
        p_fdp = Event.objects.filter(eventtype__name__contains="FDP",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date])
        p_seminar = Event.objects.filter(eventtype__name__contains="Seminar",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date])
        p_clubevent = Event.objects.filter(eventtype__name__contains="Club Event",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date])
        p_competition = Event.objects.filter(eventtype__name__contains="Competition",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date])
        p_otherevents = Event.objects.filter(eventtype__name__contains="Other",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date])



    except:
        fdp = None
        seminar = None
        clubevent = None
        competition = None
        otherevents = None
        
        p_fdp = None
        p_seminar = None
        p_clubevent = None
        p_competition = None
        p_otherevents = None

    context = {
        "fdp":fdp,
        "seminar":seminar,
        "clubevent":clubevent,
        "competition":competition,
        "otherevents":otherevents,

        "p_fdp":p_fdp,
        "p_seminar":p_seminar,
        "p_clubevent":p_clubevent,
        "p_competition":p_competition,
        "p_otherevents":p_otherevents,

        "e":Event.objects.filter(date=currentDate).all().count(),
        "pe":Event.objects.filter(date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all().count(),
        "cd":currentDate,
        "ct":current_time,
    }
    # print(Event.objects.filter(date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all().count())
    return render(request, 'Events/home.html',context)

# -------------------------------------------- home view end --------------------------------------------

# -------------------------------------------- individual event detail view --------------------------------------------


def fdp_detail(request,id):
    obj = Event.objects.filter(eventtype__name__contains="FDP").all()
    data = get_object_or_404(obj,pk=id)

    context = {
        'f_data':data,
    }
    return render(request, "Events/fdp-details.html",context)

def seminar_detail(request,id):
    obj = Event.objects.filter(eventtype__name__contains="Seminar").all()
    data = get_object_or_404(obj,pk=id)
    context = {
        's_data':data
    }
    return render(request, "Events/seminar-details.html",context)

def clubevent_detail(request,id):
    obj = Event.objects.filter(eventtype__name__contains="Club Event").all()
    data = get_object_or_404(obj,pk=id)
    context = {
        'ce_data':data
    }
    return render(request, "Events/clubevent-details.html",context)


def competition_detail(request,id):
    obj = Event.objects.filter(eventtype__name__contains="Competition").all()
    data = get_object_or_404(obj,pk=id)
    context = {
        'c_data':data
    }
    return render(request, "Events/competition-details.html",context)


def otherevent_detail(request,id):
    obj = Event.objects.filter(eventtype__name__contains="Other").all()
    data = get_object_or_404(obj,pk=id)
    context = {
        'oe_data':data
    }
    return render(request, "Events/otherevent-details.html",context)

# -------------------------------------------- individual event detail view end --------------------------------------------

# -------------------------------------------- departments list view --------------------------------------------

def departments(request):
    return render(request, 'Events/departments.html')
    
# -------------------------------------------- departments list view end --------------------------------------------

# -------------------------------------------- individual department detail view --------------------------------------------

def it_department(request):

    try: 
        i_event_data = Event.objects.filter(department__name__contains="Information Technology",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        i_event_data_p = Event.objects.filter(department__name__contains="Information Technology",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        i_event_data = None
        i_event_data_p = None
    context = {
        'i_event_data':i_event_data,
        'i_event_data_p':i_event_data_p,
        'iec':i_event_data.count(), 
        'iecp':i_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time
    }

    return render(request,'Events/it_details.html',context)

def cs_department(request):

    try: 
        cs_event_data = Event.objects.filter(department__name__contains="Computer Science",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        cs_event_data_p = Event.objects.filter(department__name__contains="Computer Science",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        cs_event_data = None
        cs_event_data_p = None
    context = {
        'cs_event_data':cs_event_data,
        'cs_event_data_p':cs_event_data_p,
        'csec':cs_event_data.count(), 
        'csecp':cs_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time
    }

    return render(request,'Events/cs_details.html',context)

def civil_department(request):

    try: 
        civil_event_data = Event.objects.filter(department__name__contains="Civil Engineering",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        civil_event_data_p = Event.objects.filter(department__name__contains="Civil Engineering",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        civil_event_data = None
        civil_event_data_p = None
    context = {
        'civil_event_data':civil_event_data,
        'civil_event_data_p':civil_event_data_p,
        'civilec':civil_event_data.count(), 
        'civilecp':civil_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time

    }

    return render(request,'Events/civil_details.html',context)

def ec_department(request):

    try: 
        ec_event_data = Event.objects.filter(department__name__contains="Electrical Communication",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        ec_event_data_p = Event.objects.filter(department__name__contains="Electrical Communication",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        ec_event_data = None
        ec_event_data_p = None
    context = {
        'ec_event_data':ec_event_data,
        'ec_event_data_p':ec_event_data_p,
        'ecec':ec_event_data.count(), 
        'ececp':ec_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time
    }

    return render(request,'Events/ec_details.html',context)

def ee_department(request):

    try: 
        ee_event_data = Event.objects.filter(department__name__contains="Electrical Electronics",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        ee_event_data_p = Event.objects.filter(department__name__contains="Electrical Electronics",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        ee_event_data = None
        ee_event_data_p = None
    context = {
        'ee_event_data':ee_event_data,
        'ee_event_data_p':ee_event_data_p,
        'eeec':ee_event_data.count(),
        'eeecp':ee_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time
    }

    return render(request,'Events/ee_details.html',context)

def mech_department(request):

    try: 
        mech_event_data = Event.objects.filter(department__name__contains="Mechanical Engineering",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[start_date, end_date]).all()
        mech_event_data_p = Event.objects.filter(department__name__contains="Mechanical Engineering",date__month__gte=currentMonth,date__month__lte=currentMonth,date__range=[p_start_date, p_end_date]).all()
    except:
        mech_event_data = None
        mech_event_data_p = None
    context = {
        'mech_event_data':mech_event_data,
        'mech_event_data_p':mech_event_data_p,
        'mechec':mech_event_data.count(),
        'mechecp':mech_event_data_p.count(),
        "cd":currentDate,
        "ct":current_time
    }

    return render(request,'Events/mech_details.html',context)

# -------------------------------------------- individual department detail end --------------------------------------------

# -------------------------------------------- blog view --------------------------------------------

def blogs(request):
    return render(request, 'Events/blog.html')

# -------------------------------------------- blog view end --------------------------------------------

class CalendarView(ListView):
    model = Event
    template_name = 'Events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month