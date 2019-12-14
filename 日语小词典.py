from pymysql import connect


class operation:
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="", database="Japan")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def find_word(self):
        key_word = input("关键字:")
        sql = """select * from word where spelling rlike "%s" or words rlike "%s" """ % (key_word, key_word)
        number = self.cursor.execute(sql)
        if number:
            for temp in self.cursor.fetchall():
                print(temp)
        else:
            print("没有喔")

    def find_meaning(self):
        key_word = input("关键字:")
        sql = """select * from word where meaning rlike "%s"  """ % key_word
        number = self.cursor.execute(sql)
        if number:
            for temp in self.cursor.fetchall():
                print(temp)
        else:
            print("找不到哟")

    def find_all(self):
        sql = """select * from word"""
        self.find_tail(sql)

    def find_tail(self, sql):
        self.execute_sql(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def appear_word(self):
        sql = """select words from word"""
        self.find_tail(sql)
        reply = input("are you finish？")
        if reply == "y":
            sql = """select words,spelling from word """
            self.find_tail(sql)

    def run(self):
        while True:
            print("1. 读音查单词")
            print("2. 意思查单词")
            print("3. 所有单词")
            print("4. 出单词")
            num = input("功能:")
            if num == "1":
                self.find_word()
            elif num == "2":
                self.find_meaning()
            elif num == "3":
                self.find_all()
            elif num == "4":
                self.appear_word()
            else:
                print("到底啦")


def main():
    """插入"""
    op = operation()
    op.run()


if __name__ == "__main__":
    main()
