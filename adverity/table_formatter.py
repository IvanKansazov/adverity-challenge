import petl as etl


class TableFormatter:
    def __init__(self, table_obj, max_rows=None):
        self.table = table_obj
        self.max_rows = max_rows

    def format(self):
        self.remove_columns()
        self.table = etl.rowslice(self.table, self.max_rows)
        return self.table

    def remove_columns(self):
        required_columns = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
                            'gender',
                            'homeworld', 'edited']
        self.table = etl.cut(self.table, required_columns)
