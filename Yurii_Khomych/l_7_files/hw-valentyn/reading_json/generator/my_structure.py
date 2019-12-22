class MyStructure:
    def __init__(self, loop_name, source_column, dest_column, node_dict, *args, **kwargs):
        try:
            self.loop = loop_name
            self.source_column = source_column
            self.dest_column = dest_column
            self.name = node_dict['name']
            self.sourcing = node_dict['sourcing']
        except KeyError:
            self.sourcing = ''

    def get_name(self):
        return self.name

    def get_sourcing(self):
        if self.sourcing:
            a = self.source_column + "|" + self.dest_column + "|" + self.loop + '/' + self.name + ":" + self.sourcing[
                "location"]
            return a
        return False
