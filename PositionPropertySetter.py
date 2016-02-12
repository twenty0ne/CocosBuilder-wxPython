# kCCBPosition
kCCBPositionTypeRelativeBottomLeft = 0
kCCBPositionTypeRelativeTopLeft = 1
kCCBPositionTypeRelativeTopRight = 2
kCCBPositionTypeRelativeBottomRight = 3
kCCBPositionTypePercent = 4
kCCBPositionTypeMultiplyResolution = 5

# kCCBSizeType
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
    node.position = absPos
    
def calcAbsolutePositionFromRelative(pos, ntype, parentSize):
    absPos = (0,0)
    
    if ntype == kCCBPositionTypePercent:
        # TODO:@twenty0ne
        # roundf
        absPos = (pos[0] * parentSize[0] * 0.01, pos[1] * parentSize[1] * 0.01)
    elif ntype == kCCBPositionTypeRelativeBottomLeft:
        absPos = pos
    elif ntype == kCCBPositionTypeRelativeTopLeft:
        absPos = (pos[0], parentSize[1] - pos[1])
    elif ntype == kCCBPositionTypeRelativeTopRight:
        absPos = (parentSize[0] - pos[0], parentSize[1] - pos[1])
    elif ntype == kCCBPositionTypeRelativeBottomRight:
        absPos = (parentSize[0] - pos[0], pos[1])
    elif ntype == kCCBPositionTypeMultiplyResolution:
        assert(0)
    
    return absPos

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
    