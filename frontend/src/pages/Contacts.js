import React from 'react';

function Contacts() {
  return (
    <>
      <h1 class="main-title">Контакты</h1>
      <div class="main-contacts-block">
        <p class="main-contact">По всем вопросам общаться на почту - <a href="mailto:katsuyoriiii@gmail.com"
          class="main-contact-link">katsuyoriiii@gmail.com</a></p>
        <p class="main-contact">Телеграмм бот проекта - <a href="https://t.me/bunker_katsu_bot"
          class="main-contact-link">@bunker_katsu_bot</a></p>
        <p class="main-contact">Открытый код проекта на github - <a
          href="https://github.com/katsuyorii/BunkerGameRESTful"
          class="main-contact-link">BunkerGameRESTful</a></p>
        <p class="main-contact">Иконки на сайте - <a href="https://icons8.ru/"
          class="main-contact-link">Icons8</a></p>
      </div>
    </>
  )
}

export default Contacts;