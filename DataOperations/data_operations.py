from enum import Enum
class OperationType(Enum):
    Add = 1
    Update = 2
    Delete = 3

class OperationInfo:
    def __init__(self, type, data):
        self.type = type
        self.data = data
    
    def __str__(self):
        return "(" +  str(self.type) + ", " + str(self.data) + ")"

def undo(object, list):
    if object.type == OperationType.Delete:
        list.append(OperationInfo(OperationType.Add, object.data))
    elif object.type == OperationType.Add:
        list.append(OperationInfo(OperationType.Delete, object.data))
    elif object.type == OperationType.Update: # Nær bara í fyrsta case-ið af þessu object, þannig ekki alvöru undo
        for parser in list:
            for key in parser.data:
                for k in object.data:
                    if k == key:
                        list.append(OperationInfo(OperationType.Update,parser.data))
                        return    

if __name__ == "__main__":
    print('Testing Opertions')
    stack = []
    info = OperationInfo(OperationType.Add, {'id':11})
    stack.append(info)
    info = OperationInfo(OperationType.Add, {'race_time':300})
    stack.append(info)
    info = OperationInfo(OperationType.Update, {'race_time':337})
    stack.append(info)
    info = OperationInfo(OperationType.Update, {'race_time':307})
    stack.append(info)

    for object in stack:
        print(object)
    
    print("")
    some_info = stack.pop()
    undo(some_info, stack)

    for object in stack:
        print(object)
    