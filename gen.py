import click
import requests

# Set this environment variable in your local ~/.bashrc or ~/.zshrc
CLI_TOKEN = "DIGITALOCEAN_API_KEY"
API_URL = "https://blog-image-gen.ondigitalocean.app/generate"

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def run(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    response = requests.post(
        API_URL,
        json={"text": text},
        headers={"X-API-Key": DIGITALOCEAN_API_KEY}
    )
    
    if response.status_code == 200:
        click.echo(f"Success! Image URL: {response.json()['image_url']}")
    else:
        click.echo(f"Failed: {response.text}")

if __name__ == '__main__':
    run()
