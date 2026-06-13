import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter} from "react-router-dom";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyCGAB60-acaAGQeFF9YizovQGFH8jCg2o8",
  authDomain: "url-shortner-202b2.firebaseapp.com",
  projectId: "url-shortner-202b2",
  storageBucket: "url-shortner-202b2.firebasestorage.app",
  messagingSenderId: "549800949399",
  appId: "1:549800949399:web:0943191fd75f7047271bd2",
  measurementId: "G-PNBFK6TWCG"
};
initializeApp(firebaseConfig);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
<BrowserRouter>
    <App />
</BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
