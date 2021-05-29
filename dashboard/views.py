from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from activities.models import Activity
from authentication.views import subscription_check
from coursework.models import Course
from letters.models import Letter
from mcat.models import MCAT
from tasks.models import Task

from .forms import QuickForm

# Create your views here.

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:sorry')
def dashboard(request):
    # Show all letter types and author names in dashboard.
    courses = Course.objects.filter(owner=request.user)
    activities = Activity.objects.filter(owner=request.user)
    bcpm_courses = Course.objects.filter(Q(course_classification='Biology') | Q(course_classification='Chemistry') | Q(course_classification='Math') | Q(course_classification='Physics'), owner=request.user)

    # MCAT
    # Display highest official MCAT score on dashboard.
    # If no official MCAT score, display highest practice score.

    official_data = []
    practice_data = []

    official_score = None
    practice_score = None

    mcat_type = None

    try:
        official_mcat = MCAT.objects.filter(owner=request.user, test_type='Official').latest('mcat_score')
        official_data.append(official_mcat.bio_biochem)
        official_data.append(official_mcat.chem_physics)
        official_data.append(official_mcat.psych_soc)
        official_data.append(official_mcat.cars)
        official_score = official_mcat.mcat_score
    except MCAT.DoesNotExist:
        official_mcat = None

    if official_mcat == None:
        try:
            practice_mcat = MCAT.objects.filter(owner=request.user, test_type='Practice').latest('mcat_score')
            practice_data.append(practice_mcat.bio_biochem)
            practice_data.append(practice_mcat.chem_physics)
            practice_data.append(practice_mcat.psych_soc)
            practice_data.append(practice_mcat.cars)
            practice_score = practice_mcat.mcat_score
        except MCAT.DoesNotExist:
            practice_mcat = None
            mcat_type = None

    else:
        pass

    if not official_mcat:
        mcat_score = practice_score
        mcat_data = practice_data
    else:
        mcat_score = official_score
        mcat_type = 'Official'
        mcat_data = official_data

    grades = {
        'A+':4.0,
        'A':4.0,
        'A-':3.7,
        'AB':3.5,
        'B+':3.3,
        'B':3.0,
        'B-':2.7,
        'BC':2.5,
        'C+':2.3,
        'C':2.0,
        'C-':1.7,
        'CD':1.5,
        'D+':1.3,
        'D':1.0,
        'D-':0.7,
        'DE':0.5,
        'F':0.0,
    }

    # AMCAS Cumulative GPA Calculator
    quality_points = int()
    credits = int()

    for course in courses:
        credits += course.credit_hours

    for course in courses:
        quality_points += (grades[course.transcript_grade]*course.credit_hours)

    try:
        amcas_gpa = quality_points/credits
        amcas_gpa = str(round(amcas_gpa, 2))
    except ZeroDivisionError:
        amcas_gpa = None

    # Display cumulative gpa trend.

    # Display cumulative GPA school year on x-axis.
    cumulative_year = []

    for course in courses:
        cumulative_year.append(course.academic_year)

    cumulative_year = list(set(cumulative_year))
    cumulative_year.sort()

    cumulative_gpa_trend = {
        '2011-2012':None,
        '2012-2013':None,
        '2013-2014':None,
        '2014-2015':None,
        '2015-2016':None,
        '2016-2017':None,
        '2017-2018':None,
        '2018-2019':None,
        '2019-2020':None,
        '2012-2021':None,
        '2021-2022':None,
    }

    for course in courses:
        if course.academic_year == '2011-2012':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2011-2012']=gpa
        if course.academic_year == '2012-2013':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2012-2013']=gpa
        if course.academic_year == '2013-2014':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2013-2014']=gpa
        if course.academic_year == '2014-2015':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2014-2015']=gpa
        if course.academic_year == '2015-2016':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2015-2016']=gpa
        if course.academic_year == '2016-2017':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2016-2017']=gpa
        if course.academic_year == '2017-2018':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2017-2018']=gpa
        if course.academic_year == '2018-2019':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2018-2019']=gpa
        if course.academic_year == '2019-2020':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2019-2020']=gpa
        if course.academic_year == '2020-2021':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2020-2021']=gpa
        if course.academic_year == '2021-2022':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            cumulative_gpa_trend['2021-2022']=gpa

    trend = cumulative_gpa_trend.values()

    cumulative_gpa_trend = [x for x in trend if x is not None]

    # Display BCPM gpa trend.

    bcpm_year = []

    for course in bcpm_courses:
        bcpm_year.append(course.academic_year)

    bcpm_year.sort()

    bcpm_gpa_trend = {
        '2011-2012':None,
        '2012-2013':None,
        '2013-2014':None,
        '2014-2015':None,
        '2015-2016':None,
        '2016-2017':None,
        '2017-2018':None,
        '2018-2019':None,
        '2019-2020':None,
        '2012-2021':None,
        '2021-2022':None,
    }

    for course in bcpm_courses:
        if course.academic_year == '2011-2012':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2011-2012']=gpa
        if course.academic_year == '2012-2013':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2012-2013']=gpa
        if course.academic_year == '2013-2014':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2013-2014']=gpa
        if course.academic_year == '2014-2015':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2014-2015']=gpa
        if course.academic_year == '2015-2016':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2015-2016']=gpa
        if course.academic_year == '2016-2017':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2016-2017']=gpa
        if course.academic_year == '2017-2018':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2017-2018']=gpa
        if course.academic_year == '2018-2019':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2018-2019']=gpa
        if course.academic_year == '2019-2020':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2019-2020']=gpa
        if course.academic_year == '2020-2021':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2020-2021']=gpa
        if course.academic_year == '2021-2022':
            credits = int()
            credits += course.credit_hours
            quality_points = int()
            quality_points += (grades[course.transcript_grade]*course.credit_hours)
            gpa = quality_points/credits
            gpa = str(round(gpa, 2))
            bcpm_gpa_trend['2021-2022']=gpa

    trend = bcpm_gpa_trend.values()

    bcpm_gpa_trend = [x for x in trend if x is not None]

    # AMCAS BCPM (Science) GPA Calculator
    bcpm_quality_points = int()
    credits = int()

    for course in bcpm_courses:
        credits += course.credit_hours
        bcpm_quality_points += (grades[course.transcript_grade]*course.credit_hours)

    try:
        bcpm_gpa = bcpm_quality_points/credits
        bcpm_gpa = str(round(bcpm_gpa, 2))
    except ZeroDivisionError:
        bcpm_gpa = None

    # Activity Hours Quick Form
    form = QuickForm(request.POST)
    form.fields['experience_name'].queryset = Activity.objects.filter(owner=request.user)

    if request.method == 'POST':
        form = QuickForm(request.POST)
        if form.is_valid():

            points = form.cleaned_data['experience_name']
            points.total_hours += form.cleaned_data['hours']
            points.save()
            return redirect('/dashboard')

    context = {
        'activities':activities,
        'bcpm_gpa':bcpm_gpa,
        'amcas_gpa':amcas_gpa,
        'credits':credits,
        'form':form,
        'mcat_data':mcat_data,
        'mcat_score':mcat_score,
        'mcat_type':mcat_type,
        'cumulative_year':cumulative_year,
        'cumulative_gpa_trend':cumulative_gpa_trend,
        'bcpm_year':bcpm_year,
        'bcpm_gpa_trend':bcpm_gpa_trend,
        }
    return render(request, 'dashboard/dashboard.html', context)
