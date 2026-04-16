import { useState } from 'react';
import type { ChangeEvent, FormEvent } from 'react';
import { api } from '../api';

type LoginData = {
  phone: string;
  password: string;
};

type Props = {
  onLoggedIn?: (message: string, user: unknown) => void;
};

function getFirstErrorMessage(data: Record<string, unknown> | undefined) {
  if (!data) {
    return 'Login xatosi';
  }

  for (const value of Object.values(data)) {
    if (Array.isArray(value) && value.length > 0) {
      return String(value[0]);
    }

    if (typeof value === 'string' && value) {
      return value;
    }
  }

  return 'Login xatosi';
}

export default function Login({ onLoggedIn }: Props) {
  const [form, setForm] = useState<LoginData>({
    phone: '',
    password: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (field: keyof LoginData) => (
    event: ChangeEvent<HTMLInputElement>,
  ) => {
    setForm((current) => ({ ...current, [field]: event.target.value }));
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await api.post('/auth/login/', form);
      onLoggedIn?.(response.data.message ?? 'Login successful', response.data.user);
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
        <label>Telefon</label>
        <input
          value={form.phone}
          onChange={handleChange('phone')}
          placeholder="+998901234567"
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

      {error && <p className="error">{error}</p>}

      <button className="primary-btn" type="submit" disabled={loading}>
        {loading ? 'Kirish...' : 'Login'}
      </button>
    </form>
  );
}
