import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, LineElement, Title, Tooltip, Legend);

function ForecastChart() {
  const [forecastData, setForecastData] = useState([]);

  useEffect(() => {
    const fetchForecast = async () => {
      try {
        const response = await axios.get('http://localhost:5001/api/forecast');
        setForecastData(response.data);
      } catch (error) {
        console.error('Tahmin verisi alınamadı:', error);
      }
    };

    fetchForecast();
  }, []);

  const data = {
    labels: forecastData.map(item => item.ds),
    datasets: [
      {
        label: 'Tahmin Edilen Envanter Seviyeleri',
        data: forecastData.map(item => item.yhat),
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
      },
    ],
  };

  return (
    <div>
      <h2>30 Günlük Envanter Tahmini</h2>
      <Line data={data} />
    </div>
  );
}

export default ForecastChart;
