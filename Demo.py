import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1q2w3e4r',
    'port': 3306,
    'database': 'jeff',
    'charset': 'utf8'
}
cnn = mysql.connector.connect(**config)
cursor = cnn.cursor()
try:

    # sql_insert = """
    #     INSERT INTO `jeff`.`t_users`
    #     (`USER_ID`,
    #     `USER_NAME`,
    #     `SEX`,
    #     `phone`,
    #     `address`)
    #     VALUES
    #     ('%d','%s','%d','%s','%s' );
    # #  """
    # for i in range(10):
    #     cursor.execute(sql_insert % (3000 + i, "name" + str(i), 1, "phone" + str(i), "address" + str(i)))

    sql_query = 'select USER_ID,user_name,phone from t_users;'
    cursor.execute(sql_query)
    search_result = cursor.fetchall()
    for id, name, phone in search_result:
        print(id, name, phone)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:

    cursor.close()
    cnn.close()
