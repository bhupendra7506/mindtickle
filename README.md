Setup python3.8 version and run below command 
pip3 install -r requirement.txt

to run the test execute :
locust -f workflow/serviceLoadTestWorkflows/authorServiceLoadTest.py

once the server is started : 
> Go to http://0.0.0.0:8089
> provide users = 100 
> provide Spawn rate as 1 sec
> provide host as "https://fakerestapi.azurewebsites.net/index.html"
> click on advance option and provide runtime as 20 sec 

test will complete and the report will be generated at http://0.0.0.0:8089