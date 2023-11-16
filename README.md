How to run

Set up the virtual env

```
python3 -m venv virtual_env

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

ENV variables

```
ATLAS_URI=hek
DB_NAME=
```

Api docs on

```
localhost:8000/docs
```
