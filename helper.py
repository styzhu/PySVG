import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# https://www.w3schools.com/graphics/svg_intro.asp
class StyBBox:
    def __init__(self, i_x=0, i_y=0, i_width=0, i_height=0):
        self.bbox = ((i_x,i_y), (i_x+i_width, i_y+i_height))
        self.center = ((i_x + i_width/2), (i_y + i_height/2))

    def bbox(self):
        return self.bbox

    def center(self):
        return self.center

class StyShape:
    def id(self, i_id):
        self.id = i_id

class StyRect(StyShape):
    def __init__(self, elt=None):
        self.id = hex(id(self))
        if elt is not None:
            self.id = elt.get('id', self.id)
            self.setBBox(elt)
            self.setStrokeFill(elt)
        StyShape.__init__(self.id)

    def setBBox(self, elt):
        self.x = elt.get('x', 0)
        self.y = elt.get('y', 0)
        self.width = elt.get('width')
        self.height = elt.get('height')
        assert self.width is not None
        self.bbox = StyBBox(self.x, self.y, self.width, self.height)

    def bbox(self):
        return self.bbox
