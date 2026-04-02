import re
import copy 

from master_list import library_data
quit_pattern = r"^q(uit)?$"


class SoundStudio:
    def __init__(self):
        self.session_library = copy.deepcopy(library_data)
        self.exclusive_track = {1: None, 2: None, 3: None} #This is where the tracks are recorded
        self.shared_tracks = []


    def get_bounce_status(self, count):
        """Returns the status based on the challenge threshold"""
        if count <= 3: return "Clear"
        if count <= 10: return "Warm"
        if count <= 15: return "Muddy"
        return "Unusable"

    def add_insrument_to_session(self, instrument_key, label=None):
        """
        Create an instance of an instrument.
        Example: add_instrument_to_session("electricguitar", "Lead")    
        """        
        if instrument_key not in library_data:
            print(f"Error: {instrument_key} not found in master library.")
            return
        
        #To create unique instance
        new_instr = copy.deepcopy(library_data[instrument_key])
        new_instr["label"] = label

        # Use label to create a unique key in the session
        unique_name = f"{instrument_key}_{label}" if label else instrument_key
        self.session_library[unique_name] = new_instr
        print(f"Added {unique_name} to new session.")

    def load_present_library(self, data_dict):
        for name, stats in data_dict.items():
            self.session_library[name] = {
                "frequency": stats.get("frequency"),
                "energy": stats.get("energy"),
                "bounce_count": stats.get("bounce_count", 0),
                "volume": stats.get("volume", 5),
                "label": stats.get("label")

            }
