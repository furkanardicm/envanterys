import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, PointElement, LineElement, CategoryScale, LinearScale, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(LineElement, PointElement, CategoryScale, LinearScale, Title, Tooltip, Legend);

// Tarih formatlama fonksiyonu
const formatDate = (dateStr) => {
  const options = { day: '2-digit', month: 'short', year: 'numeric' };
  return new Date(dateStr).toLocaleDateString('en-GB', options);
};

function ForecastChart({ forecastData }) {
  // Tarihleri formatlayarak data yapılandırması
  const data = {
    labels: forecastData.map(item => formatDate(item.ds)),
    datasets: [
      {
        label: 'Tahmin Edilen Envanter Seviyeleri',
        data: forecastData.map(item => item.yhat),
        fill: false,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.1,
      },
    ],
  };

  // Grafik seçenekleri
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      tooltip: {
        callbacks: {
          label: function(tooltipItem) {
            return `Tahmin: ${tooltipItem.raw}`;
          },
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Tarih',
        },
        ticks: {
          autoSkip: true,
          maxTicksLimit: 10,
        },
      },
      y: {
        title: {
          display: true,
          text: 'Envanter Seviyesi',
        },
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="w-full h-64">
      <Line data={data} options={options} />
    </div>
  );
}

export default ForecastChart;
