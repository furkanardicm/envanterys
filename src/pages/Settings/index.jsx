import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faPowerOff, faTrash } from '@fortawesome/free-solid-svg-icons';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { clearUser, updateUser } from '../../redux/userSlice';
import { persistor } from '../../redux/store';

function Index() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.user);
  const [oldPassword, setOldPassword] = useState(user.password || '');
  const [fullname, setFullname] = useState(user.fullname || '');
  const [password, setPassword] = useState(null);
  const [email, setEmail] = useState(user.email || '');

  const handleLogOut = () => {
    dispatch(clearUser());
    persistor.purge();
    navigate('/');
  };
  
  const handleUpdate = async (e) => {
    e.preventDefault(); // Formun gönderilmesini engelle

    if (!fullname || !email) {
      alert("Tüm alanlar doldurulmalıdır!");
      return;
    }

    // E-posta formatını kontrol et
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      alert("Geçerli bir e-posta adresi girin!");
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/api/updateUser', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: user.userID, fullname, password, oldpassword:oldPassword, email }),
      });

      if (response.ok) {
        alert("Güncelleme işlemi başarılı!")
        const data = await response.json();
        setPassword(data.password)
        setOldPassword(data.hashed_password)
        dispatch(updateUser({ fullname, email, password: data.hashed_password }));
      } else {
        console.error('Kullanıcı bilgileri güncellenemedi');
      }
    } catch (error) {
      console.error('API çağrısında hata:', error);
    }
  };

  return (
    <div className='relative mx-auto w-[80%] h-[80%] bg-white/30 shadow-inner p-4 stroke-black/30 border rounded flex flex-col items-center justify-center'>
      <form onSubmit={handleUpdate} className="w-[85%] h-[90%] rounded overflow-y-auto flex flex-col flex-wrap gap-10">
        <div className="flex flex-col">
          <label className='font-semibold' htmlFor="kadi">Kullanıcı Adı</label>
          <div className="flex flex-row gap-3 items-center">
            <input
              id="kadi"
              className='max-w-[350px] min-w-[290px] bg-white/30 h-[50px] rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
              type="text"
              value={fullname}
              onChange={(e) => setFullname(e.target.value)}
              placeholder=''
              required
            />
          </div>
        </div>
        <div className="flex flex-col">
          <label className='font-semibold' htmlFor="ksifre">Kullanıcı Şifre</label>
          <div className="flex flex-row gap-3 items-center">
            <input
              id="ksifre"
              className='max-w-[350px] min-w-[290px] bg-white/30 h-[50px] rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder='Yeni şifrenizi girin (isteğe bağlı)'
            />
            
          </div>
        </div>
        <div className="flex flex-col">
          <label className='font-semibold' htmlFor="kmail">Kullanıcı Mail</label>
          <div className="flex flex-row gap-3 items-center">
            <input
              id="kmail"
              className='max-w-[350px] min-w-[290px] bg-white/30 h-[50px] rounded px-4 py-2 text-black font-semibold shadow-black/30 shadow-inner border'
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder=''
              required
            />
          </div>
        </div>
        <div className="flex flex-row gap-2">
          <div className="flex flex-col">
            <div className="flex flex-row gap-3 items-center">
              <button type="submit" className="w-36 h-12 bg-blue-700 hover:bg-blue-800 text-white transition-all font-semibold rounded">
                Güncelle <FontAwesomeIcon className='ml-2' icon={faPen} />
              </button>
            </div>
          </div>
          <div className="flex flex-col">
            <div className="flex flex-row gap-3 items-center">
              <button onClick={handleLogOut} className="w-36 h-12 bg-red-700 hover:bg-red-800 border border-red-900 text-white transition-all font-semibold rounded">
                Çıkış Yap <FontAwesomeIcon className='ml-2' icon={faPowerOff} />
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}

export default Index;
