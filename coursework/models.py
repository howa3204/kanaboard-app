from django.conf import settings
from django.db import models

# Create your models here.

class Course(models.Model):
    YEAR = (
        ('2021-2022', '2021-2022'),
        ('2020-2021', '2020-2021'),
        ('2019-2020', '2019-2020'),
        ('2018-2019', '2018-2019'),
        ('2017-2018', '2017-2018'),
        ('2016-2017', '2016-2017'),
        ('2015-2016', '2015-2016'),
        ('2014-2015', '2014-2015'),
        ('2013-2014', '2013-2014'),
        ('2012-2013', '2012-2013'),
        ('2011-2012', '2011-2012'),
    )
    academic_year = models.CharField(max_length=9, choices=YEAR)
    TERM = (
        ('Summer Semseter (Summer)', 'Summer Semseter (Summer)'),
        ('First Semester (Fall)', 'First Semester (Fall)'),
        ('2nd Semester (Spring)', '2nd Semester (Spring)'),
        ('Mini Semester (Winter/Spring)', 'Mini Semester (Winter/Spring)'),
        ('Full Year Course - Semester System', 'FullYear Course - Semester System'),
        ('Summer Quarter (Summer)', 'Summer Quarter (Summer)'),
        ('1st Quarter (Fall)', '1st Quarter (Fall)'),
        ('2nd Quarter (Winter)', '2nd Quarter (Winter)'),
        ('3rd Quarter (Spring)', '3rd Quarter (Spring)'),
        ('Full Year Course - Qaurter System', 'FullYear Course - Qaurter System'),
        ('Summer Trimester (Summer)', 'Summer Trimester (Summer)'),
        ('1st Trimester (Fall)', '1st Trimester (Fall)'),
        ('2nd Trimester (Winter)', '2nd Trimester (Winter)'),
        ('3rd Trimester (Spring)', '3rd Trimester (Spring)'),
        ('FullYear Course - Trimester System', 'FullYear Course - Trimester System'),
        ('Summer Semester (Summer)', 'Summer Semester (Summer)'),
        ('1st Semester (Fall)', '1st Semester (Fall)'),
        ('2nd Semester (Spring)', '2nd Semester (Spring)'),
        ('Mini Semester (Winter/Spring)', 'Mini Semester (Winter/Spring)'),
        ('Full Year Course - 4-1-4 / 4-4-1 System', 'Full Year Course - 4-1-4 / 4-4-1 System'),
        ('Other Term', 'Other Term'),
    )
    academic_term = models.CharField(max_length=39, choices=TERM)
    SCHOOL_YEAR = (
        ('High School', 'High School'),
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Postbaccalaureate Undergraduate', 'Postbaccalaureate Undergraduate'),
        ('Graduate', 'Gradutae'),
    )
    school_year = models.CharField(max_length=31, choices=SCHOOL_YEAR)
    course_number = models.PositiveIntegerField()
    course_name = models.CharField(max_length=100)
    CLASSIFICATION = (
        ('Behavioral & Social Sciences', 'Behavioral & Social Sciences'),
        ('Biology', 'Biology'),
        ('Business', 'Business'),
        ('Chemistry', 'Chemistry'),
        ('Communications', 'Communications'),
        ('Computer Science/Technology', 'Computer Science/Technology'),
        ('Education', 'Education'),
        ('Engineering', 'Engineering'),
        ('English Language & Literature', 'English Language & Literature'),
        ('Fine Arts', 'Fine Arts'),
        ('Foreign Languages & Literature', 'Foreign Languages & Literature'),
        ('Government/Political Science/Law', 'Government/Political Science/Law'),
        ('Health Sciences', 'Health Sciences'),
        ('History', 'History'),
        ('Math', 'Math'),
        ('Natural/Physical Sciences', 'Natural/Physical Sciences'),
        ('Other', 'Other'),
        ('Philosophy/Religion', 'Philosophy/Religion'),
        ('Physics', 'Physics'),
        ('Special Studies', 'Special Studies'),
    )
    course_classification = models.CharField(max_length=32, choices=CLASSIFICATION)
    credit_hours = models.PositiveIntegerField()
    GRADE = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('AB', 'AB'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('BC', 'BC'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('CD', 'CD'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('D-', 'D-'),
        ('DE', 'DE'),
        ('F', 'F'),
    )
    transcript_grade = models.CharField(max_length=2, choices=GRADE)
    LAB = (
        ('Lecture Only', 'Lecture Only'),
        ('Lab Only', 'Lab Only'),
        ('Combined Lecture and Lab', 'Combined Lecture and Lab'),
    )
    include_lab = models.CharField(max_length=24, choices=LAB)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_name)

    class Meta:
        verbose_name_plural = "coursework"
