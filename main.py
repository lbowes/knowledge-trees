from treelib import Tree


def main():
	arg = load_argument()
	o = compress(arg, 0.5)
	print(o)


def load_argument() -> Tree:
	# todo: this won't be hardcoded
	arg = Tree()

	arg.create_node("The main conclusion of the argument.", "conclusion")  # root node
	arg.create_node("Some supporting premise", "p1", parent="conclusion")
	arg.create_node("An example", "ex1", parent="p1")
	arg.create_node("Another supporting premise", "p2", parent="conclusion")

	return arg


def compress(arg: Tree, level: float) -> str:
	"""Compress a written argument to a subset of the points in the original"""
	compression = "todo"

	# todo: outline argument given a compression level

	return compression


if __name__ == '__main__':
	main()