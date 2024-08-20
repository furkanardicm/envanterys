import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXmark, faSortDown, faTrash, faSquarePlus, faPen, faArrowDownAZ, faArrowDown19, faSnowflake, faRotateRight } from '@fortawesome/free-solid-svg-icons';
import Actions from '../../components/Actions';
import axios from 'axios';
import NotificationBar from '../../components/NotificationBar';
import { useSelector } from 'react-redux'; // Import useSelector

function Index() {
  const [value, setValue] = useState(-1);
  const [isOpen, setOpen] = useState(false);
  const [isOpen2, setOpen2] = useState(false);
  const [items, setItems] = useState([]);
  const [filteredItems, setFilteredItems] = useState([]);
  const [sortCriterion, setSortCriterion] = useState(null);
  const [seasonFilter, setSeasonFilter] = useState([]);
  const [quantityRange, setQuantityRange] = useState({ min: 0, max: 5000 });
  const [selectedItem, setSelectedItem] = useState(null);
  const [myAlert, setMyAlert] = useState(false);
  const [showNotification, setShowNotification] = useState(false);

  // Get user ID from Redux store
  const userID = useSelector(state => state.user.userID);

  const handleShowNotification = () => {
    setShowNotification(true);
  };

  const handleCloseNotification = () => {
    setShowNotification(false);
  };
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch data based on user ID
        const response = await axios.get(`http://localhost:5001/api/select/${userID}`);
        if (response.data.status === 'success') {
          console.log(response.data)
          setItems(response.data.data);
          setMyAlert(false);
        } else {
          console.error(response.data.message);
        }

      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    if (userID) {
      fetchData();
    }
  }, [userID, myAlert]);

  useEffect(() => {
    const applyFiltersAndSort = () => {
      let updatedItems = applyFilters(items);

      if (sortCriterion) {
        updatedItems = [...updatedItems].sort((a, b) => {
          switch (sortCriterion) {
            case 'quantity':
              return b.InventoryLevel - a.InventoryLevel; // Descending order
            case 'alphabetical':
              return a.ProductName.localeCompare(b.ProductName); // Alphabetical order
            case 'season':
              const seasons = ['İlkbahar', 'Yaz', 'Sonbahar', 'Kış'];
              return seasons.indexOf(a.Season) - seasons.indexOf(b.Season); // Season order
            default:
              return 0;
          }
        });
      }

      setFilteredItems(updatedItems);
    };

    applyFiltersAndSort();
  }, [items, seasonFilter, quantityRange, sortCriterion]);

  const applyFilters = (items) => {
    let filteredItems = [...items];

    if (seasonFilter.length > 0) {
      filteredItems = filteredItems.filter(item => seasonFilter.includes(item.Season));
    }

    filteredItems = filteredItems.filter(item => item.InventoryLevel >= quantityRange.min && item.InventoryLevel <= quantityRange.max);

    return filteredItems;
  };

  const handleClick = (x, item) => {
    setValue(x);
    setSelectedItem(item);
  };

  const handleSort = (criterion) => {
    setSortCriterion(criterion);
    setOpen(false);
  };

  const handleSeasonFilterChange = (season) => {
    setSeasonFilter(prevState =>
      prevState.includes(season) ? prevState.filter(s => s !== season) : [...prevState, season]
    );
  };

  const handleQuantityRangeChange = (min, max) => {
    setQuantityRange({ min, max });
  };

  const handleResetSort = () => {
    setSortCriterion(null);
    setOpen(false);
  };

  const handleResetFilters = () => {
    setSeasonFilter([]);
    setQuantityRange({ min: 0, max: 5000 });
    setOpen2(false);
  };

  const getSortClass = (criterion) => {
    return sortCriterion === criterion ? 'bg-black text-white' : 'hover:bg-gray-200';
  };

  const refreshData = () => {
    setValue(-1);
    setMyAlert(true);
    handleShowNotification();
  };
  return (
    <>
      {showNotification && (
        <div className="fixed w-full top-2 mx-auto flex flex-row items-center justify-center">
          <NotificationBar
            message="İşlem Başarılı ! Envanter Güncellendi..."
            duration={5000}
            isVisible={showNotification}
            onClose={handleCloseNotification}
          />
        </div>
      )}

      <div className='relative mx-auto w-[80%] h-[80%] bg-white/30 shadow-inner shadow-black/30 p-4 stroke-black/30 border rounded flex flex-col items-center justify-center'>
        <div className="absolute top-0 left-0 px-4 py-2"><span className='font-extrabold'>{filteredItems.length}</span> Ürün Getirildi.</div>
        
        <div className="flex flex-row gap-4 flex-wrap items-center justify-center">
          <button onClick={() => handleClick(1, null)} className="mt-4 w-52 h-11 bg-green-700 hover:bg-green-800 text-white transition-all font-semibold rounded">Ürün Ekle <FontAwesomeIcon className='ml-2' icon={faSquarePlus} /></button>
          <div onClick={() => { setOpen(!isOpen); setOpen2(false); }} className="relative cursor-pointer flex items-center justify-center mt-4 gap-4 font-bold h-11 text-white px-6 bg-black rounded">Sırala <FontAwesomeIcon className={`transition-all delay-300 ease-in-out ${isOpen ? 'mt-1 rotate-180' : 'mb-2'}`} icon={faSortDown} />
            {isOpen && (
              <ul className="z-20 absolute top-14 mt-2 w-56 bg-white text-black rounded shadow-2xl shadow-black -right-15 border border-gray-100">
                <li onClick={() => handleSort('quantity')} className={`px-4 py-2 ${getSortClass('quantity')} font-medium cursor-pointer`}>Adede Göre <FontAwesomeIcon className='float-right' icon={faArrowDown19} /></li>
                <li onClick={() => handleSort('alphabetical')} className={`px-4 py-2 ${getSortClass('alphabetical')} font-medium cursor-pointer`}>Alfabetik <FontAwesomeIcon className='float-right' icon={faArrowDownAZ} /></li>
                <li onClick={() => handleSort('season')} className={`px-4 py-2 ${getSortClass('season')} font-medium cursor-pointer`}>Mevsime Göre <FontAwesomeIcon className='float-right' icon={faSnowflake} /></li>
                <li onClick={handleResetSort} className="px-4 py-2 hover:bg-gray-200 flex items-center justify-between font-medium cursor-pointer">Sıfırla <FontAwesomeIcon className='float-right' icon={faRotateRight} /></li>
              </ul>
            )}
          </div>
          <div className="relative">
            <div onClick={() => { setOpen2(!isOpen2); setOpen(false); }} className="relative cursor-pointer flex items-center justify-center mt-4 gap-4 font-bold h-11 text-white px-6 bg-black rounded">Filtrele <FontAwesomeIcon className={`transition-all delay-300 ease-in-out ${isOpen2 ? 'mt-1 rotate-180' : 'mb-2'}`} icon={faSortDown} /></div>
            {isOpen2 && (
              <ul className="z-20 absolute top-20 w-56 bg-white text-black rounded shadow-2xl shadow-black -right-12 border border-gray-100">
                <li className="px-4 py-2 hover:bg-gray-200 font-medium cursor-pointer">
                  Adede Göre
                  <div className="flex flex-col">
                    <input
                      type="number"
                      value={quantityRange.min}
                      onChange={(e) => handleQuantityRangeChange(Number(e.target.value), quantityRange.max)}
                      placeholder="Min"
                      className="mt-2 p-1 border rounded"
                    />
                    <input
                      type="number"
                      value={quantityRange.max}
                      onChange={(e) => handleQuantityRangeChange(quantityRange.min, Number(e.target.value))}
                      placeholder="Max"
                      className="mt-2 p-1 border rounded"
                    />
                  </div>
                </li>
                <li className="px-4 py-2 hover:bg-gray-200 font-medium cursor-pointer">
                  Mevsime Göre
                  <div className="flex flex-col">
                    {['İlkbahar', 'Yaz', 'Sonbahar', 'Kış'].map(season => (
                      <label key={season} className="flex items-center">
                        <input
                          type="checkbox"
                          checked={seasonFilter.includes(season)}
                          onChange={() => handleSeasonFilterChange(season)}
                        />
                        <span className="ml-2">{season}</span>
                      </label>
                    ))}
                  </div>
                </li>
                <li onClick={handleResetFilters} className="px-4 py-2 hover:bg-gray-200 flex items-center justify-between font-medium cursor-pointer">Sıfırla <FontAwesomeIcon className='float-right' icon={faRotateRight} /></li>
              </ul>
            )}
          </div>
        </div>
        <div className="w-[85%] h-[90%] mt-4 rounded overflow-y-auto flex flex-row flex-wrap gap-2 items-center justify-center"> 
          
          { filteredItems.length === 0 ? "Envanteriniz Boş, Lütfen Ürün Ekleyin !": (
            filteredItems.map((item, index) => (
              <div key={index} className="relative grid place-items-center bg-white/30 w-56 h-64 rounded p-3 shrink-0 shadow-inner border shadow-black/30">
                <button onClick={() => handleClick(0, item)} className="absolute top-2 right-11 grid place-items-center p-2 bg-blue-700 hover:bg-blue-800 text-white transition-all font-semibold rounded"><FontAwesomeIcon icon={faPen} /></button>
                <button onClick={() => handleClick(2, item)} className="absolute top-2 right-2 grid place-items-center p-2 bg-red-700 hover:bg-red-800 text-white transition-all font-semibold rounded"><FontAwesomeIcon className='' icon={faTrash} /></button>
                <p className='font-bold z-10 mt-5'>{item.ProductName} </p>
                <p className='text-sm font-bold'>Ürün ID: {item.ProductID}</p>
                <p className='text-4xl font-bold'>{item.InventoryLevel}</p>
                <p className='font-bold'>{item.Season}</p>
                <p className='font-bold w-full text-center'>{item.Date.slice(5,16)}</p>
              </div>
            ))
          )}
        </div>
      </div>

      {value >= 0 && (
        <div className="absolute w-screen h-screen bg-black/50 grid place-items-center backdrop-blur z-20">
          <div className="relative w-[60%] min-h-[60%] bg-white px-6 py-3 rounded shadow-inner shadow-black/30 border-2 border-gray-100 items-center justify-center flex">
            <span 
              onClick={() => setValue(-1)} 
              className='absolute right-4 top-0 float-right text-[40px] font-extrabold cursor-pointer shadow-black text-red-600 hover:text-red-700 hover:rotate-90 ease-in-out transition-all delay-0'>
              <FontAwesomeIcon icon={faXmark} />
            </span>
            <Actions refreshData={refreshData} value={value} item={selectedItem} datas={filteredItems} />
          </div>
        </div>
      )}
    </>
  );
}

export default Index;
