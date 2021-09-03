## Slides 5-7

First build our application in a container so we can run it interactively:

`podman build -t hello:cli -f Dockerfile.hello .`

Run the container interactively:

`podman run -it --rm hello:cli bash`

Add entrypoint to container:

`podman build -t hello:cli -f Dockerfile.hello-1 .`

Run container as a CLI tool non-interactively

`podman run -it --rm hello:cli --name=Lisa`

Add some fun ASCII art to our cli tool:

`podman build -t hello:cli -f Dockerfile.hello-2 .`

`podman run -it --rm hello:cli --name=Lisa`

Build and run a simple web application.

`podman build -t hello:cli -f Dockerfile.hello-web .`

We will need to use the -p flag to map the ports 5000 on the host machine to the container port. This is the default port for Flask.

`podman run -it --rm -p 5000:5000 hello:web`

## Slides 8-9

Building completely on the command line with buildah:

```
newcontainer=$(buildah from python:3) && echo $newcontainer
buildah copy $newcontainer . .
buildah config --entrypoint $newcontainer '[“python”, “hello-cli.py”]'
buildah commit --rm $newcontainer hello:cli
```

Now we can run this with podman container like we did before!

`podman run -it --rm hello:cli --name=Lisa`

## Slides 10-11

Build our container with the external registry

`podman build -t quay.io/lranjbar/hello:cli -f Dockerfile.hello-1 .`

Push the container to the external registry

`podman push quay.io/lranjbar/hello:cli`

Copy an image to a new tag

`skopeo copy docker://quay.io/lranjbar/hello:cli docker://quay.io/lranjbar/hello:latest`

Inspect my external image

`skopeo inspect docker://quay.io/lranjbar/hello`

## Slides 12

Create a new toolbox

`toolbox create`

This is a podman based container so you can see it running with the command

`podman container list`

Enter the toolbox to play around

`toolbox enter`

Install ansible

`sudo dnf install ansible`

Run the hello world playbook

`ansible-playbook hello-playbook.yaml`

Exit the toolbox

`exit`

Stop the toolbox container

`podman container stop fedora-toolbox-33`

Remove the toolbox container

`toolbox rm fedora-toolbox-33`

