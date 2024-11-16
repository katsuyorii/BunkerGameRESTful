import React from 'react';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { generateData } from '../services/generateData';

function Generator() {
  const { category } = useParams();
  const { title, content } = generateData(category);

  return (
    <>
      <h1 class="main-title">{ title }</h1>
      <div class="main-block">
        { content }
      </div>
      <div class="main-row">
        <Link to={`/generator/${category}`} class="main-row-btn">Сгенерировать</Link>
      </div>
    </>
  )
}

export default Generator;