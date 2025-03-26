import { useState } from "react";

const PredictionForm = ({ onPredict }) => {
  const [sqft, setSqft] = useState("");
  const [bedrooms, setBedrooms] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    onPredict(Number(sqft), Number(bedrooms));
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Square Footage:</label>
      <input type="number" value={sqft} onChange={(e) => setSqft(e.target.value)} required />

      <label>Number of Bedrooms:</label>
      <input type="number" value={bedrooms} onChange={(e) => setBedrooms(e.target.value)} required />

      <button type="submit">Predict Price</button>
    </form>
  );
};

export default PredictionForm;
