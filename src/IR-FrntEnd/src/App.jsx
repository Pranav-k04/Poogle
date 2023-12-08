import { useState } from 'react';
import './App.css';

function App() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = () => {
    // Perform the action here with the searchQuery state
    console.log('Searching for:', searchQuery);
    // You can add logic here to perform the search functionality using searchQuery
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
    </>
  );
}

export default App;
