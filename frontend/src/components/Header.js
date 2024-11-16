import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header class="header">
            <div class="wrapper">
                <div class="header-flex">
                    <div class="header-flex-nav">
                        <Link to="/"><img class="header-flex-nav-logo" src="/images/logo.png" alt="Logo"/></Link>
                        <div class="header-flex-nav-block">
                            <ul class="header-flex-nav-block-list">
                                <li><Link to="/" class="header-flex-nav-block-list-item">Генератор</Link></li>
                                <li><Link to="/rules" class="header-flex-nav-block-list-item">Правила игры</Link></li>
                                <li><Link to="/contacts" class="header-flex-nav-block-list-item">Контакты</Link></li>
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