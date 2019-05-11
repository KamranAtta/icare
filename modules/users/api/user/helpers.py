from modules.users.models import User, Admin, Student, Guardian, Relation
from django.utils.translation import ugettext_lazy as _
from django.db import transaction


def validate(data):
    if data['password1'] != data['password2']:
        raise serializers.ValidationError(_('THe passwords do not match'))

def user_get_by_name(username):
    try:
        return User.objects.get(username=username)
    except:
        return None

def user_get_by_email_address(email):
    try:
        return User.objects.get(email=email)
    except:
        return None

def validate_email(email):
    try:
        return User.objects.get(email=email)
    except:
        return None

def user_is_verified(user_id):
        try:
                return User.objects.get(id=user_id)
        except:
                return None

def get_user_role_by_id(user_id):
    try:
        user = Guardian.objects.get(user_id=user_id)
        if user:
            return 0
    except Guardian.DoesNotExist:
        pass
    try:
        user = Student.objects.get(user_id=user_id)
        if user:
            return 1
    except Student.DoesNotExist:
        pass
    try:
        user = Admin.objects.get(user_id=user_id)
        if user:
            return 2
    except Admin.DoesNotExist:
        pass

    return None

def create_relation(guardian, student):
    try:
        relation = Relation.objects.get(guardian=guardian, student=student)
    except Relation.DoesNotExist:
        relation = Relation(guardian=guardian, student=student)
        relation.save()

    return relation

@transaction.atomic
def user_create(username, password, first_name, last_name, email, role=1):
    if email:
        email = email.lower()
    m = User(username=username, first_name=first_name, last_name=last_name, email=email)
    m.set_password(password)
    m.save()

    User.ROLES[role](m)

    return m
