from collections import defaultdict

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
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def dashboard(request):
    # Show all letter types and author names in dashboard.
    courses = Course.objects.filter(owner=request.user)
    activities = Activity.objects.filter(owner=request.user)
    bcpm_courses = Course.objects.filter(Q(course_classification='Biology') | Q(course_classification='Chemistry') | Q(course_classification='Math') | Q(course_classification='Physics'), owner=request.user)

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
        mcat_type = 'Practice'
    else:
        mcat_score = official_score
        mcat_data = official_data
        mcat_type = 'Official'

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

    # Display cumulative GPA school year on x-axis.
    cumulative_year = []

    for course in courses:
        cumulative_year.append(course.academic_year)

    cumulative_year = list(set(cumulative_year))
    cumulative_year.sort()

    # Display cumulative GPA on y-axis.
    years_dict = defaultdict(list)

    for course in courses:
        credits = int()
        credits += course.credit_hours
        quality_points = int()
        quality_points += (grades[course.transcript_grade]*course.credit_hours)
        gpa = quality_points/credits
        gpa = round(gpa, 2)
        years_dict[course.academic_year].append(gpa)

    for year,gpa in years_dict.items():
        years_dict[year] = sum(gpa)/float(len(gpa))

    cumulative_gpa_trend = [years_dict[key] for key in sorted(years_dict.keys())]

    # Display science GPA school year on x-axis.
    bcpm_year = []

    for course in bcpm_courses:
        bcpm_year.append(course.academic_year)

    bcpm_year = list(set(bcpm_year))
    bcpm_year.sort()

    # Display cumulative GPA on y-axis.
    bcpm_years_dict = defaultdict(list)

    for course in bcpm_courses:
        credits = int()
        credits += course.credit_hours
        quality_points = int()
        quality_points += (grades[course.transcript_grade]*course.credit_hours)
        gpa = quality_points/credits
        gpa = round(gpa, 2)
        bcpm_years_dict[course.academic_year].append(gpa)

    for year,gpa in bcpm_years_dict.items():
        bcpm_years_dict[year] = sum(gpa)/float(len(gpa))

    bcpm_gpa_trend = [bcpm_years_dict[key] for key in sorted(bcpm_years_dict.keys())]

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
