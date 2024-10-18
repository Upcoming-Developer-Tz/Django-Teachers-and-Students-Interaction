from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Statuses(models.Model):
    StatusName = models.CharField(max_length=100, verbose_name='Status Name')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['StatusName','CreatedDate','ModifiedDate']

    def __str__(self):
        return self.StatusName
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher', verbose_name='User')
    firstName = models.CharField(max_length=100, default='John', verbose_name='First Name')
    lastName = models.CharField(max_length=100, default='Doe', verbose_name='Last Name')
    subject = models.ForeignKey('Subjects', on_delete=models.CASCADE, verbose_name='Subject Name', default=1)  # Assuming ID 1 exists
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, verbose_name='Status')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    modifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['firstName','lastName', 'subject','createdDate','modifiedDate']

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers' 

class SchoolLevels(models.Model):
    LevelName = models.CharField(max_length=100, verbose_name='Level Name')
    level_order = models.IntegerField(unique=True, verbose_name='Level Order')  # Add this field
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['LevelName','CreatedDate','ModifiedDate']

    def __str__(self):
        return self.LevelName
    
    class Meta:
        verbose_name = 'School Level'
        verbose_name_plural = 'School Levels'

class SchoolClases(models.Model):
    ClassName = models.CharField(max_length=100, verbose_name='Class Name')
    SchoolLevel = models.ForeignKey(SchoolLevels, on_delete=models.CASCADE, verbose_name='School Level')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['ClassName','SchoolLevel','CreatedDate','ModifiedDate']

    def __str__(self):
        return self.ClassName
    
    class Meta:
        verbose_name = 'School Class'
        verbose_name_plural = 'School Clases'


class Subjects(models.Model):
    SubjectName = models.CharField(max_length=100, verbose_name='Subject Name')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['SubjectName', 'CreatedDate','ModifiedDate']

    def __str__(self):
        return self.SubjectName
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class AssignToClasses(models.Model):
    Teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name='Teacher Name')
    School = models.ForeignKey(SchoolClases, on_delete=models.CASCADE, verbose_name='Class Name')
    Subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Subject Name')
    Status = models.ForeignKey(Statuses, on_delete=models.CASCADE, verbose_name='Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['Teacher','School','Subject','Status','CreatedDate','ModifiedDate']

    # def __str__(self):
    #     return self.Teacher
    
    class Meta:
        verbose_name = 'Assign To Class'
        verbose_name_plural = 'Assign To Classes'
        
        
class Questions(models.Model):
    QuestionName = models.TextField(verbose_name='Question Name')
    LevelName = models.ForeignKey(SchoolLevels, on_delete=models.CASCADE, verbose_name='Level Name')
    SubjectName = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Subject Name')
    IsApproved = models.BooleanField(verbose_name='Is Approved')
    ApprovedBy = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name='Approved By')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['QuestionName','LevelName','SubjectName','IsApproved','ApprovedBy','CreatedDate','ModifiedDate']

    def __str__(self):
        return self.QuestionName
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    QuestionName = models.ForeignKey(Questions, related_name='answers', on_delete=models.CASCADE, verbose_name='Question Name')
    Answer = models.TextField(verbose_name='Answer')
    IsApproved = models.BooleanField(verbose_name='Is Approved')
    ApprovedBy = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name='Approved By')
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    ModifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['QuestionName','Answer','IsApproved','ApprovedBy','CreatedDate','ModifiedDate']

    def __str__(self):
        return self.Answer

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', verbose_name='User')
    firstName = models.CharField(max_length=100, verbose_name='First Name')
    middleName = models.CharField(max_length=100, verbose_name='Middle Name')
    lastName = models.CharField(max_length=100, verbose_name='Last Name')
    gender = models.CharField(max_length=100, verbose_name='Gender')
    dob = models.DateField(verbose_name='Date of Birth')
    schoolLevel = models.ForeignKey(SchoolLevels, on_delete=models.CASCADE, verbose_name='School Level')
    className = models.ForeignKey(SchoolClases, on_delete=models.CASCADE, verbose_name='School Class')
    address = models.CharField(max_length=100, verbose_name='Address')
    academicYear = models.IntegerField(verbose_name='Academic Year')
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, verbose_name='Status')
    emailAddress = models.CharField(max_length=100, verbose_name='Email Address')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    modifiedDate = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    display_fields = ['firstName','middleName','lastName','gender','address','createdDate','modifiedDate', 'emailAddress']

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students' 

