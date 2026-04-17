import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Définir dynamiquement l'URL du backend pour les composants
if (!process.env.REACT_APP_CODESPACE_URL) {
  // Remplacez par votre nom de codespace ou définissez-le dans .env
  process.env.REACT_APP_CODESPACE_URL = 'https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev';
  console.log('REACT_APP_CODESPACE_URL set to', process.env.REACT_APP_CODESPACE_URL);
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
