class Element:
  def __init__(self, location=(0,0,0)):
    self.location = location

  def getX(self): return self.location[0]
  def getY(self): return self.location[1]
  def getZ(self): return self.location[2]

  def moveLeft(self, distance): self.location[0] -= distance
  def moveForward(self, distance): self.location[1] += distance
  def moveUp(self, distance): self.location[2] += distance

class Solid(Element):
  def bounce(self, ray):
    raise "Not Implemented"

  def __str__(self):
    return "<Solid " + str(self.location) + "> "

class Camera(Element):
  def __init__(self, direction=(0,0,0), location=(0,0,0)):
    super().__init__(location)
    self.direction = direction

  def capture(self, size=(10,10), solids=[]):
    x,y = size
    for xpixel in range(x):
      for ypixel in range(y):
        pass

  def __str__(self):
    return "<Camera " + str(self.location) + " -> " + str(self.location) + "> "

class Scene:
  def __init__(self):
    self.solids = []
    self.cameras = []

  def addCamera(self, camera):
    self.cameras.append(camera)

  def addSolid(self, solid):
    self.solids.append(solid)

  def capture(self, size=(10,10), cameraNumber=0):
    self.cameras[cameraNumber].capture(size, self.solids)

  def __str__(self):
    retval = "<Scene "
    for camera in self.cameras:
      retval += str(camera)
    for solid in self.solids:
      retval += str(solid)
    return retval + "> "

if __name__ == "__main__":
  s = Scene()
  c = Camera()
  s.addCamera(c)
  s.addSolid(Solid((0, 10, 0)))
  print(s)
  s.capture()
