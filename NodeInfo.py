class NodeInfo:
    def __init__(self):
        self._plugIn = None
        self._extraProps = {
            "customClass" : "",
            "isExpanded" : True,
            "memberVarAssignmentType" : 0,
            "memberVarAssignmentName" : "",
        }
        self._animatableProperties = {}
        self._baseValues = {}
        self._customProperties = []
        self._transformStartPosition = (0,0)
        self._displayName = ""
        
def nodeInfoWithPlugIn(pin):
    info = NodeInfo()
    info._plugIn = pin
    return info