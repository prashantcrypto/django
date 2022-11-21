from django.db import models


class Contact(models.Model):
    clint_name = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=200, default='')
    clint_email = models.EmailField(default='')
    pub_date = models.DateTimeField(auto_now_add=True, blank=False,)

    def __str__(self):
        return 'Massage from '+self.clint_name


class Subscribe(models.Model):
    s_email = models.EmailField(

    )

    pub_date: models.DateTimeField('date published')

    def __str__(self):
        return self.s_email


class Empoly(models.Model):
    Emp_name = models.CharField(max_length=50)
    Emp_photo = models.ImageField(
        upload_to='empoly_img', default=None, null=True)
    Emp_design = models.CharField(max_length=30)
    Emp_email = models.EmailField()
    Emp_contact = models.CharField(max_length=13)

    def __str__(self):
        return 'Data of '+self.Emp_name


class Review(models.Model):
    clint_name = models.CharField(max_length=50)
    clint_photo = models.ImageField(
        upload_to='clint_img', default=None, null=True)
    company_name = models.CharField(max_length=50)
    reviw = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False,)

    def __str__(self):
        return 'review of '+self.clint_name


class Project(models.Model):
    c_choice = (
        ('Web app', 'Web app'),
        ('Nfts', 'Nfts'),
        ('minting ui', 'Minting ui'),
    )
    project_name = models.CharField(max_length=50)
    project_photo = models.ImageField(
        upload_to='Project_img', default=None, null=True)

    pub_date = models.DateTimeField(auto_now_add=True, blank=False,)

    category = models.CharField(max_length=25, choices=c_choice)

    def __str__(self):
        return 'Project from '+self.project_name
