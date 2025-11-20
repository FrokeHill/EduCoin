from home.models import User, Group
from django.db.models import Count

def get_student(request):
        user = request.user

        coin_obj = user.coins.first()
        total_coins = coin_obj.count if coin_obj else 0
        groups = user.student_groups.all()
        transactions = user.transactions_set.all().order_by('-created_at')
        
        studentlar = User.objects.filter(
            user_type='student',

            coins__isnull=False
        ).annotate(
            coin_count=Count("coins")
        ).order_by('-coin_count')
        
        user_rank = None
        for index, student in enumerate(studentlar, start=1):
            if student.id == user.id:
                user_rank = index
                break
            
        context = {
            "coin": total_coins,
            "user_type": "student",
            "username": user.username,
            "full_name": user.get_full_name() or user.username,
            "t_yil": user.t_yil,
            "groups": groups,
            "daraja": user_rank,
            "email": user.email,
            "phone": user.phone,
            "transactions": transactions,
            "email": user.email,
        }

        return context
    
def get_teacher(request):
    user = request.user

    students = User.objects.filter(user_type="student")
    guruhlar = Group.objects.filter(teacher=user)
    
    # studentlar = User.objects.filter(
    #         user_type='student',

            
    #     ).annotate(
    #         students_count=Count("coins")
    #     ).order_by('-coin_count')
    context = {
            "started_at": user.started_at,
            "user_type": "teacher",
            "username": user.username,
            "full_name": user.get_full_name() or user.username,
            "guruhlar": guruhlar,
        }
    
    return context