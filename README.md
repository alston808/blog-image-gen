# Blog Header Image Generator

This repository provides a lightweight Python-based microservice designed for deployment on the **DigitalOcean App Platform**. It acts as a secure API proxy, interfacing with the **DigitalOcean Native Inference Engine** to generate high-quality images in an absurdist digital painting style for your blog headers.

**Note: Following these steps may result in charges for the use of DigitalOcean services (minimum $5/month for the Basic-XS container tier).**

---

## Deployment

Click the button below to deploy this service to your DigitalOcean account.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/alston808/blog-image-gen/tree/main)

### Manual Setup & Forking
To enable automatic re-deployment on code pushes:
1. **Fork** this repository to your GitHub account.
2. In the [DigitalOcean Apps Control Panel](https://cloud.digitalocean.com/apps), click **Create App**.
3. Select **GitHub** and choose your fork of this repository.
4. Set the region to **SFO (San Francisco)**.
5. In the **Environment Variables** section, you must add the following keys (marked as **Secret**):
    * `DO_API_TOKEN`: Your Personal Access Token (PAT) with read/write access.
    * `CLI_TOKEN`: A custom password/token of your choosing to secure your API from unauthorized access.

---

## Usage

Once deployed, the App Platform will provide a public URL (e.g., `https://blog-image-gen-xxxxx.ondigitalocean.app`).

### Using the CLI
Use the provided `gen.py` script on your local machine to generate headers from your blog post text:

1. Update the `API_URL` variable in `gen.py` with your live App Platform URL.
2. Ensure `CLI_TOKEN` in `gen.py` matches the secret you set in the DO Control Panel.
3. Execute the generator:
   ```bash
   python gen.py path/to/your/blog_post.txt
