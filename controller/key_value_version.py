import bisect
class KeyValueVersionController:
    def __init__(self):
        self.version = 1
        self.keyValueMap = {}

    # Input: key
    # output: latest_value
    def GetLatest(self, key: str) -> str:
        if key not in self.keyValueMap:
            return "<NULL>"
        return self.keyValueMap[key][-1][-1]

    # input: key version
    # output: version, value
    def Get(self, key : str, version : str) -> tuple[int, str]:
        if key not in self.keyValueMap:
            return -1,"<NULL>"
        index_high_value = bisect.bisect_right(self.keyValueMap[key], version, key = lambda x : x[0])
        if index_high_value == 0:
            return -1,"<NULL>"
        version_and_value =  self.keyValueMap[key][index_high_value - 1]
        
        return version_and_value[0], version_and_value[1]

    # input: key, value
    # output: version
    def Put(self, key: str, value : str) -> int:
        if key not in self.keyValueMap:
            self.keyValueMap[key] = []
        self.keyValueMap[key].append([self.version,value])
        integrated_version = self.version
        self.version += 1

        return integrated_version
        


    