# Toy Robot with FastAPI

This is a Toy Robot server that allows users to place a toy on a table and move, turn and get the current location
of the toy on the table. Only one toy is allowed to be placed at a time and to be moved. No actions will occur if
no toy is placed on the table.

If the toy is moving beyond the table dimension, it will simply stay in its current place. Turning the toy will change
its location on the table.

Table Dimensions
X [0-10]
Y [0-10]

## Modules Used

- FastAPI
- Pydantic
- HttpX
- Pytest
- Uvicorn

## Steps to Run

1. **Clone the repository:**
git clone https://github.com/kingcobra1325/toy-robot-api


3. **Install the required dependencies:**
pip install -r requirements.txt


4. **Run the FastAPI server via Uvicorn:**
uvicorn api:app --reload


5. **Perform actions to the toy by accessing the following URLs.**

- POST `\place\`
```bash
curl -X POST "http://127.0.0.1:8000/place/" -H "Content-Type: application/json" -d '{"x": 3, "y": 4, "face": "NORTH"}'
```

This will place the toy within the table. Upon a successful request, you should receive a response in the following format:
`{
  "x": 3,
  "y": 4,
  "face": "north",
}`

- POST `\move\`
```bash
curl -X POST "http://127.0.0.1:8000/move/" -H "Content-Type: application/json"
```

This will move the toy one place forward. Will stay in place if it has reached the edge of the table.
Does no action when no toy is placed.


- POST `\left\`
```bash
curl -X POST "http://127.0.0.1:8000/left/" -H "Content-Type: application/json"
```

Will turn the toy to its left once. It will not move the toy's location.
Does no action when no toy is placed.


- POST `\right\`
```bash
curl -X POST "http://127.0.0.1:8000/right/" -H "Content-Type: application/json"
```

Will turn the toy to its right once. It will not move the toy's location.
Does no action when no toy is placed.


- GET `\report\`
```bash
curl -X GET "http://127.0.0.1:8000/report/" -H "Content-Type: application/json"
```

Fetch the toy's current location details.
Returns an empty dict when no toy is placed.



## Caveats

- Ensure that you have Python and pip installed on your system.
- The application relies on external libraries (`fastapi`, `uvicorn` and `pytest`), so ensure they are installed.
- This application may not work correctly if the specified URL is invalid or inaccessible.

## Test Cases

- PLACE Negative X Error
- PLACE Negative Y Error
- PLACE Over the X Table limit Error
- PLACE Over the Y Table limit Error
- PLACE Invalid Face Error
- PLACE Successful
- MOVE No toy placed
- MOVE Successful
- MOVE Inplace Successful
- TURN LEFT No toy placed
- TURN LEFT Successful
- TURN RIGHT No toy placed
- TURN RIGHT Successful
- REPORT No toy placed
- REPORT Successful