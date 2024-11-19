import axios from 'axios';

export async function generateContent(category) {
    let content;

    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/${category}/`);
        const data = response.data;

        switch (category) {
            case 'bunker':
                content = (
                    <>
                        <p>📛 Наименование бункера: {data.title}</p>
                        <p>📜 Описание бункера: {data.description}</p>
                        <p>📦 Предметы в бункере:</p>
                        {data.items.map((item, index) => (
                            <li class="item-li" key={index}> - {item.name}</li>
                        ))}
                        <p>🏠 Комнаты в бункере:</p> 
                        {data.rooms.map((room, index) => (
                            <li class="item-li" key={index}> - {room.name}</li>
                        ))}
                        <p>📐 Площадь бункера: {data.area} кв.м.</p>
                        <p>🥕 Количество еды в бункере: {data.sup_food_month} мес.</p>
                    </>
                )
                break;
            case 'catastrophe':
                content = (
                    <>
                        <p>💥 Наименование катастрофы: {data.title}</p>
                        <p>📜 Описание катастрофы: {data.description}</p>
                        <p>🚧 Процент разрушения на поверхности: {data.perc_destruction}%</p>
                        <p>☠️ Процент выживших людей на поверхности: {data.perc_survivors}%</p>
                    </>
                )
                break;
            case 'character':
                content = (
                    <>
                        <p >👨 Пол, возраст: {data.gender}, {data.age}, {data.fertility}</p >
                        <p>💼 Профессия, стаж (лет.): {data.profession.name}, {data.profession.exp}</p>
                        <p>🏥 Состояние здоровья: {data.health.name}</p>
                        <p>🎨 Хобби: {data.hobby.name}</p>
                        <p>👻 Фобия: аквафобия - {data.phobia.name}</p>
                        <p>🗿 Человеческая черта: {data.trait.name}</p>
                        <p>💪 Телосложение: {data.physique.name}</p>
                        <p>🎒 Багаж: {data.baggage.name}</p>
                        <p>📜 Доп. информация: {data.additional_info.description}</p>
                        <p>✨ Спец. действие №1: {data.special_action_one.description}</p>
                        <p>✨ Спец. действие №2: {data.special_action_two.description}</p>
                    </>
                );
                break;
            case 'gender':
                content = (
                    <p>👨 Пол, возраст: {data.gender}, {data.age}, {data.fertility}</p>
                );
                break;
            case 'health':
                content = (
                    <p>🏥 Состояние здоровья: {data.name}</p>
                );
                break;
            case 'profession':
                content = (
                    <p>💼 Профессия: {data.name}, {data.exp}</p>
                );
                break;
            case 'hobby':
                content = (
                    <p>🎨 Хобби: {data.name}</p>
                );
                break;
            case 'phobia':
                content = (
                    <p>👻 Фобия: {data.name}</p>
                );
                break;
            case 'trait':
                content = (
                    <p>🗿 Человеческая черта: {data.name}</p>
                );
                break;
            case 'physique':
                content = (
                    <p>💪 Телосложение: {data.name}</p>
                );
                break;
            case 'baggage':
                content = (
                    <p>🎒 Багаж: {data.name}</p>
                );
                break;
            case 'info':
                content = (
                    <p>📜 Доп. информация: {data.description}</p>
                );
                break;
            case 'rooms':
                content = (
                    <>
                    <p>🏠 Комнаты в бункере:</p> 
                    {data.map((room, index) => (
                        <li class="item-li" key={index}> - {room.name}</li>
                    ))}
                    </>
                );
                break;
            case 'items':
                content = (
                    <>
                    <p>📦 Предметы в бункере:</p> 
                    {data.map((item, index) => (
                        <li class="item-li" key={index}> - {item.name}</li>
                    ))}
                    </>
                );
                break;
            default:
                content = '';
        }

    } catch (error) {
        console.error(`Ошибка при генерации, повторите снова!:`, error);
    }

    return content;
};