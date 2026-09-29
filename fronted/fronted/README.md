# Barber frontend

React + TypeScript interface for the Barber application.

See the [project README](../../README.md) for backend setup and the full development guide.

## Development

Use Node.js 22.12+. From this directory:

```bash
npm ci
npm run dev
```

Copy `.env.example` to `.env` and set `VITE_API_URL=http://127.0.0.1:8000` for a local backend. Restart Vite after changing environment variables.

## Checks

```bash
npm run build
npm run lint
```
