from modules.sponsorship.models import Sponsorship
from modules.users.api.user.models import User


def create_sponsorship(relation_id, expense_id, duration=0):
    try:
        sponsorship = Sponsorship(relation_id=relation_id, expense_id=expense_id,duration=duration)
        return sponsorship;
    except:
        return None
