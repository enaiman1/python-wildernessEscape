print("Once up a time...")
######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

print(story_root.story_piece)

######
# VARIABLES FOR TREE
######

######
# TESTING AREA
######
