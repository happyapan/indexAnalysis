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

    # max_id_sql = """
    #     select max(USER_ID) from `jeff`.`t_users`;
    # """
    # cursor.execute(max_id_sql)
    # search_result = cursor.fetchall()
    # max_id = 0
    #
    # for one in search_result:
    #     max_id = one[0]
    #
    # cursor.close()
    # cursor = cnn.cursor()

    sql_insert = """
        INSERT INTO `jeff`.`t_users`
        (`USER_ID`,
        `USER_NAME`,
        `SEX`,
        `phone`,
        `address`)
        VALUES
        (%d,%s,%d,%s,%s );
    #  """

    data_news=[]
    for i in range(1, 10):
        cursor.execute(sql_insert, (5000 + i, "name" + str(i), 1, "phone" + str(i), "address" + str(i)))


    cnn.commit()
    # sql_query = 'select USER_ID,user_name,phone from t_users;'
    # cursor.execute(sql_query)
    # search_result = cursor.fetchall()
    # for id, name, phone  in search_result:
    #     print(id, name, phone)


except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
