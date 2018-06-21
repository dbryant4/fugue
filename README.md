# Fugue Technical Assessment

## Problem

The provided tarball contains a small static HTML application that needs to be version controlled and deployable via Docker. Your task is to:

- Create a new git repository for the supplied static files.
- Write an HTTP server to serve the static files in the programming language of your choice and include the code in the git repository. You may use any existing libraries when implementing your HTTP server, but may not use an off the shelf HTTP server such as nginx or Apache (humor us). Your server should support a health check at the /health URL that returns HTTP code 200 and the following JSON if the server is healthy: {"status":"Ok"}.- Package your server and the static files in a Docker container that exposes the HTTP server.

- Setup CI/CD to build and test your server and the Docker container.

- Deploy the container to a docker registry when a release happens (a release is signaled by tagging the repository with a tag in the format of vX.Y.Z
- Any other tooling or processes you think would be important in a production CI/CD pipeline. You are free to use the programming language of your choice as well as any existing Docker images, git hosting (Github, Gitlab, etc...), hosted CI services (Travis, CircleCI, Gitlab, etc...), or tooling that makes sense. Note that you should be able to implement this project using the free offerings from most hosted git and CI services. Feel free to follow up with us via email if you have any questions about the problem.

## Deliverables

Send us a link to the git repository containing your work and the corresponding CI project along with any instructions on how to run the docker container.
