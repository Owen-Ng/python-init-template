from sortedcontainers import SortedList
import requests
from controller.key_value_version import KeyValueVersionController
from utils.str_utils import RemoveTrailingNewLine
def main():
    arg = input("Input file Path\n")
    req = []
    with open(arg, "r") as rf:
        for line in rf.readlines():
            req.append(RemoveTrailingNewLine(line))

    response = []

    keyValueVersionController = KeyValueVersionController()

    for query in req:
        query_split = query.split(" ")

        if len(query_split) == 3: # GET with version or PUT
            op, key, additional = query_split

            if op == "GET": 
                version, value = keyValueVersionController.Get(key, int(additional))
                txt = "GET {key}(#{version}) = {value}"
                formatted_output = txt.format(key=key,version =additional,value =value)# "GET " + key + "(#" + additional + ") = " + value
                response.append(formatted_output)
            elif op == "PUT":
                raw_output = keyValueVersionController.Put(key, additional)
                txt = "PUT(#{version}) {key} = {value}"
                formatted_output = txt.format(version = raw_output, key = key, value = additional) #"PUT(#" + str(raw_output) + ") "+ key + " = "+ str(additional) 
                response.append(formatted_output)
            else:
                response.append("Error input incorrect")
            
        elif len(query_split) == 2: # GET lastest
            op, key = query_split

            if op == "GET":
                raw_output =  keyValueVersionController.GetLatest(key)
                txt = "GET {key} = {value}"
                formatted_output = txt.format(key = key, value = raw_output) # "GET "+ key + " = " + raw_output
                response.append(formatted_output)
            else:
                response.append("Error input incorrect")

        else:
            response.append("Error input incorrect")

    for resp in response:
        print(resp)

    return "\n".join(response)
if __name__ == '__main__':
    main()