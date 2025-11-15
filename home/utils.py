from home.models import User
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