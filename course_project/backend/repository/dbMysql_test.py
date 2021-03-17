from dbMysql import Database


class DataBaseTest():
    @staticmethod
    def testCreate(db):
        # Create Course
        data = {"course_name":"HOW TO LALA CODE", "code":"001","year":2021,"quarter":"Spring", "descript":"a course teaching you to be smart and avoid coding forever."}
        table = "courses"
        expected = False
        if expected == db.create(data, table):
            print("PASSED: CreateCourse")
        else:
            print("FAILED: Create Course")

    @staticmethod
    def testWhereQuery(db):
        criteria = {"division": ["Physics", "Art"], "instructor": "Balman", "day": ["MWF"]}
        query, args = db.build_where(criteria)
        print(query, args)

    @staticmethod
    def testFind(db):
        select = ["name"]

        def find(self, select, table, criteria):
            pass


if __name__ == "__main__":
    new_db = Database()
    DataBaseTest.testCreate(new_db)
    DataBaseTest.testWhereQuery(new_db)