import React, { useState, useEffect } from 'react';

const ResultPage = ({ data }) => {
  const itemsPerPage = 10;
  const [currentPage, setCurrentPage] = useState(1);

  const titles = data ? data.map(item => item.title) : [];
  const urls = data ? data.map(item => item.url) : [];
  
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentTitles = titles.slice(indexOfFirstItem, indexOfLastItem);
  const currentUrls = urls.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil(titles.length / itemsPerPage);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <div className='search-results' style={{ justifyContent: 'center', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ fontSize: '28px', fontWeight: 'normal', color: '#1a0dab', marginBottom: '20px' }}>Search Results</h1>
      {currentTitles.length > 0 && currentUrls.length > 0 ? (
        <div>
          {currentTitles.map((title, index) => (
            <div key={index} style={{ marginBottom: '20px' }}>
              <h3 style={{ fontSize: '18px', fontWeight: 'normal', marginBottom: '5px' }}>{title}</h3>
              <a href={currentUrls[index]} target='_blank' rel='noopener noreferrer' style={{ fontSize: '14px', color: '#1a0dab', textDecoration: 'none' }}>
                {currentUrls[index]}
              </a>
            </div>
          ))}
          <div className='pagination' style={{ marginTop: '20px' }}>
            {Array.from({ length: totalPages }, (_, i) => (
              <button key={i + 1} onClick={() => handlePageChange(i + 1)} style={{ padding: '8px 12px', marginRight: '5px', fontSize: '14px', fontWeight: 'normal', color: '#1a0dab', backgroundColor: '#f8f9fa', border: '1px solid #dadce0', borderRadius: '4px', cursor: 'pointer' }}>
                {i + 1}
              </button>
            ))}
          </div>
        </div>
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
};

export default ResultPage;
