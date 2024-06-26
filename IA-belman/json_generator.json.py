import json

matrix = True
if matrix:
    data = {
        "final": 22,
        "p_on": {
            "16.0": {
                "16.0": 0.3,
                "16.5": 0.5,
                "17.0": 0.2,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "16.5": {
                "16.0": 0.1,
                "16.5": 0.2,
                "17.0": 0.5,
                "17.5": 0.2,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "17.0": {
                "16.0": 0.0,
                "16.5": 0.1,
                "17.0": 0.2,
                "17.5": 0.5,
                "18.0": 0.2,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "17.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.1,
                "17.5": 0.2,
                "18.0": 0.5,
                "18.5": 0.2,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "18.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.1,
                "18.0": 0.2,
                "18.5": 0.5,
                "19.0": 0.2,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "18.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.1,
                "18.5": 0.2,
                "19.0": 0.5,
                "19.5": 0.2,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "19.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.1,
                "19.0": 0.2,
                "19.5": 0.5,
                "20.0": 0.2,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "19.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.1,
                "19.5": 0.2,
                "20.0": 0.5,
                "20.5": 0.2,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "20.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.1,
                "20.0": 0.2,
                "20.5": 0.5,
                "21.0": 0.2,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "20.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.1,
                "20.5": 0.2,
                "21.0": 0.5,
                "21.5": 0.2,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "21.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.1,
                "21.0": 0.2,
                "21.5": 0.5,
                "22.0": 0.2,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "21.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.1,
                "21.5": 0.2,
                "22.0": 0.5,
                "22.5": 0.2,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "22.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.1,
                "22.0": 0.2,
                "22.5": 0.5,
                "23.0": 0.2,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "22.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.1,
                "22.5": 0.2,
                "23.0": 0.5,
                "23.5": 0.2,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "23.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.1,
                "23.0": 0.2,
                "23.5": 0.5,
                "24.0": 0.2,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "23.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.1,
                "23.5": 0.2,
                "24.0": 0.5,
                "24.5": 0.2,
                "25.0": 0.0
            },
            "24.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.1,
                "24.0": 0.2,
                "24.5": 0.5,
                "25.0": 0.2
            },
            "24.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.1,
                "24.5": 0.2,
                "25.0": 0.7
            },
            "25.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.1,
                "25.0": 0.9
            }
        },
        "p_off": {
            "16.0": {
                "16.0": 0.9,
                "16.5": 0.1,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "16.5": {
                "16.0": 0.7,
                "16.5": 0.2,
                "17.0": 0.1,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "17.0": {
                "16.0": 0.0,
                "16.5": 0.7,
                "17.0": 0.2,
                "17.5": 0.1,
                "18.0": 0.2,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "17.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.7,
                "17.5": 0.2,
                "18.0": 0.1,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "18.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.7,
                "18.0": 0.2,
                "18.5": 0.1,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "18.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.7,
                "18.5": 0.2,
                "19.0": 0.1,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "19.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.7,
                "19.0": 0.2,
                "19.5": 0.1,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "19.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.7,
                "19.5": 0.2,
                "20.0": 0.1,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "20.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.7,
                "20.0": 0.2,
                "20.5": 0.1,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "20.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.7,
                "20.5": 0.2,
                "21.0": 0.1,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "21.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.7,
                "21.0": 0.2,
                "21.5": 0.1,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "21.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.7,
                "21.5": 0.2,
                "22.0": 0.1,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "22.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.7,
                "22.0": 0.2,
                "22.5": 0.1,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "22.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.7,
                "22.5": 0.2,
                "23.0": 0.1,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "23.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.7,
                "23.0": 0.2,
                "23.5": 0.1,
                "24.0": 0.0,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "23.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.7,
                "23.5": 0.2,
                "24.0": 0.1,
                "24.5": 0.0,
                "25.0": 0.0
            },
            "24.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.7,
                "24.0": 0.2,
                "24.5": 0.1,
                "25.0": 0.0
            },
            "24.5": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.7,
                "24.5": 0.2,
                "25.0": 0.1
            },
            "25.0": {
                "16.0": 0.0,
                "16.5": 0.0,
                "17.0": 0.0,
                "17.5": 0.0,
                "18.0": 0.0,
                "18.5": 0.0,
                "19.0": 0.0,
                "19.5": 0.0,
                "20.0": 0.0,
                "20.5": 0.0,
                "21.0": 0.0,
                "21.5": 0.0,
                "22.0": 0.0,
                "22.5": 0.0,
                "23.0": 0.0,
                "23.5": 0.0,
                "24.0": 0.0,
                "24.5": 0.7,
                "25.0": 0.3
            }
        },
        "max_it": 1000,
        "tolerance": 0.001,
        "coste_on": 5,
        "coste_off": 1
    }
else:
    data = {
        "final": 22,
        "p_on": {
            "16.0": {"s": 0.3, "up1": 0.2, "up0.5": 0.5, "down": 0.0},
            "16.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "17.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "17.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "18.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "18.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "19.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "19.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "20.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "20.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "21.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "21.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "22.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "22.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "23.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "23.5": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "24.0": {"s": 0.1, "up1": 0.2, "up0.5": 0.5, "down": 0.1},
            "24.5": {"s": 0.2, "up1": 0.0, "up0.5": 0.7, "down": 0.1},
            "25.0": {"s": 0.9, "up1": 0.0, "up0.5": 0.0, "down": 0.1}
        },
        "p_off": {
            "16.0": {"s": 0.9, "up0.5": 0.1, "down": 0.0},
            "16.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "17.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "17.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "18.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "18.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "19.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "19.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "20.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "20.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "21.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "21.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "22.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "22.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "23.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "23.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "24.0": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "24.5": {"s": 0.2, "up0.5": 0.1, "down": 0.7},
            "25.0": {"s": 0.3, "up0.5": 0.0, "down": 0.7}
        },
        "max_it": 1000,
        "tolerance": 0.001,
        "coste_on": 5,
        "coste_off": 1
    }

with open("input-matrix.json", 'w') as file:
    json.dump(data, file, indent=2)
