import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <>
      <h1 class="main-title">Генератор характеристик</h1>
      <div class="main-flex">
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/bunker.png" alt="Bunker"/>
          </div>
          <p class="main-flex-item-title">Бункер</p>
          <Link to="/generator/bunker" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/catastrophe.png" alt="Catastrophe"/>
          </div>
          <p class="main-flex-item-title">Катастрофа</p>
          <Link to="/generator/catastrophe" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/character.png" alt="Character"/>
          </div>
          <p class="main-flex-item-title">Персонаж</p>
          <Link to="/generator/character" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/gender.png" alt="Gender"/>
          </div>
          <p class="main-flex-item-title">Пол, возраст</p>
          <Link to="/generator/gender" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/profession.png" alt="Profession"/>
          </div>
          <p class="main-flex-item-title">Профессия</p>
          <Link to="/generator/profession" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/health.png" alt="Health"/>
          </div>
          <p class="main-flex-item-title">Здоровье</p>
          <Link to="/generator/health" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/physique.png" alt="Physique"/>
          </div>
          <p class="main-flex-item-title">Телосложение</p>
          <Link to="/generator/physique" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/trait.png" alt="Trait"/>
          </div>
          <p class="main-flex-item-title">Чел. черта</p>
          <Link to="/generator/trait" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/hobby.png" alt="Hobby"/>
          </div>
          <p class="main-flex-item-title">Хобби</p>
          <Link to="/generator/hobby" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/phobia.png" alt="Phobia"/>
          </div>
          <p class="main-flex-item-title">Фобия</p>
          <Link to="/generator/phobia" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/baggage.png" alt="Baggage"/>
          </div>
          <p class="main-flex-item-title">Багаж</p>
          <Link to="/generator/baggage" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/info.png" alt="AddInfo"/>
          </div>
          <p class="main-flex-item-title">Доп. инфо</p>
          <Link to="/generator/addinfo" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/rooms.png" alt="Rooms"/>
          </div>
          <p class="main-flex-item-title">Комнаты</p>
          <Link to="/generator/rooms" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
        <div class="main-flex-item">
          <div class="main-flex-item-block">
            <img class="main-flex-item-img" src="/images/icons/items.png" alt="Items"/>
          </div>
          <p class="main-flex-item-title">Предметы</p>
          <Link to="/generator/items" class="main-flex-item-btn">Сгенерировать</Link>
        </div>
      </div>
    </>
  )
}

export default Home;