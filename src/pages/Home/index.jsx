import React from 'react';
import axios from 'axios';
import { Button, Checkbox, Form, Input, Flex } from 'antd';
import { LockOutlined, UserOutlined, MailOutlined } from '@ant-design/icons';
import { useNavigate, Navigate, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { setUserEmail, setUserFullName, setUserID, setUserPassword } from '../../redux/userSlice';

function Index() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const user = useSelector((state) => state.user.userID);
    const location = useLocation();
    if (user) return <Navigate to="/panel" state={{ from: location }} replace />

    const handleLogin = async (values) => {
        try {
            const { mail, password } = values;
            const response = await axios.post('http://localhost:5000/api/login', { mail, password }, { withCredentials: true });
            console.log('Login response:', response.data);
            dispatch(setUserEmail(response.data.user.email));
            dispatch(setUserPassword(response.data.user.password));
            dispatch(setUserFullName(response.data.user.fullname));
            dispatch(setUserID(response.data.user.userID)); // UserID'yi Redux'a kaydet
            navigate('/panel');
        } catch (error) {
            alert("Hatalı Giriş Yaptınız!")
            console.error('Login error:', error);
        }
    };

    const handleSign = async (values) => {
        try {
            const { fullname, mail, password, password2 } = values;

            // Şifrelerin eşleşip eşleşmediğini kontrol et
            if (password !== password2) {
                alert('Passwords do not match!');
                return;
            }

            const response = await axios.post('http://localhost:5000/api/register', { fullname, password, mail }, { withCredentials: true });
            console.log('Register response:', response.data);
            dispatch(setUserEmail(response.data.user.email));
            dispatch(setUserFullName(response.data.user.fullname));
            dispatch(setUserID(response.data.user.userID)); // UserID'yi Redux'a kaydet
            navigate('/panel');
        } catch (error) {
            console.error('Register error:', error);
        }
    };

    return (
        <div className='w-[80%] bg-white/30 border shadow-inner shadow-black/30 h-[80%] mx-auto flex flex-row items-center justify-evenly rounded'>
            <div className="flex flex-col w-[250px] scale-110">
                <span className='w-full bg-black text-center items-center text-white px-4 py-2 mb-3 rounded font-semibold'>Login</span>
                <Form
                    name="login"
                    initialValues={{ remember: true }}
                    style={{ maxWidth: 360 }}
                    onFinish={handleLogin}
                >
                    <Form.Item
                        name="mail"
                        rules={[{ required: true, message: 'Please input your Mail!' }]}
                    >
                        <Input prefix={<MailOutlined />} placeholder="Mail" />
                    </Form.Item>
                    <Form.Item
                        name="password"
                        rules={[{ required: true, message: 'Please input your Password!' }]}
                    >
                        <Input prefix={<LockOutlined />} type="password" placeholder="Password" />
                    </Form.Item>
                    <Form.Item>
                        <Flex justify="space-between" align="center">
                            <Form.Item name="remember" valuePropName="checked" noStyle>
                                <Checkbox>Remember me</Checkbox>
                            </Form.Item>
                            <a href="">Forgot password</a>
                        </Flex>
                    </Form.Item>
                    <Form.Item>
                        <Button block type="primary" htmlType="submit">
                            Log in
                        </Button>
                    </Form.Item>
                </Form>
            </div>
            <div className="flex flex-col w-[250px] scale-110">
                <span className='w-full bg-black text-center items-center text-white px-4 py-2 mb-3 rounded font-semibold'>Register</span>
                <Form
                    name="register"
                    initialValues={{ remember: true }}
                    style={{ maxWidth: 360 }}
                    onFinish={handleSign}
                >
                    <Form.Item
                        name="fullname"
                        rules={[{ required: true, message: 'Please input your Full Name!' }]}
                    >
                        <Input prefix={<UserOutlined />} placeholder="Full Name" />
                    </Form.Item>
                    <Form.Item
                        name="mail"
                        rules={[{ type: 'email', required: true, message: 'Please input your e-Mail!' }]}
                    >
                        <Input prefix={<MailOutlined />} placeholder="Email" />
                    </Form.Item>
                    <Form.Item
                        name="password"
                        rules={[{ required: true, message: 'Please input your Password!' }]}
                    >
                        <Input prefix={<LockOutlined />} type="password" placeholder="Password" />
                    </Form.Item>
                    <Form.Item
                        name="password2"
                        rules={[{ required: true, message: 'Please input your Password Again!' }]}
                    >
                        <Input prefix={<LockOutlined />} type="password" placeholder="Password Again" />
                    </Form.Item>
                    <Form.Item>
                        <Button block type="primary" htmlType="submit">
                            Sign in
                        </Button>
                    </Form.Item>
                </Form>
            </div>
        </div>
    );
}

export default Index;
