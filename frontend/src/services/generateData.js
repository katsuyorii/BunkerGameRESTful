export function generateData(category) {
    let title;

    switch (category) {
        case 'bunker':
            title = 'Бункер';
            break;
        case 'catastrophe':
            title = 'Катастрофа';
            break;
        case 'character':
            title = 'Персонаж';
            break;
        case 'gender':
            title = 'Пол, возраст';
            break;
        case 'health':
            title = 'Состояние здоровья';
            break;
        case 'profession':
            title = 'Профессия';
            break;
        case 'hobby':
            title = 'Хобби';
            break;
        case 'phobia':
            title = 'Фобия';
            break;
        case 'trait':
            title = 'Человеческая черта';
            break;
        case 'physique':
            title = 'Телосложение';
            break;
        case 'baggage':
            title = 'Багаж';
            break;
        case 'addinfo':
            title = 'Доп. информация';
            break;
        case 'rooms':
            title = 'Комнаты бункера';
            break;
        case 'items':
            title = 'Предметы в бункере';
            break;
        default:
            title = 'Выберите характеристику для генерации...';
    }

    return { title };
}