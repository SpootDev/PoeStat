class ServerDatabase(object):
    """
    Main database class for server
    """
    from database.db_base import db_open, \
        db_close, \
        db_commit, \
        db_rollback, \
        db_table_index_check, \
        db_table_count, \
        db_query, \
        db_parallel_workers
    from database.db_base_stash import db_stash_insert, \
        db_stash_read_all, \
        db_stash_all_league, \
        db_stash_delete_null_league
    from database.db_base_status import db_status_read,\
        db_status_upsert


    # class variables
    sql_conn = None
    sql_cursor = None
