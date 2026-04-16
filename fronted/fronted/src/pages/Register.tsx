import { useState } from 'react';
import type { ChangeEvent, FormEvent } from 'react';
import { api } from '../api';

type RegisterData = {
  name: string;
  phone: string;
  email: string;
  password: string;
  password2: string;
};

type Props = {
  onRegistered?: (message: string) => void;
};

function getFirstErrorMessage(data: Record<string, unknown> | undefined) {
  if (!data) {
    return 'Register xatosi';
  }

  for (const value of Object.values(data)) {
    if (Array.isArray(value) && value.length > 0) {
      return String(value[0]);
    }

    if (typeof value === 'string' && value) {
      return value;
    }
  }

  return 'Register xatosi';
}

export default function Register({ onRegistered }: Props) {
  const [form, setForm] = useState<RegisterData>({
    name: '',
    phone: '',
    email: '',
    password: '',
    password2: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (field: keyof RegisterData) => (
    event: ChangeEvent<HTMLInputElement>,
  ) => {
    setForm((current) => ({ ...current, [field]: event.target.value }));
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setError('');

    try {
      await api.post('/auth/register/', form);
      onRegistered?.('Ro`yxatdan o`tish muvaffaqiyatli');
      setForm({
        name: '',
        phone: '',
        email: '',
        password: '',
        password2: '',
      });
    } catch (err: unknown) {
      const error = err as {
        response?: {
          data?: Record<string, unknown>;
        };
      };
      setError(getFirstErrorMessage(error.response?.data));
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <div className="field">
        <label>Ism</label>
        <input value={form.name} onChange={handleChange('name')} placeholder="Ali" />
      </div>

      <div className="field">
        <label>Telefon</label>
        <input
          value={form.phone}
          onChange={handleChange('phone')}
          placeholder="+998901234567"
        />
      </div>

      <div className="field">
        <label>Email</label>
        <input
          type="email"
          value={form.email}
          onChange={handleChange('email')}
          placeholder="ali@mail.com"
        />
      </div>

      <div className="field">
        <label>Parol</label>
        <input
          type="password"
          value={form.password}
          onChange={handleChange('password')}
          placeholder="********"
        />
      </div>

      <div className="field">
        <label>Parolni takrorlang</label>
        <input
          type="password"
          value={form.password2}
          onChange={handleChange('password2')}
          placeholder="********"
        />
      </div>

      {error && <p className="error">{error}</p>}

      <button className="primary-btn" type="submit" disabled={loading}>
        {loading ? 'Yuborilmoqda...' : 'Register'}
      </button>
    </form>
  );
}
