from db_analyst.models import Purposes


def select_db_purposes():
    """Получаем результат из БД таблицы Purposes"""
    result = Purposes.objects.all().values_list('machine', 'apartment', 'vacation', 'another_target')
    return result


def insert_db_purposes(machine, apartment, vacation, another_target):
    result = Purposes.objects.create(machine=machine, apartment=apartment, vacation=vacation, another_target=another_target)
    return result


