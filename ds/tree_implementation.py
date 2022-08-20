class TREE:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, data):
        for i in self.children:
            if i == data:
                raise Exception("CHILD ALREADY PRESENT")
        data.parent = self
        self.children.append(data)

    def get_tree_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, parent_type):
        if parent_type == "designation":
            spaces = ' ' * self.get_tree_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if len(self.children) > 0:
                for i in self.children:
                    i.print_tree(parent_type)
        elif parent_type == "name":
            spaces = ' ' * self.get_tree_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name)
            if len(self.children) > 0:
                for i in self.children:
                    i.print_tree(parent_type)
        else:
            spaces = ' ' * self.get_tree_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name + " (" + self.designation + ")")
            if len(self.children) > 0:
                for i in self.children:
                    i.print_tree(parent_type)


def build_electronics_tree():
    root = TREE("Electronics")

    laptop = TREE("Laptop")
    laptop.add_child(TREE("Mac"))
    laptop.add_child(TREE("Surface"))
    laptop.add_child(TREE("Thinkpad"))

    cellphone = TREE("Cell Phone")
    cellphone.add_child(TREE("iPhone"))
    cellphone.add_child(TREE("Google Pixel"))
    cellphone.add_child(TREE("Vivo"))

    tv = TREE("TV")
    tv.add_child(TREE("Samsung"))
    tv.add_child(TREE("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


def build_management_tree():
    root = TREE("Nilupul", "CEO")

    chinmay = TREE("chinmay", "CTO")
    root.add_child(chinmay)

    vishwa = TREE("vishwa", "Infra Structure Head")
    chinmay.add_child(vishwa)
    vishwa.add_child(TREE("Dhaval", "Cloud Manager"))
    vishwa.add_child(TREE("Abhijit", "App Manager"))
    chinmay.add_child(TREE("Aamir", "Application Head"))

    gels = TREE("Gels", "HR HEAD")
    root.add_child(gels)
    gels.add_child(TREE("Peter", "RecruitMent Manager"))
    gels.add_child(TREE("Waqas", "Policy Manager"))

    return root


if __name__ == "__main__":
    # build_electronics_tree()
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
