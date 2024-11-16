import axios from 'axios';

export async function generateContent(category) {
        let content;

        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/${category}/`);
            const data = response.data;

            switch (category) {
                case 'bunker':
                    content = data;
                    break;
                case 'catastrophe':
                    content = data;
                    break;
                case 'character':
                    content = data;
                    break;
                case 'gender':
                    content = (
                        <p>Пол, возраст: {data.gender}, {data.age}, {data.fertility}</p>
                    );
                    break;
                case 'health':
                    content = data;
                    break;
                case 'profession':
                    content = data;
                    break;
                case 'hobby':
                    content = data;
                    break;
                case 'phobia':
                    content = data;
                    break;
                case 'trait':
                    content = data;
                    break;
                case 'physique':
                    content = data;
                    break;
                case 'baggage':
                    content = data;
                    break;
                case 'addinfo':
                    content = data;
                    break;
                case 'rooms':
                    content = data;
                    break;
                case 'items':
                    content = data;
                    break;
                default:
                    content = '';
            }

        } catch (error) {
            console.error(`Ошибка при генерации, повторите снова!:`, error);
        }

    return content;
};