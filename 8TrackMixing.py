import re
quit_pattern = r"^q(uit)?$"

instruments = {
    "kickdrum": {
        "frequency": "low",
        "energy": 10,
        "bounce_count": 0
    },
    "snareDrum": {
        "frequency": "mid",
        "energy": 8,
        "bounce_count": 0
    },
    "hiHat": {
        "frequency": "high",
        "energy": 8,
        "bounce_count": 0
    },
    "electricGuitar": {
        "frequency": "mid",
        "energy": 7,
        "bounce_count": 0
    },
    "acousticGuitar": {
        "frequency": "mid",
        "energy": 5,
        "bounce_count": 0
    },
    "12-stringGuitar": {
        "frequency": "mid-high",
        "energy": 6,
        "bounce_count": 0
    },
    "cello": {
        "frequency": "low",
        "energy": 7,
        "bounce_count": 0
    },
    "violin": {
        "frequency": "mid-high",
        "energy": 6,
        "bounce_count": 0
    },
    "bongo": {
        "frequency": "high",
        "energy": 5,
        "bounce_count": 0
    },
    "piano": {
        "frequency": "mid",
        "energy": 8,
        "bounce_count": 0
    },
    "organ": {
        "frequency": "mid",
        "energy": 9,
        "bounce_count": 0
    },
    "saxophone": {
        "frequency": "mid-high",
        "energy": 8,
        "bounce_count": 0
    }
}

#In the future implement GUI 
while True:
    inst_name = input("\nEnter instrument name (or 'quit' to stop: )").strip()

    if re.search(quit_pattern, inst_name, re.IGNORECASE):
        break

    freq = input(f"Freqency: ")
    nrg = int(input(f"Energy: "))

    instruments[inst_name] = {
        "frequency": freq,
        "energy": nrg,
        "bounce_count": 0
    }
    print(f"Added {inst_name} successfully!")


