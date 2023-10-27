How to run

Set up the virtual env
```
ptyhon3 -m venv virtual_env

source virtual_env/bin/activate
```

Install fastapi
```
pip3 install -r requirements.txt
```

Start server
```
uvicorn main:app --reload
```

https://fastapi.tiangolo.com/tutorial/first-steps/