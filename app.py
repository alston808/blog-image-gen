import click
import requests

# This must match the CLI_TOKEN you set in the DO Control Panel
CLI_TOKEN = "your-secure-token-here"
API_URL = "https://blog-image-gen-xxxxx.ondigitalocean.app/generate" # Update with your live URL

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def run(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    response = requests.post(
        API_URL,
        json={"text": text},
        headers={"X-API-Key": CLI_TOKEN}
    )
    
    if response.status_code == 200:
        click.echo(f"Success! Image URL: {response.json()['image_url']}")
    else:
        click.echo(f"Failed with status {response.status_code}: {response.text}")

if __name__ == '__main__':
    run()
