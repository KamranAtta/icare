from modules.sponsorship.models import Sponsorship

def create_sponsorship(relation, expense, donation=0, duration=0, is_active=False):
    try:
        sponsorship = Sponsorship.objects.get(relation=relation)
    except Sponsorship.DoesNotExist:
        sponsorship = Sponsorship(relation=relation, expense=expense, donation=donation, duration=duration, is_active=is_active)
        sponsorship.save()
    return sponsorship

# def create_sponsorship(relation, expense, **data):
#     try:
#         sponsorship = Sponsorship.objects.get(relation=relation)
#     except Sponsorship.DoesNotExist:
#         sponsorship = Sponsorship(relation=relation, expense=expense, duration=data['duration'])
#         sponsorship.save()
#     return sponsorship
