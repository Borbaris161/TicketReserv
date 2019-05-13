def red(apps, scheme_editor):
    '''
    Добавление данных в модель
    '''
    new_model = apps.get_model("halls", "Hall")
    result = new_model.objects.create(
        title='red',
        rows=10,
        seats=11
    )

def yellow(apps, scheme_editor):
    '''
    Добавление данных в модель
    '''
    new_model = apps.get_model("halls", "Hall")
    result = new_model.objects.create(
        title='yellow',
        rows=11,
        seats=12
    )


def green(apps, scheme_editor):
    '''
    Добавление данных в модель
    '''
    new_model = apps.get_model("halls", "Hall")
    result = new_model.objects.create(
        title='green',
        rows=12,
        seats=13
    )


def black(apps, scheme_editor):
    '''
    Добавление данных в модель
    '''
    new_model = apps.get_model("halls", "Hall")
    result = new_model.objects.create(
        title='black',
        rows=13,
        seats=14
    )