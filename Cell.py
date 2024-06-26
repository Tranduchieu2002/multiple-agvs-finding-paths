class Cell:
  def __init__(self, STATUS: int = 0):
    self.parent_i = 0  # Parent cell's row index
    self.parent_j = 0  # Parent cell's column index
    self.f = float('inf')  # Total cost of the cell (g + h)
    self.g = float('inf')  # Cost from start to this cell
    self.h = 0  # Heuristic cost from this cell to destination
    self.status = STATUS  # 0: blocked, 1: Open, 2: Closed, 3: Blocked
    self.agv = None
    self.isChargingStation = False
    self.isStore = False
    self.isDepot = False
    self.isObstacle = False
  def __str__(self) -> str:
    return f"Cell: {self.status}"