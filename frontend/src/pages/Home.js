import { useState } from "react";
import PredictionForm from "../components/Form";
import ResultDisplay from "../components/Display";

const HomePage = () => {
  const API_URL = process.env.REACT_APP_API_URL;

  const [predictedPrice, setPredictedPrice] = useState(null);
  console.log(API_URL);
  const fetchPrediction = async (sqft, bedrooms) => {
    const response = await fetch(`${API_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sqft, bedrooms }),
    });

    const data = await response.json();
    setPredictedPrice(data.predicted_price);
  };

  return (
    <div>
      <h1>House Price Predictor</h1>
      <PredictionForm onPredict={fetchPrediction} />
      <ResultDisplay predictedPrice={predictedPrice} />
    </div>
  );
};

export default HomePage;
