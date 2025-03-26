const ResultDisplay = ({ predictedPrice }) => {
    return (
      <div>
        {predictedPrice !== null && (
          <h2>Predicted Price: ${predictedPrice.toLocaleString()}</h2>
        )}
      </div>
    );
  };
  
  export default ResultDisplay;
  