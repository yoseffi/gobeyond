# GitHub Pages Setup Instructions

Follow these steps to create a permanent URL for your **GoBeyond** app:

## Step 1: Initialize Git Repository

Run these commands in your terminal (from the GoBeyond project directory):

```bash
cd /path/to/your/gobeyond
git init
git add .
git commit -m "Initial commit: GoBeyond app"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon → **New repository**
3. Repository name: `gobeyond` (GitHub usernames and repo names are lowercase)
4. Description: "GoBeyond – Interactive AR quiz game"
5. Choose **Public** (required for free GitHub Pages)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click **Create repository**

## Step 3: Push to GitHub

GitHub will show you commands. Run these (replace `<your-username>` with your GitHub username):

```bash
git remote add origin https://github.com/<your-username>/gobeyond.git
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/<your-username>/gobeyond`
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**:
   - Select **Branch**: `main`
   - Select **Folder**: `/ (root)`
5. Click **Save**

## Step 5: Your Permanent URL

After a few minutes, your GoBeyond app will be live at:

```
https://<your-username>.github.io/gobeyond/
```

**Example**: If your username is `yhazan`, your URL will be:
```
https://yhazan.github.io/gobeyond/
```

## Step 6: Create Tiny URL & QR Code

### Tiny URL Options:
- **Bitly**: https://bitly.com (free account available)
- **TinyURL**: https://tinyurl.com (no account needed)
- **Rebrandly**: https://rebrandly.com (free custom short links)

### QR Code Generators:
- **QR Code Generator**: https://www.qr-code-generator.com
- **QRCode Monkey**: https://www.qrcode-monkey.com
- **Google Charts API**: `https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=YOUR_URL`

Just paste your GitHub Pages URL into any of these services!

## Troubleshooting

- **404 Error**: Wait 5-10 minutes after enabling Pages, GitHub needs time to build
- **Still 404**: Make sure `index.html` is in the root directory
- **Custom Domain**: See README.md for custom domain setup

## Next Steps

Once your GoBeyond URL is live:
1. Test it on mobile devices (the app uses camera/AR features)
2. Create your tiny URL
3. Generate QR code
4. Share with users!
