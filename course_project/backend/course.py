
# from ..repository.dbMysql import Database
# from ..repository import Repository

class CourseRequestManager():
    def __init__(self, db):
        self.db = db
        self.table = "courses"
        # super().__init__(length, length)

    def add(self, data):
        '''
        Input:
            data(dictionary)
        '''
        success = self.db.create(data=data, table=self.table)
        return success

    def modify(self, new_data, course_id):
        '''
        Input:
            new_data(dict)
            course_id(int): the id of the course to be changed
        '''
        # Check whether the section exists
        # Check whether the updated version will run into conflict with other courses
        # Modify
        # success = False
        # if not self.__check_existence(data = new_data):
        criteria = {"courses.course_id":course_id}
        success = self.db.update(new_data=new_data, criteria=criteria, table=self.table )
        return success

    def delete(self, data):
        success = False
        if self.db.delete(criteria=data, table=self.table):
            success = True
        return success

    def read(self, criteria, table):
        '''
        Inputs:
            criteria(dictionary)
        '''
        select = ["courses.course_id", "course_name", "code", "year", "quarter", "descript", "dept"]
        results = self.db.find(select=select, table={"tables": [table]}, criteria=criteria)
        return results

    def __check_existence(self, data, table):
        # Check whether the course already exist 
        # select = "course_id"
        # table = "courses"
        # check_data = {
        #     "dept":data["dept"], 
        #     "course_name":data["course_name"],
        #     "code":data["code"],
        #     "quarter":data["quarter"]
        #     }
        # course_info = self.db.find(select, table, check_data)
        results = self.read(data, table)
        if results.empty:
            return False
        return True



# class Course:
#     '''
#     Course Object
#     '''
#     def __init__(self, data):
#         self.year = data["year"]
#         self.quarter = data["quarter"]
#         self.description = data.get("descript",None)
#         self.name = data["name"]
#         self.code = data["code"]


        
        