import React, { useState, useEffect, useCallback } from 'react';
import { Link, useParams } from 'react-router-dom';
import { generateData } from '../services/generateData';
import { generateContent } from '../services/generateContent';

function Generator() {
  const { category } = useParams();
  const { title } = generateData(category);
  const [content, setContent] = useState(null);

  const fetchData = useCallback(async () => {
    const result = await generateContent(category);
    setContent(result);
  }, [category]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return (
    <>
      <h1 class="main-title">{title}</h1>
      <div class="main-block">
        { content }
      </div>
      <div class="main-row">
        <Link onClick={fetchData} class="main-row-btn">Сгенерировать</Link>
      </div>
    </>
  )
}

export default Generator;