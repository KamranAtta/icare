from modules.expense.models import Expense

def create_expense(school_id, fee=0.0, books=0.0, uniform=0.0, shoes=0.0, transport=0.0, lunch=0.0, total_amount=0.0):
    try:
        expense = Expense(school_idschool_id, fee=fee, books=books, uniform=uniform, shoes=shoes, transport=transport, lunch=lunch, total_amount=0.0)
        return expense;
    except:
        return None

def get_by_id(expense_id):
    try:
        return Expense.objects.get(id=expense_id)
    except Expense.DoesNotExist:
        return None
