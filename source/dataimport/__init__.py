class ServerImport(object):
    """
    Main database class for server data import
    """
    from dataimport.import_base_items import import_base_items

    def __init__(self, db_connection):
        self.db_connection = db_connection
