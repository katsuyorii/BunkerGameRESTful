export function generateData(category) {
    let title, content;

    switch (category) {
        case 'bunker':
            title = 'Бункер';
            content = 'Бункер';
            break;
        case 'catastrophe':
            title = 'Катастрофа';
            content = 'Катастрофа';
            break;
        case 'character':
            title = 'Персонаж';
            content = 'Персонаж';
            break;
        case 'gender':
            title = 'Пол, возраст';
            content = 'Пол, возраст';
            break;
        case 'health':
            title = 'Состояние здоровья';
            content = 'Состояние здоровья';
            break;
        case 'profession':
            title = 'Профессия';
            content = 'Профессия';
            break;
        case 'hobby':
            title = 'Хобби';
            content = 'Хобби';
            break;
        case 'phobia':
            title = 'Фобия';
            content = 'Фобия';
            break;
        case 'trait':
            title = 'Человеческая черта';
            content = 'Человеческая черта';
            break;
        case 'physique':
            title = 'Телосложение';
            content = 'Телосложение';
            break;
        case 'baggage':
            title = 'Багаж';
            content = 'Багаж';
            break;
        case 'addinfo':
            title = 'Доп. информация';
            content = 'Доп. информация';
            break;
        case 'rooms':
            title = 'Комнаты бункера';
            content = 'Комнаты бункера';
            break;
        case 'items':
            title = 'Предметы в бункере';
            content = 'Предметы в бункере';
            break;
        default:
            title = 'Выберите характеристику для генерации...';
            content = '';
    }

    return { title, content };
}