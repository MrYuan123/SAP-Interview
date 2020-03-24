# SAP-Interview
> This is the Github Repository for SAP SVNT Program.

## 1. Task Description

- Create a basic Flask web application:
	- `Root /` is not important :)
	- `/<int:number>` will display integers from 1 to that number
	- `/<int:number>/odd` will display only odd numbers in that range
	- `/<int:number>/even` will display only even numbers in that range
	- `/<int:number>/prime` will display only prime numbers in that range

- Extra points for creating Dockerfile so I can spin it up faster when testing

## 2. How to Use That

- Git clone the Git repo to the local machine:
		
		git clone git@github.com:MrYuan123/SAP-Interview.git	
- Build the docker image:

		docker build -t my_app:latest .
		
- Run the docker container:

		docker run -d -p 5000:5000 my_app:latest

