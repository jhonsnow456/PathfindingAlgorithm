from Classes.Color import color
from pygame import draw

class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = color.Color.WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == color.Color.RED

	def is_open(self):
		return self.color == color.Color.GREEN

	def is_barrier(self):
		return self.color == color.Color.BLACK

	def is_start(self):
		return self.color == color.Color.ORANGE

	def is_end(self):
		return self.color == color.Color.TORQUISE

	def reset(self):
		self.color = color.Color.WHITE

	def make_start(self):
		self.color = color.Color.ORANGE

	def make_closed(self):
		self.color = color.Color.RED

	def make_open(self):
		self.color = color.Color.GREEN

	def make_barrier(self):
		self.color = color.Color.BLACK

	def make_end(self):
		self.color = color.Color.TORQUISE

	def make_path(self):
		self.color = color.Color.PURPLE

	def draw(self, win):
		draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False