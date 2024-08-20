import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import axios from 'axios';
import { confirmAlert } from 'react-confirm-alert';
import { useSelector } from 'react-redux';
import 'react-confirm-alert/src/react-confirm-alert.css';
import ForecastChart from '../ForecastFrame'; // ForecastChart bileşenini içe aktar

// Yup schema
const schema = yup.object().shape({
  yeniIsim: yup.string().required('Yeni isim gereklidir'),
  yeniAdet: yup.number()
    .required('Yeni adet gereklidir')
    .positive('Adet pozitif bir sayı olmalıdır')
    .integer('Adet tam sayı olmalıdır'),
  yeniMevsim: yup.string().required('Mevsim seçilmelidir'),
  secilenUrun: yup.string().nullable()
});

function Actions({ value, item, refreshData, datas }) {
  const userID = useSelector((state) => state.user.userID);
  const [forecastData, setForecastData] = useState(null);
  const [recommendations, setRecommendations] = useState(null);
  const [selectedProductID, setSelectedProductID] = useState('');

  const {
    control,
    handleSubmit,
    reset,
    watch,
    formState: { errors },
    getValues
  } = useForm({
    resolver: yupResolver(schema),
    defaultValues: {
      yeniIsim: item ? item.ProductName : '',
      yeniAdet: item ? item.InventoryLevel : '',
      yeniMevsim: item ? item.Season : 'Yaz',
      secilenUrun: item ? item.ProductID : ''
    }
  });

  useEffect(() => {
    if (item) {
      reset({
        yeniIsim: item.ProductName,
        yeniAdet: item.InventoryLevel,
        yeniMevsim: item.Season,
        secilenUrun: item.ProductID
      });
    }
  }, [item, reset]);

  const onSubmit = async (data) => {
    try {
      if (value === 0) {
        // Güncelleme işlemi
        try {
          await axios.put('http://localhost:5001/api/update', {
            ProductID: data.secilenUrun,
            ProductName: data.yeniIsim,
            InventoryLevel: data.yeniAdet,
            Season: data.yeniMevsim,
            UserID: userID,
          });
          refreshData();
          console.log('Güncelleme başarılı, ProductID: ' + data.secilenUrun + " Yeni Adet: " + data.yeniAdet);
        } catch (updateError) {
          console.error('Güncelleme işlemi sırasında bir hata oluştu:', updateError);
          alert("Güncelleme işlemi sırasında bir hata oluştu")
          // Hata mesajını kullanıcıya göstermek için gerekli işlemleri yapabilirsiniz
        }
      } else if (value === 1) {
        // Ekleme işlemi
        try {
          const addResponse = await axios.post('http://localhost:5001/api/add', {
            UserID: userID,
            ProductID: null, // Yeni bir ürün eklediğimiz için ProductID'yi null gönderiyoruz
            Date: new Date().toISOString().slice(0, 10),
            ProductName: data.yeniIsim,
            InventoryLevel: data.yeniAdet,
            Season: data.yeniMevsim,
          });
          const productID = addResponse.data.ProductID;
          setSelectedProductID(productID); // ProductID'yi state'e kaydet
          refreshData();
          console.log('Ekleme başarılı');
        } catch (addError) {
          console.error('Ekleme işlemi sırasında bir hata oluştu:', addError);
          alert("Ekleme işlemi sırasında bir hata oluştu")
          // Hata mesajını kullanıcıya göstermek için gerekli işlemleri yapabilirsiniz
        }
      } else if (value === 2) {
        // Silme işlemi
        confirmAlert({
          title: 'Silme Onayı',
          message: 'Bu ürünü silmek istediğinizden emin misiniz?',
          buttons: [
            {
              label: 'Evet',
              onClick: async () => {
                try {
                  await axios.post('http://localhost:5001/api/delete', {
                    ProductID: item.ProductID,
                    UserID: userID,
                    Date: item.Date
                  });
                  console.log('Silme başarılı');
                  refreshData();
                } catch (error) {
                  console.error('Silme başarısız:', error);
                }
              }
            },
            {
              label: 'Hayır',
              onClick: () => console.log('Silme iptal edildi')
            }
          ]
        });
      }
    } catch (error) {
      console.error('İşlem başarısız:', error);
    }
  };
  
  const handleYZKullan = async (productID) => {
    try {
      // Öneri verilerini al
      const yzResponse = await axios.get('http://localhost:5002/api/recommendations', {
        params: {
          season: getValues().yeniMevsim,
          productID: productID,
          userID
          
        }
      });

      setRecommendations(yzResponse.data); // Önerileri state'e kaydet
      console.log('Öneriler başarılı:', yzResponse.data);

      // Forecast veri çağrısını yap
      const forecastResponse = await axios.post('http://localhost:5002/api/forecast', {
        ProductID: productID,
        UserID: userID
      });

      if (forecastResponse.data.length < 2) {
        // Veri yetersizliği durumunda uyarı
        console.error("Yetersiz Veri Girişi! En Az 2 Adet Veri Gerekli.");
        alert("Yetersiz Veri Girişi! En Az 2 Adet Veri Gerekli.");
        return;
      }

      setForecastData(forecastResponse.data); // Tahmin verilerini state'e kaydet
      console.log("Tahmin verileri", forecastResponse.data);
    } catch (error) {
      console.error('YZ Kullanımında hata:', error);
      alert("Yetersiz Veri Girişi! En Az 2 Adet Veri Gerekli.");
    }
  };

  return (
    <div className='h-full flex items-center justify-center'>
      <div className="overflow-auto max-w-full max-h-screen mx-auto w-full h-full flex flex-col justify-center items-center gap-10">
        <div className="w-full max-w-lg mx-auto flex flex-col gap-2 justify-center">
          {value === 2 && (
            <input
              className='cursor-not-allowed w-full bg-white/30 h-full rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
              type="search"
              placeholder='Bir şeyler yaz...'
              disabled={true}
              value={item ? item.ProductID : ''}
            />
          )}
          {value !== 2 && (
            <>
              <Controller
                name="yeniIsim"
                control={control}
                render={({ field }) => (
                  <input
                    className='w-full bg-white/30 h-full rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
                    type="text"
                    id='yeniIsim'
                    placeholder='Yeni İsim'
                    {...field}
                  />
                )}
              />
              {errors.yeniIsim && <p className='text-red-500'>{errors.yeniIsim.message}</p>}

              <Controller
                name="yeniAdet"
                control={control}
                render={({ field }) => (
                  <input
                    className='w-full bg-white/30 h-full rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
                    type="number"
                    placeholder='Yeni Adet'
                    {...field}
                  />
                )}
              />
              {errors.yeniAdet && <p className='text-red-500'>{errors.yeniAdet.message}</p>}

              <Controller
                name="yeniMevsim"
                control={control}
                render={({ field }) => (
                  <select
                    className='cursor-pointer w-full bg-white/30 h-full rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
                    {...field}
                  >
                    <option value="İlkbahar">İlkbahar</option>
                    <option value="Yaz">Yaz</option>
                    <option value="Sonbahar">Sonbahar</option>
                    <option value="Kış">Kış</option>
                  </select>
                )}
              />
              {errors.yeniMevsim && <p className='text-red-500'>{errors.yeniMevsim.message}</p>}
            </>
          )}

          {errors.secilenUrun && <p className='text-red-500'>{errors.secilenUrun.message}</p>}
          <div className="flex flex-row gap-5">
            <button
            id='crud'
              className='px-6 py-4 bg-green-700 hover:bg-green-800 text-white font-bold rounded-lg shadow-white shadow-2xl border'
              type="button"
              onClick={handleSubmit(onSubmit)}
            >
              {value === 0 ? "Güncelle" : value === 1 ? "Ekle" : "Sil"}
            </button>
            {value === 1 && (
              <button
              id='yz'
                className='px-6 py-4 bg-blue-700 hover:bg-blue-800 text-white font-bold rounded-lg shadow-white shadow-2xl border'
                type="button"
                onClick={() => {
                  const productId = datas.find(item => item.ProductName === getValues().yeniIsim)?.ProductID;
                  handleYZKullan(productId); // Yapay zeka çağrısını tetikle
                }}
              >
                YZ Kullan
              </button>
            )}
          </div>
        </div>

        {forecastData && <ForecastChart forecastData={forecastData} />}
        {recommendations && (
          <div className="recommendations">
            <h2>Önerilen Ürünler</h2>
            <select
              className='w-full bg-white/30 h-full rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
              onChange={(e) => setSelectedProductID(e.target.value)}
              value={selectedProductID}
            >
              <option value="">Seçiniz</option>
              {recommendations.map((rec, index) => (
                <option key={index} value={rec.ProductID}>
                  {datas.find(item => item.ProductID === rec.ProductID)?.ProductName}
                </option>
              ))}
            </select>
          </div>
        )}
      </div>
    </div>
  );
}

export default Actions;
