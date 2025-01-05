class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2 + self.data)
        for child in self.children:
            child.display(level + 1)

# Example Usage
root = TreeNode("Project")
phase1 = TreeNode("Phase 1: Planning")
phase2 = TreeNode("Phase 2: Execution")
root.add_child(phase1)
root.add_child(phase2)

task1 = TreeNode("Task 1.1: Site Survey")
task2 = TreeNode("Task 1.2: Budgeting")
phase1.add_child(task1)
phase1.add_child(task2)

root.display()
# Output:
# Project
#   Phase 1: Planning
#     Task 1.1: Site Survey
#     Task 1.2: Budgeting
#   Phase 2: Execution
