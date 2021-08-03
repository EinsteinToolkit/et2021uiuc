---
layout: default
title: Instructions
---

<div class="container-fluid" markdown="1">
# Instructions

## Connecting
The school will be completely virtual with sessions hosted via the University
of Illinois' Zoom subscription. In order to join, you will need to log into
your Zoom account (any account, it does not have to be associated with a
University) and there will be a waiting room. A live video stream of the
meeting will be available on YouTube once the meeting starts. Please note that
some sessions will be recorded.

We will use Gitter as a chat solution for chats that persist across Zoom
sessions. You will need a GitHub, GitLab or Twitter account to be able to post
messages but can read without logging in. The chat, in addition to the website,
will be used to disseminate information during the workshop, such as schedule
changes, breaks and YouTube channel URLs.

Each day before and after the actual school there will be a 30 minutes "help
session" for the tutorials and also general discussions.

Gitter chat:
[https://gitter.im/EinsteinToolkit/workshop](https://gitter.im/EinsteinToolkit/workshop)

The Zoom meeting opens at 7:45AM CDT each day, the school program starts at
8:25AM CDT. Zoom login information is provided in the information package sent
to each registered participant.

## YouTube Stream
A life stream is provided via [YouTube](https://go.illinois.edu/et2021uiuc).
Please note that there is about a 30s delay, so please enter all questions to
speeakers well in advance of the end of the preseentation.

## Tutorial server

We will be using a server sponsored by the Center for Computation & Technology
at Louisina State University. Login information will be provided during the
first day of the summer school in both the 7:55AM CDT "Setup Help"
[session](program.html), during lunch break and at the beginning of the
[first tutorial](lectures/10-SteveBrandt/index.html).

The tutorial is Jupyter based and, if you prefer, you can run the tutorial
environment in a Docker container on your own computer rather than using an
account on the tutorial server.

We provide a Docker compose
[file](https://github.com/nds-org/jupyter-et/blob/master/tutorial-server/docker-compose.user.yml)
which also contains information on how to set this up.

To use the file you will need `docker` and `docker-compose` installed.

See this link for macOS and Windows: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

On linux, you can probably use your package manager (apt, dnf, yum, etc.).

1. Download this file and save it as `docker-compose.yml`:
```bash
curl -o docker-compose.yml https://raw.githubusercontent.com/nds-org/jupyter-et/master/tutorial-server/docker-compose.user.yml
```

2. Start the server:
```bash
docker-compose up -d
```

3. Get the URL for the server:
```bash
docker-compose logs
```

You will see output of the form. Copy the URL and paste it in your browser.

```
et-notebook | To access the notebook, open this file in a browser copy and paste this URL:
et-notebook |
et-notebook |  http://localhost:8888/?token=IHxGfgOO3P1efasL2s5BAtlC1haaG43X
et-notebook |
et-notebook | [I 14:13:24.359 NotebookApp] Serving notebooks from local directory: /home/jovyan
```

4. entering the Docker container
You can enter ("log in" in some sense) the container hosting the notebook server using docker commands:

```bash
docker exec -it et-notebook bash
```

or

```bash
docker exec -it --user 0 et-notebook bash
```

if you need to be root in the container to for example install extra packages.

5. transferring files
Docker provides commands to copy files into and out of containers:

```bash
# to copy in
docker cp file et-notebook:/home/jovyan/
# to copy out
docker cp et-notebook:/home/jovyan/file $PWD
```

## xTensor tutorial

To run the tutorial on your own laptop, please install the xAct package before
class; see [xAct.es](http://www.xact.es). You will require a Mathematica
license for this tutorial.


</div>
