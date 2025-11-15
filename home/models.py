from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel


class User(AbstractUser, BaseModel):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    
   
    t_yil = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan yil")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon raqami")
    phone2 = models.CharField(max_length=15, blank=True, null=True, verbose_name="Qo'shimcha telefon raqami")
    profil_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Profil rasmi")
    
    started_at = models.DateField(null=True, blank=True, verbose_name="Ish boshlagan sana")
    
    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions_set",
        related_query_name="custom_user_permission",
    )

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    @property
    def is_student(self):
        return self.user_type == 'student' # views faylida ishlatish uchun, user.is_student qilib user typeni olish oson
    
    @property
    def is_teacher(self):
        return self.user_type == 'teacher'


# sum() davomli element berilsa, o'sha elementni yig'indisini

class Coins(BaseModel):
    count = models.IntegerField(default=0)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'}, related_name="coins") #  limit_choices_to={'user_type': 'student'} bu qism aynan student yozilishini ta'minlash uchun
    
    def __str__(self):
        return f"Coins: {self.count} (Updated at: {self.updated_at})"


class Transactions(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'}, related_name='transactions_set')
    reason = models.CharField(max_length=255)
    amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=[
        ("50", "50 To'lov"),
        ("30", "30 Homework"),
        ("10", "10 Davomat"),
        ("5", "5 Other"),
    ])

    def __str__(self):
        return f"Transaction of {self.amount} for {self.student} - Status: {self.status}"


class Item(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    image = models.ImageField(upload_to='item_images/', verbose_name="Rasm")
    info = models.TextField(verbose_name="Ma'lumot")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Narxi")
    total = models.IntegerField(verbose_name="Mavjud soni")
    category = models.CharField(max_length=100, verbose_name="Kategoriyasi", null=True, blank=True, default="Umumiy")

    def __str__(self):
        return self.name
    
class Purchase(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'}, related_name="purchases")
    maxsulot = models.ForeignKey(Item, on_delete=models.CASCADE)
    miqdor = models.IntegerField(default=1)

    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Purchase of {self.maxsulot} - Status: {self.status}"


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    content = models.TextField(max_length=2000,verbose_name="Kontent")
    news_date = models.DateTimeField(auto_now_add=True, verbose_name="Nashr qilingan sana")
    news_image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Rasm") 

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-news_date']

class Group(BaseModel):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teaching_groups', limit_choices_to={'user_type': 'teacher'})
    students = models.ManyToManyField(User, related_name='student_groups', limit_choices_to={'user_type': 'student'}) #ko'pgina studentlar va ko'pgina grouplar o'zaro bog'lanishi uchun

    def __str__(self):
        return self.name
    
    
    
