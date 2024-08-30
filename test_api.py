from fastapi.testclient import TestClient
from api import app, toy_db
from copy import deepcopy

client = TestClient(app)

########## PLACE
############################################


def test_place_negative_x_error():
    response = client.post(
        "/place/",
        json={
            "x": -1,
            "y": 5,
            "face": "NORTH",
        },
    )
    # Check error response
    assert response.status_code == 422

    # Check no changes on toy db
    assert not toy_db.details


def test_place_negative_y_error():
    response = client.post(
        "/place/",
        json={
            "x": 5,
            "y": -1,
            "face": "NORTH",
        },
    )
    # Check error response
    assert response.status_code == 422

    # Check no changes on toy db
    assert not toy_db.details


def test_place_over_max_limit_x_error():
    response = client.post(
        "/place/",
        json={
            "x": 16,
            "y": 5,
            "face": "NORTH",
        },
    )
    # Check error response
    assert response.status_code == 422

    # Check no changes on toy db
    assert not toy_db.details


def test_place_over_max_limit_y_error():
    response = client.post(
        "/place/",
        json={
            "x": 5,
            "y": 11,
            "face": "NORTH",
        },
    )
    # Check error response
    assert response.status_code == 422

    # Check no changes on toy db
    assert not toy_db.details


def test_place_invalid_face_error():
    response = client.post(
        "/place/",
        json={
            "x": 4,
            "y": 5,
            "face": "WRONGFACE",
        },
    )
    # Check error response
    assert response.status_code == 422

    # Check no changes on toy db
    assert not toy_db.details


def test_place_success():
    for face in ("NORTH", "SOUTH", "EAST", "WEST"):
        response = client.post(
            "/place/",
            json={
                "x": 4,
                "y": 5,
                "face": face,
            },
        )
        # Check successful response
        assert response.status_code == 200

        # Check db is working
        assert toy_db.details == {"x": 4, "y": 5, "face": face.lower()}


########## MOVE
############################################


def test_move_no_toy_placed():
    toy_db.details = {}

    response = client.post("/move/")
    # Check successful response
    assert response.status_code == 200

    # Check no changes on toy db
    assert not toy_db.details


def test_move_success():
    for face, updated_coord in (
        ("NORTH", {"y": 4}),
        ("SOUTH", {"y": 2}),
        ("EAST", {"x": 4}),
        ("WEST", {"x": 2}),
    ):
        toy_db.details = {"x": 3, "y": 3, "face": face.lower()}
        correct_result = deepcopy(toy_db.details)

        correct_result.update(updated_coord)

        response = client.post("/move/")
        # Check successful response
        assert response.status_code == 200

        # Check db is correctly updated
        assert toy_db.details == correct_result

def test_move_inplace_success():
    for face, border_coord, in (
        ("NORTH", {"y": 5}),
        ("SOUTH", {"y": 0}),
        ("EAST", {"x": 5}),
        ("WEST", {"x": 0}),
    ):
        original_coordinates = {"x": 5, "y": 5, "face": face.lower()}.update(border_coord)

        toy_db.details = deepcopy(original_coordinates)

        response = client.post("/move/")
        # Check successful response
        assert response.status_code == 200

        # Check toy hasn't moved
        assert toy_db.details == original_coordinates

########## TURN LEFT
############################################


def test_turn_left_no_toy_placed():
    toy_db.details = {}

    response = client.post("/left/")
    # Check successful response
    assert response.status_code == 200

    # Check no changes on toy db
    assert not toy_db.details


def test_turn_left_success():
    for face, new_face in (
        ("NORTH", "WEST"),
        ("SOUTH", "EAST"),
        ("EAST", "NORTH"),
        ("WEST", "SOUTH"),
    ):
        toy_db.details = {"x": 3, "y": 3, "face": face.lower()}
        correct_result = deepcopy(toy_db.details)

        correct_result["face"] = new_face.lower()

        response = client.post("/left/")
        # Check successful response
        assert response.status_code == 200

        # Check toy turned left without moving
        assert toy_db.details == correct_result

########## TURN RIGHT
############################################


def test_turn_right_no_toy_placed():
    toy_db.details = {}

    response = client.post("/right/")
    # Check successful response
    assert response.status_code == 200

    # Check no changes on toy db
    assert not toy_db.details


def test_turn_right_success():
    for face, new_face in (
        ("NORTH", "EAST"),
        ("SOUTH", "WEST"),
        ("EAST", "SOUTH"),
        ("WEST", "NORTH"),
    ):
        toy_db.details = {"x": 3, "y": 3, "face": face.lower()}
        correct_result = deepcopy(toy_db.details)

        correct_result["face"] = new_face.lower()

        response = client.post("/right/")
        # Check successful response
        assert response.status_code == 200

        # Check toy turned left without moving
        assert toy_db.details == correct_result


########## REPORT
############################################


def test_report_no_toy_placed():
    toy_db.details = {}

    response = client.get("/report/")
    # Check successful response
    assert response.status_code == 200

    # Check empty toy data returned
    assert not response.json()


def test_report_success():
    toy_db.details = {
        "x": 4,
        "y": 5,
        "face": "NORTH",
    }

    response = client.get("/report/")
    # Check successful response
    assert response.status_code == 200

    # Check the toy details are returned correctly
    assert response.json() == {
        "x": 4,
        "y": 5,
        "face": "north",
    }