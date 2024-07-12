from predict_training import predict_training
from parsing_youtube_video import get_1st_video


def result(completed_training, history):
    segmentation = ["Верх", "Низ", "Смешанная"]
    if history[0] not in segmentation:
        raise Exception("Неверный тип тренировки")
    else:
        segmentation = segmentation.index(history[0])
    goal = ["Потеря веса", "Наращивание мышечной массы", "Улучшение выносливости"]
    if history[1] not in goal:
        raise Exception("Неверная цель тренировки")
    else:
        goal = goal.index(history[1])
    healthlimit =  ["Без ограничений", "Пресс", "Приводящие мышцы", "Отводящие мышцы", "Бицепсы", "Икроножные мышцы", "Грудные мышцы",
                "Предплечья", "Ягодичные мышцы", "Подколенные сухожилия", "Широчайшие мышцы спины",
                "Нижняя часть спины", "Средняя часть спины",
                "Шея",
                "Квадрицепсы",
                "Плечи",
                "Трапеции",
                "Трицепсы"]
    if history[2] not in healthlimit:
        raise Exception("Указано неверное ограничение по здоровью")
    else:
        healthlimit = healthlimit.index(history[2])
    tire = int(history[3])
    if tire < 0 or tire > 5:
        raise Exception("Указано неверный уровень усталости")
    time = int(history[4])
    if time <= 0:
        raise Exception("Указано неверное время тренировки")
    quant = int(history[5])
    if quant <= 0:
        raise Exception("Указано некорректное количество упражнений")
    type = ["Кардио", "Олимпийские поднятия весов", "Плиометрика", "Паверлифтинг", "Силовая", "Растяжка", "Стронгман"]
    if history[6] not in type:
        raise Exception("Неверный тип тренировки")
    else:
        type = type.index(history[6])
    bodypart = ["Пресс", "Приводящие мышцы", "Отводящие мышцы", "Бицепсы", "Икроножные мышцы", "Грудные мышцы",
                "Предплечья", "Ягодичные мышцы", "Подколенные сухожилия", "Широчайшие мышцы спины",
                "Нижняя часть спины", "Средняя часть спины",
                "Шея",
                "Квадрицепсы",
                "Плечи",
                "Трапеции",
                "Трицепсы"]
    if history[7] not in bodypart:
        raise Exception("Указана неверная часть тела")
    else:
        bodypart = bodypart.index(history[7])
    equipment = [
        "Резинки",
        "Штанга",
        "Собственный вес",
        "Кроссовер",
        "Гантели",
        "Изогнутый гриф",
        "Гимнастический мяч",
        "Пенопластовый ролик",
        "Гиря",
        "Тренажер",
        "Медицинский мяч",
        "Другое",
        "Без инвентаря"
    ]
    if history[8] not in equipment:
        raise Exception("Указан неверный инвентарь")
    else:
        equipment = equipment.index(history[8])
    level = ["Начинающий", "Эксперт", "Продвинутый"]
    if history[9] not in level:
        raise Exception("Указан неверный уровень физической подготовки")
    else:
        level = level.index(history[9])
    nametraining = predict_training(completed_training, segmentation, goal, healthlimit, tire, time, quant, type, bodypart, equipment, level, top_k=3)
    names = [nt[1] for nt in nametraining]
    videotraining = get_1st_video(names)
    return ([(name, video) for name, video in zip(names, videotraining)])
