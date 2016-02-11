
kCCBSizeTypeAbsolute = 0
kCCBSizeTypePercent = 1
kCCBSizeTypeRelativeContainer = 2
kCCBSizeTypeHorizontalPercent = 3
kCCBSizeTypeVerticalPercent = 4
kCCBSizeTypeMultiplyResolution = 5

def setPosition(pos, ntype, node, prop, parentSize):
    absPos = calcAbsolutePositionFromRelative(pos, ntype, parentSize)
    
    # Set the position value
    # TODO:@twenty0ne
    node.position = pos
    
def calcAbsolutePositionFromRelative(pos, ntype, parentSize):
    pass

def setSize(size, ntype, node, prop, parentSize):
    # Calculate absolute size
    absSize = (0,0)
    
    if ntype == kCCBSizeTypeAbsolute:
        absSize = size
    elif ntype == kCCBSizeTypePercent:
        absSize = (size[0] * 0.01 * parentSize[0], 
                   size[1] * 0.01 * parentSize[1])
    elif ntype == kCCBSizeTypeRelativeContainer:
        absSize = (parentSize[0] - size[0],
                   parentSize[1] - size[1])
    elif ntype == kCCBSizeTypeHorizontalPercent:
        absSize = (size[0] * 0.01 * parentSize[0], size[1])
    elif ntype == kCCBSizeTypeVerticalPercent:
        absSize = (size[0], size[1] * 0.01 * parentSize[1])
    elif ntype == kCCBSizeTypeMultiplyResolution:
        assert(0)
    
    # Set the size value
    # TODO:@twenty0ne
    