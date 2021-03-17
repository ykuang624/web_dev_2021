
from course import CourseRequestManager

class SectionRequestManager:

    def __init__(self, db):
        self.db = db
        self.table = "sections"

    def add(self, data):
        '''
        Input:
            data(dictionary)
        '''
        success = False
        message = "Not able to create the course due to database issue"


        # Find ok rooms
        room_ids = find_room(data["max_enrollment"], data[""])
        if room_ids:
            for room_id in room_ids:
                try:
                    data["room_id"] = room_id
                    success = self.db.create(data=data, table=self.table)
                    if success:
                        message = "Section successfully created"

                        break
                except: 
                    continue
        else:
            message="No rooms available"

        return (success, message)
                        
                
    def find_room(self, max_enrollment, day_data, time_id):
        '''
        Input:
            capactiy(int): max enrollment number
        Output:
            room_id(int)
        '''
        # Select all rooms that satisfy the room requirement
        rooms = self.db.find(select=["room_id"], table="rooms", criteria={"capacity":{"operator":">=", "arg":max_enrollment}})
        rooms_ids = [room["room_id"] for room in rooms]
        return room_ids
        

    def modify(self, new_data, section_id):
        '''
        Input:
            new_data(dict)
            section_id(int): the id of the section to be changed
        '''
        # Modify
        success = False
        criteria = {"section_id":section_id}
        success = self.db.update(new_data=new_data, criteria=criteria, table=self.table)
        return success

    def delete(self, data, course_id):
        # I can only delete a section that has less than 5 students or no instructor
        success  = False
        message = ""
         # Check on students number
        student_results = self.db.find(select=["COUNT(student_id)"], from_tables={"tables":"student_section"}, criteria={"section_id":data["section_id"]},limit=["GROUPBY section_id HAVING COUNT(student_id) >= 5"])
        if student_results:
            message = "Students over 5, cannot delete"
        else: 
            #Check on instructor availability
            instructor_result =  self.db.find(select=["instructor_id"], from_table={"tables":self.table}, criteria={"section_id":data["section_id"]})
            if not instructor_result[0]["instructor_id"]:
                if self.db.delete(criteria = data, table = self.table):
                    success =  True
                    message = "deleted the section successfully"
                    #DON"t forget to delete course if all sections are gone
                    section_results = self.db.find(select = ["sections.course_id"], from_table={"tables":self.table})
                    if not instructor_result[0]["sections.course_id"]:
                        course_manager = CourseRequestManager(self.db)
                        course_manager.delete(criteria={"sections.course_id":course_id})
            else:
                message="professor available, cannot delete"
        return (success, message)

    def read(self, criteria):
        '''
        Inputs:
            criteria(dictionary)
        '''
        select= [" * "]
        tables = ["courses",self.table, "instructors", "rooms"]
        ons = ["courses.course_id=sections.course_id", "sections.instructor_id = instructors.instructor_id", "sections.room_id=rooms.room_id"]
        results = self.db.find(select=select, from_tables={"tables":tables, "ons":ons}, criteria=criteria, limit=None)
        return results



    def __check_existence(cls, data):
        '''
        Output:
            Boolean: return true if doesn't exist, false if exists
        '''
        results = self.read(data)
        if results.empty:
            return False
        return True



    