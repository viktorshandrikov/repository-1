SELECT Class.name, Student_in_class.student 
FROM Class JOIN Student_in_class
    ON Class.id = Student_in_class.class 
    
