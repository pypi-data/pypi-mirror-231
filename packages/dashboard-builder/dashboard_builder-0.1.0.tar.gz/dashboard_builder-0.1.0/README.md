# Dashboard Builder



## Local Dev Notes

Using poetry for managing dependencies and deploying. On my local machine also using pyenv for python version controll manager. So start up the remote 
environment, can do the following:

1. Set the python version - currently 3.10 for this project: `pyenv global 3.10.0`
2. Tell poetry to use that: `poetry env use $(pyenv which python)` 
3. Then can add things, e.g., `poetry add requests` 

Once done there, can then generate the requirements.txt file with:
```bash poetry export --output requirements.txt```

For publishing: 
1. Package the updates: ```bash poetry build``` 
2. Once it has finished packing, can run ```bash poetry publish``` to get the latest/greatest version on pypi 
