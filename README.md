# GoBeyond

An interactive AR quiz game for math and spelling challenges.

## GitHub Pages Setup

This project is configured to be hosted on GitHub Pages. Once you push this repository to GitHub, follow these steps:

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under **Source**, select:
   - **Branch**: `main` (or `master`)
   - **Folder**: `/ (root)`
4. Click **Save**

### 2. Your Permanent URL

After enabling GitHub Pages, your app will be available at:

```
https://<your-username>.github.io/gobeyond/
```

For example: `https://yhazan.github.io/gobeyond/`

### 3. Create Tiny URL & QR Code

Once you have your GitHub Pages URL:

1. **Tiny URL**: Use a service like:
   - [Bitly](https://bitly.com)
   - [TinyURL](https://tinyurl.com)
   - [Rebrandly](https://rebrandly.com)

2. **QR Code**: Generate using:
   - [QR Code Generator](https://www.qr-code-generator.com)
   - [QRCode Monkey](https://www.qrcode-monkey.com)
   - Or use the GitHub Pages URL directly

### 4. Custom Domain (Optional)

If you want a custom domain:

1. Add a `CNAME` file in the root with your domain name
2. Configure DNS records to point to GitHub Pages
3. See [GitHub Pages custom domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

## Local Development

Simply open `index.html` in a browser or use a local server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`
