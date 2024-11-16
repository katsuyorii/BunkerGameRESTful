import React from 'react';

function Header() {
  return (
    <header class="header">
            <div class="wrapper">
                <div class="header-flex">
                    <div class="header-flex-nav">
                        <a href="/#"><img class="header-flex-nav-logo" src="/images/logo.png" alt="Logo"/></a>
                        <div class="header-flex-nav-block">
                            <ul class="header-flex-nav-block-list">
                                <li><a href="/#" class="header-flex-nav-block-list-item">Генератор</a></li>
                                <li><a href="/#" class="header-flex-nav-block-list-item">Правила игры</a></li>
                                <li><a href="/#" class="header-flex-nav-block-list-item">Контакты</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="header-flex-login">
                        <div class="header-flex-login-block">
                            <ul class="header-flex-login-block-list">
                                <li><a href="/#" class="header-flex-login-block-list-link">Вход</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </header>
  );
}

export default Header;