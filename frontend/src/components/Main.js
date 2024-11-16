import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Generator from '../pages/Generator';
import Rules from '../pages/Rules';
import Contacts from '../pages/Contacts';

function Main() {
  return (
    <main class="main">
        <div class="wrapper">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/generator" element={<Generator />} />
            <Route path="/rules" element={<Rules />} />
            <Route path="/contacts" element={<Contacts />} />
          </Routes>
        </div>
    </main>
  );
}

export default Main;