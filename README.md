# URL Shortener

A full-stack URL shortening app. Paste a long URL, get a short one. Click the short link, get redirected.

Built with React + Flask + Firebase, deployed on Render.

---

## Tech Stack

- **Frontend** — React 19, React Router v7, Bootstrap, nanoid
- **Backend** — Python Flask + Gunicorn, Firebase Admin SDK
- **Database** — Firebase Realtime Database
- **Deployment** — Render (Web Service, free tier)

---

## Project Structure

```
URL-SHORTNER/
├── .gitignore                     # Covers both client and server
├── render.yaml                    # Render deployment config
├── README.md
│
├── url-shortner-client/           # React source (not deployed directly)
│   ├── src/
│   ├── public/
│   ├── .gitignore
│   └── package.json
│
└── url-shortner-server/           # Flask app (deployed to Render)
    ├── app/
    │   ├── main.py                # Flask routes
    │   └── build/                 # React production build (gitignored)
    ├── wsgi.py                    # Gunicorn entry point
    ├── requirements.txt
    └── .gitignore
```

---

## How It Works

1. User pastes a long URL into the React form
2. Frontend generates a unique key with `nanoid`
3. Key + URL saved to Firebase Realtime Database
4. User gets a short link: `yourapp.onrender.com/<key>`
5. Flask looks up the key and redirects to the original URL

---

## Local Setup

### Prerequisites
- Node.js + npm
- Python 3.x
- Firebase project with Realtime Database enabled

### Client

```bash
cd url-shortner-client
npm install
npm start
```

Runs on `http://localhost:3000`

Create `url-shortner-client/.env.local`:

```env
REACT_APP_FIREBASE_API_KEY=...
REACT_APP_FIREBASE_AUTH_DOMAIN=...
REACT_APP_FIREBASE_PROJECT_ID=...
REACT_APP_FIREBASE_STORAGE_BUCKET=...
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=...
REACT_APP_FIREBASE_APP_ID=...
REACT_APP_FIREBASE_MEASUREMENT_ID=...
```

### Server

```bash
cd url-shortner-server
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python wsgi.py
```

Runs on `http://localhost:5000`

Create `url-shortner-server/.env`:

```env
DATABASE_URL=https://your-project-id-default-rtdb.firebaseio.com/
```

Place `ServiceAccountKey.json` in `url-shortner-server/`.
> ⚠️ This file is gitignored — never push it to GitHub.

---

## Deployment (Render)

Flask serves the React build as static files — one Render Web Service handles everything.

### Before Deploying

Build the React app and copy it into the server:

```bash
cd url-shortner-client
npm run build
cp -r build ../url-shortner-server/app/build
```

### Deploy Steps

1. Push repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set the following in Render dashboard:

| Setting | Value |
|--------|-------|
| Root Directory | `url-shortner-server` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn wsgi:app` |
| Plan | Free |

5. Add environment variables in Render → Environment:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Your Firebase Realtime DB URL |
| `FIREBASE_CREDENTIALS` | Paste full contents of `ServiceAccountKey.json` |

> ⚠️ Never add `ServiceAccountKey.json` to the repo. Use the env variable approach above.

---

## What Goes to GitHub

| File / Folder | Pushed? |
|---------------|---------|
| `url-shortner-client/src/` | ✅ Yes |
| `url-shortner-server/app/main.py` | ✅ Yes |
| `wsgi.py`, `requirements.txt` | ✅ Yes |
| `ServiceAccountKey.json` | ❌ No (gitignored) |
| `node_modules/`, `venv/` | ❌ No (gitignored) |
| `app/build/` | ❌ No (gitignored, rebuilt on Render) |
