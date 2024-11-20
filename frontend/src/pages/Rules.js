import React from 'react';

function Rules() {
  return (
    <>
      <h1 class="main-title">Правила игры</h1 >
      <div class="main-rules-block">
        <div class="main-rules-block-item">
          <h2 class="main-rules-block-item-title">🎲 Цель игры</h2>
          <p class="main-rules-block-item-text">Ваша команда – группа выживших, и вы все хотите попасть в
            бункер, чтобы спастись от
            надвигающейся катастрофы. Но места в бункере ограничены, и вам придется решать, кто достоин
            остаться! В процессе игроки обсуждают, спорят и голосуют, выбирая самых полезных и нужных
            для выживания. По стандартным правилам игры, в бункере должны остаться как минимум 1 мужчина
            и 1 женщина для будущего продолжения рода!</p>
        </div>
        <div class="main-rules-block-item">
          <h2 class="main-rules-block-item-title">🔧 Подготовка к игре</h2>
          <p class="main-rules-block-item-text">1. Каждый игрок генерирует персонажа со случайными
            характеристиками.</p>
          <p class="main-rules-block-item-text">2. Генерируется случайная катастрофа.</p>
          <p class="main-rules-block-item-text">3. Генерируется случайный бункер.</p>
        </div>
        <div class="main-rules-block-item">
          <h2 class="main-rules-block-item-title">👥 Процесс игры</h2>
          <p class="main-rules-block-item-text">1. Каждый игрок по очереди вскрывают по 2 характетистики,
            одну обязательную - пол и возраст, а вторую на выбор.</p>
          <p class="main-rules-block-item-text">2. Обсуждаются плюсы и минусы каждого участника,
            основываясь на его навыках и характеристиках.</p>
          <p class="main-rules-block-item-text">3. В каждом раунде проводится голосование, чтобы исключить
            одного игрока. Тот, кто набрал больше голосов, покидает игру и не попадает в бункер.</p>
          <p class="main-rules-block-item-text">4. Также имеется возможность пропустить 1 круг голосования
            и перейти к следующему кругу, однако в таком случае придется исключить сразу 2 игроков!</p>
        </div>
        <div class="main-rules-block-item">
          <h2 class="main-rules-block-item-title">⏳ Окончание игры</h2>
          <p class="main-rules-block-item-text">Когда количество выживших совпадает с количеством мест в
            бункере, а также выполнено условие по продолжению рода (1 мужчина и 1 женщина), игра заканчивается. Остальные игроки считаются выбывшими, а оставшиеся —
            победителями! 🏆</p>
        </div>
      </div>
    </>
  )
}

export default Rules;