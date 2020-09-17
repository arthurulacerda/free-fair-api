mysql = {'host': 'localhost',
         'user': 'dbuser',
         'passwd': 'DBpassword_1234',
         'db': 'db_fair'}

mysqlConfig = "mysql://{}:{}@{}:3306/{}".format(mysql['user'], mysql['passwd'], mysql['host'], mysql['db'])
