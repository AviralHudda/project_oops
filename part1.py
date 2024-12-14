class appointment:
    
    def __init__(self,day_of_week,start_time_hour):
        self.__client_name = 0
        self.__client_phone = 0
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name
    
    def get_client_phone(self):
        return self.__client_phone
    
    def get_appt_type(self):
        return self.__appt_type
    
    def get_day_of_week(self):
        return self.__day_of_week
    
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_appt_type_desc(self):
        return("1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")
    
    def get_appt_type_changed_to_desc(self):
        if int(self.get_appt_type()) == 0:
            return "Available"
        elif int(self.get_appt_type()) == 1:
            return "Mens Cut" 
        elif int(self.get_appt_type()) == 2:
            return "Ladies Cut"
        elif int(self.get_appt_type()) == 3:
            return "Mens Colouring"
        elif int(self.get_appt_type()) == 4:
            return "Ladies Colouring"


    def get_end_time_hour(self):
        return(self.__start_time_hour + 1)
    
    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.__client_name = 0
        self.__client_phone = 0
        self.__appt_type = 0

    def formatTime(self, time):
        if len(str(time)) < 2:
            return f"0{time}"
        return time
    
    def for_str_client_name(self,client_name):
        if client_name != 0:
            return client_name
        return ""
        
    def for_str_client_phone(self,client_phone):
        if client_phone != 0:
            return client_phone
        return ""

    def format_record(self):
        return(f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.formatTime(self.__start_time_hour)}")
    
    def __str__(self):
        return(f"{self.for_str_client_name(self.get_client_name()):<20}{self.for_str_client_phone(self.get_client_phone()):<15}{self.__day_of_week:<10}{self.formatTime(self.__start_time_hour)}:00  -  {self.get_end_time_hour()}:00     {self.get_appt_type_changed_to_desc()}")
    

