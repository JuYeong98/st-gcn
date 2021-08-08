
from .AbstractConverter import AbstractConverter

class GeneralConverter(AbstractConverter):


    def remove_useless_in_persons(self, frames):
        for frame in frames:
            if frame["persons"]:    
                for idx, person in enumerate(frame["persons"]):
                    person2 = {key:value for key, value in person.items() if key!="memo"}
                    person2 = {key : value for key, value in person2.items() if key != "person_index"} 
                    frame["persons"][idx] = person2
            frame["skeleton"] = frame["persons"]
            del frame["persons"]
        return frames


class FightingConverter(AbstractConverter):
    def remove_useless_in_persons(self, frames):
        for frame in frames:
            if frame["persons"]:
                for idx, person in enumerate(frame["persons"]):
                    person2 = {key: value for key, value in person.items() if key != "memo"}
                    person2 = {key: value for key, value in person2.items() if key != "person_index"}
                    person2 = {key: value for key, value in person2.items() if key != "keypoints_movement"}
                    person2 = {key: value for key, value in person2.items() if key != "keypoints_angle"}
                    person2 = {key: value for key, value in person2.items() if key != "person_center"}

                    frame["persons"][idx] = person2
            frame["skeleton"] = frame["persons"]
            del frame["persons"]
        return frames



