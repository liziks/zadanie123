import sqlite3

import config
import function

def main():
    while True:
        act = input("Введите : ")
        if act == "parse":
            if config.logs:
                
                conn = sqlite3.connect(config.db_name)
                cursor = conn.cursor()
                function.del_table(cursor)
                for log_line in config.logs.split('\n'):
                    log_data = function.analyze_log_line(log_line)
                    if log_data:
                        function.insert_to_db(cursor, log_data)
                
                conn.commit()
                conn.close()
                print("Выполнено успешно")
            else:
                print("Не удалось выполнить")
        else:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()
            filters = act.split()
            all_data = function.get_from_db(cursor, config.table_name)
            filtered_data = function.filt_data(all_data, filters)
            for row in filtered_data:
                print(row)
            conn.commit()
            conn.close()

    
    
if __name__ == "__main__":
    main()
