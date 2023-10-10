### Run the code

We highly recommend to run the services with Docker.

#### Run inside docker
1. Build the docker image. `# docker build -t <name> .`
2. Run the service. `# docker run -it <name>`
3. Optionally, run the demo. `$ python3 demo.py`

#### Run directly.
1. Make sure all the libs have been installed.
2. Install Nginx.
3. Copy our conf to Nginx conf dir.
4. Start Nginx
5. Start Auth service. `$ cd auth && python3 main.py &`
6. Start URL service. `$ cs urlshortner && python3 main.py &`
7. Optionally, run the demo.

