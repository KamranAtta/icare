from modules.users.models import Guardian

def get_guardian_by_user_id(user_id):
    try:
        return Guardian.objects.get(user=user_id)
    except Guardian.DoesNotExist:
        return None
