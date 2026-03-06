# Cloudflare Python Worker


### BEFORE YOU START GIT CLONE, PLEASE READ TO THE END TO NOT END UP GIVING UP

After hour of considering whether to continue coding or start poultry, I managed to deploy my first python CloudFlare worker.
It took me around 3 hours just do deploy the code listed in official docs(https://developers.cloudflare.com/workers/languages/python/packages/fastapi/)

This is what I managed to come up with, and coding is worth again

## Prerequisites

- [Node.js](https://nodejs.org/)
- [uv](https://github.com/astral-sh/uv) (Python package installer and resolver)

## Setup

1. Run this commands on your project(preferably in your pc terminal and not ide terminal):
please continue reading first, dont open your terminal yet
   ```bash
   uv init
   uv tool install workers-py
   uv run pywrangler init
   ```
   This will create a `pyproject.toml` file with workers-py as a development dependency.
   `pywrangler init` will create a wrangler config file.

## Development

To run the worker locally(I dont know if it will work since It failed for me, I suck at cli stuff):

```bash
uv run pywrangler dev
```

## Deployment

To deploy the worker to Cloudflare:

```bash
uv run pywrangler deploy
```
Honestly speaking, I suck at cli tools, so this failed for me(don't know how, but it failed, believe me)
so I came up with this other method of using the GUI provided by CloudFlare directly from your CloudFlare Workers & Pages.


To do so, you will need to follow this steps.

1. Fork this repo
    https://github.com/NotoriousBigg/cloudflare-pyworker/fork

2. Import the project to your CloudFlare workers.

    you can import this project to your cloudflare workers by clicking on the "Create Application" button.
    This interface will appear:
    <img src="./src/assets/create_application.png" alt="select continue with github" width="500">

    Select "continue with github"

    This will prompt you to install cloudflare workers to your github if you have not done so. If you have already installed, proceed to the next step

    Select the repo you want:
    <img src="./src/assets/select_repo.png" alt="select the repository" width="500">

    and click Next

    On the next screen, Setup this:
    <img src="./src/assets/set_configs.png" alt="set the configs" width="500">

    Note:
        The project name config here should be the same as the one in wrangler.jsonc
        ```jsonc
        	"name": "cloudflare-pyworker",
        ```
        and in package.json(not sure though):
        ```
        "name": "cloudflare-pyworker",
        ```

    You should not fill the Build command if your project have the pyproject.toml file.
    From my opinion(trust me bro):
        run this command:
            ```
            uv init && uv tool install workers-py && uv run pywrangler init
            ```
        before everything. This will setup everything for you, then you should  not fill the build command.

        but if you are a pro dev, then you can add the command as it is(this will not work if you already have the toml file)


    Then click on the "Deploy button"


    At last, the builds for the project should be as:

    <img src="./src/assets/builds.png" alt="Final builds" width="500">

    That's it.

To add new routes, you just add the code in /src/entry.py or you set up your own custom routers(from fastapi import APIRouter)

About dependencies, cloudflare pyworkers does not support requirements.txt files.

They say you should name the files as cf-requirements.txt. But this still does not work, so the correct way is to add them
on the pyproject.toml file:

```
dependencies = [
    "webtypy>=0.1.7",
    "fastapi"
    "you can add other here like httpx, etc(don't know if they support all pypi modules)"
]
```
This is one reason why you should run the build commands manually and then upload them to github.


