# Vishal Lokhande — Personal Website

A personal portfolio site built with plain HTML, CSS, and JavaScript.

## Preview locally

```bash
cd personal-website
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Deploy with your personal GitHub

The code is already pushed to [github.com/VishalLokh/portfolio](https://github.com/VishalLokh/portfolio).

### 1. Deploy on Vercel (recommended, free subdomain)

1. Go to https://vercel.com and sign in with your `VishalLokh` GitHub account.
2. Click **Add New Project** → import the `portfolio` repo.
3. Framework preset: **Other** (it's a static site, no build step needed).
4. Click **Deploy**. Vercel will give you a live URL like `portfolio-vishallokh.vercel.app`.
5. Every push to `main` auto-redeploys.

### 2. Alternative: Netlify

1. Go to https://app.netlify.com and sign in with GitHub.
2. **Add new site → Import an existing project** → pick the `portfolio` repo.
3. Build command: leave empty. Publish directory: `.`
4. Deploy — you'll get a URL like `portfolio-vishallokh.netlify.app`.

### 3. Alternative: GitHub Pages (also free)

In the repo on GitHub: **Settings → Pages → Source: `main` branch, `/ (root)`**. Your site will be live at `https://VishalLokh.github.io/portfolio`.

## Custom domain (optional, later)

You don't need to buy a domain to get started. If you want one later, buy it from any registrar (Namecheap, Google Domains, etc.) and connect it in your Vercel/Netlify project settings under **Domains**.

## Updating content

- Edit text directly in [index.html](index.html).
- Colors and layout live in [styles.css](styles.css).
- Small interactive behavior (mobile nav) is in [script.js](script.js).
