# Andrew Keller
# 12/29/2024


def main():
    course_list = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']
    room_list = ['3004', '4501', '6755', '1244', '1411']
    instructors_list = ['Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee']
    time_list = ['8:00 a.m.', '9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '1:00 p.m.']
    room_dict, instructor_dict, time_dict = make_dictionaries(course_list, room_list, instructors_list, time_list)
    course = get_input(course_list)
    display_output(room_dict, instructor_dict, time_dict, course)
    

def make_dictionaries(course_list, room_list, instructors_list, time_list):
    room_dict = dict(zip(course_list, room_list))
    instructor_dict = dict(zip(course_list, instructors_list))
    time_dict = dict(zip(course_list, time_list))
    return room_dict, instructor_dict, time_dict

def get_input(course_list):
    course = input('What is the course number you would like to look up? ')
    course = course.upper()
    while course not in course_list:
        course = input('Course not found. What is the course number you would like to look up? ')
        course = course.upper()
    return course

def display_output(room_dict, instructor_dict, time_dict, course):
    print(f'Course {course} meets at {time_dict[course]} in room {room_dict[course]} and is taught by {instructor_dict[course]}.')


if __name__ == '__main__':
    main()
