import { useState } from 'react';
import './App.css';
import Result_page from './Search';
function Poogle() {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setsearchResults] = useState([]);
  

  const handleSearch = async() => {
    // Check if the search query is not empty
    if (searchQuery.trim() !== '') {
      // Construct the URL
      const apiUrl = `http://localhost:6969/api/search?q=${searchQuery.trim()}`;

      // Perform the fetch request
      await fetch(apiUrl)
        .then(response => response.json()) // Parse response data as JSON
        .then(setsearchResults)
        .catch(error => {
          console.error('Fetch Error:', error);
        });
    }
  };

  const handleInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <>
      <div className='wrapper'>
        <h1 className='title'>Poogle</h1>
        <div className='input-container'>
          <input
            className='input-box'
            value={searchQuery}
            onChange={handleInputChange}
          />
          <button className='search-button' onClick={handleSearch}>
            <img
              src='./search.webp'
              alt='Search'
              className='search-icon'
            />
          </button>
        </div>
      </div>
      <Result_page data= {searchResults}/>
    </>
  );
}

export default Poogle;
