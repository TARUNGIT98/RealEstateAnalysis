import React, { useState, useEffect } from 'react';
import './App.css';

const HomePriceEstimator = () => {
  const [sqft, setSqft] = useState(1000);
  const [bhk, setBhk] = useState(2);
  const [bathrooms, setBathrooms] = useState(2);
  const [location, setLocation] = useState('');
  const [locations, setLocations] = useState([]);
  const [estimatedPrice, setEstimatedPrice] = useState(null);

  const API_BASE_URL = "https://realestateanalysis.onrender.com/api"; // Backend Render URL

  useEffect(() => {
    fetch(`${API_BASE_URL}/get_location_names`)
      .then(response => response.json())
      .then(data => {
        if (data.locations) {
          setLocations(data.locations);
        }
      })
      .catch(error => console.error('Error fetching locations:', error));
  }, []);

  const estimatePrice = async () => {
    if (!location) {
      alert('Please select a location.');
      return;
    }

    const response = await fetch(`${API_BASE_URL}/predict_home_price`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        total_sqft: parseFloat(sqft),
        bhk,
        bath: bathrooms,
        location
      })
    });

    const data = await response.json();
    setEstimatedPrice(data.estimated_price);
  };

  return (
    <div className="container">
      <div className="form">
        <h2>Area (Square Feet)</h2>
        <input
          className="area-input"
          type="number"
          value={sqft}
          onChange={(e) => setSqft(e.target.value)}
        />

        <h2>BHK</h2>
        <div className="switch-field">
          {[1, 2, 3, 4, 5].map(value => (
            <React.Fragment key={value}>
              <input
                type="radio"
                id={`bhk-${value}`}
                name="bhk"
                value={value}
                checked={bhk === value}
                onChange={() => setBhk(value)}
              />
              <label htmlFor={`bhk-${value}`}>{value}</label>
            </React.Fragment>
          ))}
        </div>

        <h2>Bath</h2>
        <div className="switch-field">
          {[1, 2, 3, 4, 5].map(value => (
            <React.Fragment key={value}>
              <input
                type="radio"
                id={`bath-${value}`}
                name="bath"
                value={value}
                checked={bathrooms === value}
                onChange={() => setBathrooms(value)}
              />
              <label htmlFor={`bath-${value}`}>{value}</label>
            </React.Fragment>
          ))}
        </div>

        <h2>Location</h2>
        <select
          className="select-field"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        >
          <option value="" disabled>Choose a Location</option>
          {locations.map(loc => (
            <option key={loc} value={loc}>{loc}</option>
          ))}
        </select>

        <button type="button" className="submit-button" onClick={estimatePrice}>
              Estimate Price
        </button>



        {estimatedPrice && (
          <div className="result">
            <h2>Estimated Price: ₹{estimatedPrice} Lakh</h2>
          </div>
        )}
      </div>
    </div>
  );
};

export default HomePriceEstimator;
