from modules.users.models import Student

def get_student_by_user_id(user_id):
    try:
        return Student.objects.get(user=user_id)
    except Student.DoesNotExist:
        return None
