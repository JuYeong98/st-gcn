from abc import *
import json
import re

class AbstractConverter(metaclass=ABCMeta):

    def removeObjectAttribute(self,frame):
        frame1 = {key:value for key, value in frame.items() if key != "objects"}
        frame1 = {key:value for key, value in frame1.items() if key != "objects_changed"}
        return frame1

    @abstractmethod
    def remove_useless_in_persons(self,frames):
        pass

    def reduceSkeleton(self, dict):
        for data in dict["data"]:
            if data["skeleton"]:
                for skeleton in data["skeleton"]:
                
                    skeleton["pose"] = list()
                
                    skeleton["score"] = list()

                    for i in range(19):
                        if i in [9,10,11,12,13,14,15,16,17,18]:
                            # print(i)
                            split = list(map(float, skeleton["keypoints"][i].split(",")))
                        
                            skeleton["pose"].append(split[0])
                            skeleton["pose"].append(split[1])
                        
                            skeleton["score"].append(float(skeleton["keypoints_score"][i]))
                        elif i in [0,1,2,3,4,5,6,7]:
                            # print(i)
                            split = list(map(float, skeleton["keypoints"][i].split(",")))
                            skeleton["pose"].append(split[0])
                            skeleton["pose"].append(split[1])
                            
                        
                            skeleton["score"].append(float(skeleton["keypoints_score"][i]))
                        else:
                            pass

                    del skeleton["keypoints"]
                    del skeleton["keypoints_score"]
        return dict

    
    def convert(self,input_path):
        with open(input_path, "rb") as f:
            jsonDict = json.load(f)

        frames = list()
        for frame in jsonDict["frames"]:
            frame = self.removeObjectAttribute(frame)
            frames.append(frame)

        frames = self.remove_useless_in_persons(frames)
        self.new_dict = {"data": frames}
        self.new_dict = self.reduceSkeleton(self.new_dict)
        input_path = input_path.split("/")
        input_path = input_path[-1]
       
        rm = re.sub("[-=_.#/>:$}]","",input_path)
        labels = re.sub("[0-9]","", rm).split("x")
        label_index = re.sub("[a-zA-Z]","", rm)[3]
        
        label = labels[0]

        self.new_dict["label"] = label
        self.new_dict["label_index"] = label_index
        
        
        return self.new_dict
    
    def store(self,output_path):
        with open(output_path, "w") as f:
            json.dump(self.new_dict, f)


