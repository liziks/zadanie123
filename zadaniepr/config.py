import function

url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"
format = r'(?P<host>\S+) (?P<identity>\S+) (?P<user>\S+) \[(?P<time>.+?)\] "(?P<request>.+?)" (?P<status>\d{3}) (?P<size>\S+)'
logs = function.adoption_logs(url)
db_name = 'apache_logs.db'
table_name = 'apache_logs'