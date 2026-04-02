"""
This is the hardcoded list of available instruments. 

Like the Beatles, there will be two electric guitars being used one as the lead and another as the rhythm. We will get two copies and name them underneath label
to understand these are seperate instruments being used and not to prevent bouncing twice.

Volume by default if 5. This serves as a hypothetical where the instrument can be changed by the sound engineer to be louder or softer.
Frequency is important as if two low frequency can cause distortions.
Additionally, instruments widen the curve of the vinyl record causing the needle to jump, to prevent this the frequency is often changed. 
Energy is...
bounce_count serves as the amount of times a select instrument moves from track to track. The more the instrument bounces it can go 
from a warm sound to something muddled or eventually unusable. The sound engineer must be careful when moving the the recordings.

For this challenge:
0-3: Clear
4-10: Warm
11-15: Muddy
16+: Unusable

"""


library_data = {
    "kickdrum": {
        "frequency": "low",
        "energy": 10,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "snaredrum": {
        "frequency": "mid",
        "energy": 8,
        "bounce_count": 0,
        "volume": 5,
        "label": None
        
    },
    "hihat": {
        "frequency": "high",
        "energy": 8,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "electricguitar": {
        "frequency": "mid",
        "energy": 7,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "acousticguitar": {
        "frequency": "mid",
        "energy": 5,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "12-stringguitar": {
        "frequency": "mid-high",
        "energy": 6,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "cello": {
        "frequency": "low",
        "energy": 7,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "violin": {
        "frequency": "mid-high",
        "energy": 6,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "bongo": {
        "frequency": "high",
        "energy": 5,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "piano": {
        "frequency": "mid",
        "energy": 8,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "organ": {
        "frequency": "mid",
        "energy": 9,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "saxophone": {
        "frequency": "mid-high",
        "energy": 8,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    },
    "vocals": {
        "frequency": None,
        "energy": None,
        "bounce_count": 0,
        "volume": 5,
        "label": None
    }
}