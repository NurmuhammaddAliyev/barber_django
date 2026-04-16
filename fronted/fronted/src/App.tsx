import { useState } from 'react';
import Login from './pages/Login';
import Register from './pages/Register';
import './App.css';

type Tab = 'login' | 'register';

function App() {
  const [activeTab, setActiveTab] = useState<Tab>('register');
  const [message, setMessage] = useState('');

  return (
    <main className="app-shell">
      <section className="hero-panel">
        <div className="badge">Barber API</div>
        <h1>Login va register frontend</h1>
        <p className="lead">
          Bu sahifa Django backenddagi <code>/auth/register/</code> va{' '}
          <code>/auth/login/</code> endpointlariga ulanadi.
        </p>

        <div className="switcher">
          <button
            className={activeTab === 'register' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('register')}
            type="button"
          >
            Register
          </button>
          <button
            className={activeTab === 'login' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('login')}
            type="button"
          >
            Login
          </button>
        </div>

        {message && <div className="notice">{message}</div>}
      </section>

      <section className="form-panel">
        {activeTab === 'register' ? (
          <Register onRegistered={setMessage} />
        ) : (
          <Login
            onLoggedIn={(text) => {
              setMessage(text);
            }}
          />
        )}
      </section>
    </main>
  );
}

export default App;
