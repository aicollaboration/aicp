import typer
import os


def search_docker():
    files = os.listdir(os.getcwd())

    if "Dockerfile" in files:
        with open("Dockerfile", "r") as file:
            return file.read()

    return None

def search_docker_compose():
    files = os.listdir(os.getcwd())

    if "docker-compose.yaml" in files:
        with open("docker-compose.yaml", "r") as file:
            return file.read()

    if "docker-compose.yml" in files:
        with open("docker-compose.yml", "r") as file:
            return file.read()

    return None

def search_openapi():
    files = os.listdir(os.getcwd())

    if "openapi.yaml" in files:
        with open("openapi.yaml", "r") as file:
            return file.read()

    if "openapi.yml" in files:
        with open("openapi.yml", "r") as file:
            return file.read()

    if "openapi.json" in files:
        with open("openapi.json", "r") as file:
            return file.read()

    return None

def search_kubernetes():
    search_result = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file_path in files:
            if file_path.endswith(".yaml") or file_path.endswith(".yml"):
                with open('{}/{}'.format(root, file_path), "r") as file:
                    file_content = file.read()
                    if "apiVersion: " in file_content:
                        search_result.append({
                            'path': '{}/{}'.format(root, file_path),
                            'content': file_content,
                        })
    
    return search_result


def download_github_zipfile_and_extract(name):
    typer.echo("Downloading zip file from github...")
    url = "https://github.com/aicollaboration/service-template-python/archive/refs/heads/main.zip"
    os.system("curl -L {} -o {}.zip".format(url, name))
    typer.echo("Downloaded zip file from github.")

    typer.echo("Extracting zip file...")
    os.system("unzip {}.zip".format(name))
    typer.echo("Extracted zip file.")

    typer.echo("Removing zip file...")
    os.system("rm {}.zip".format(name))
    typer.echo("Removed zip file.")

    typer.echo("Moving extracted files to current directory...")
    os.system("mv service-template-python-main {}".format(name))
    typer.echo("Moved extracted files to current directory.")

    return name

def replace_placeholder_in_file(file_path, placeholder, value):
    with open(file_path, "r") as file:
        file_content = file.read()
        file_content = file_content.replace(placeholder, value)
        with open(file_path, "w") as file:
            file.write(file_content)


app = typer.Typer()


@app.command('create')
def create_service(name: str):
    typer.echo(f"Create service: {name}")

    download_github_zipfile_and_extract(name)

    typer.echo("Replace placeholder...")
    replace_placeholder_in_file("{}/{}/deployment/manifests/api-ingress.yaml".format('.', name), "<repo>", name)
    replace_placeholder_in_file("{}/{}/deployment/manifests/deployment.yml".format('.', name), "<repo>", name)
    replace_placeholder_in_file("{}/{}/deployment/manifests/service.yml".format('.', name), "<repo>", name)




@app.command('import')
def import_service():
    typer.echo(f"Import service")

    docker_compose = search_docker_compose()
    print('✔' if docker_compose else '✘', 'docker-compose.yaml')

    docker = search_docker()
    print('✔' if docker else '✘', 'Dockerfile')

    openapi = search_openapi()
    print('✔' if openapi else '✘', 'openapi.yaml')

    kubernetes = search_kubernetes()
    print('✔' if kubernetes else '✘', 'kubernetes')

