import { createBrowserRouter } from 'react-router-dom';
import MainLayout from '../layouts/main';
import Home from "../pages/Home";
import Panel from "../pages/Panel";
import Settings from "../pages/Settings";
import PrivateRoute from '../PrivateRoute';

const routes = createBrowserRouter([
    {
        path: '/', 
        element: <MainLayout/>,
        children: [
            {
                index: true,
                element: <Home/>,
            },            
            {
                path: "index",
                element: <Home/>,
            },
            {
                path: "panel",
                element: <PrivateRoute element={<Panel />} />,
            },
            {
                path: "settings",
                element: <PrivateRoute element={<Settings />} />,
            }
        ] 
    },
    {
        path: '*',
        element: "404 - Aradığınız Sayfa Bulunamadı!"
    }    
]);

export default routes;
