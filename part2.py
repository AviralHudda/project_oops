# Create a weekly calendar with appointment slots
def create_weekly_calender(appt_list):
    # Clear any existing appointments in the list
    appt_list.clear()
    # Define the working days of the week
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        # Create an appointment slot for every hour (9AM-5PM) on each day
    for day in week_days:
        for hour in range(9,17): # # Salon operates from 9 AM to 5 PM
            current_appt = appointment(day,hour)
            appt_list.append(current_appt) ## Add the created appointment to the list
    print("Weekly calender created")

#  Create a dictionary to load previous schedule from a file
def load_scheduled_appointments(appt_list):
    import os
    # Prompt user to enter the filename
    file_load = input("Enter appointment filename: ")
    file_found = False
    while file_found == False:
        # Check if the file exists, re-prompt if it doesn't
        if os.path.exists(file_load):
            file_found = True
        else:
            file_load = input("File not found. Re-enter appointment filename: ")

    if file_found:
        no_of_appts = 0
            # Open the file and read appointments line by line
        with open(file_load , "r") as file:
            for line in file:
            # Parse the appointment details
                client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(",")
                # Find the corresponding appointment slot
                current_appt = find_appointment_by_time(appt_list, day_of_week, start_time_hour)
                # Schedule the appointment with the loaded details
                current_appt.schedule(client_name, client_phone, appt_type)
                no_of_appts += 1
        print(f"{no_of_appts} previously scheduled appointments have been loaded")

#  Create a dictionary to store the monthly calendar
def find_appointment_by_time(appt_list, day_to_find, start_hour_to_find):
    # Loop through the appointments to find the matching one
    for appt in appt_list:
        if str(appt.get_day_of_week()) == str(day_to_find) and int(appt.get_start_time_hour()) == int(start_hour_to_find) :
            return appt # # Return the matching appointment
    return None ## Return None if no match is found

    
# Display the main menu and prompt the user for a selection
def print_menu():
    repeat_menu = True
    while repeat_menu:
        print()
        print("======================================")
        print(f"    Hair Salon Appointment Manager    ")
        print("======================================","\n",
          "1) Schedule an appointment","\n","2) Find appointment by name","\n",
          "3) Print calender for a specific day","\n",
          "4) Cancel an appointment","\n","5) Change an appointment","\n",
          "6) Calculate total fees for a day","\n",
          "7) Calculate total weekly fees","\n","9) Exit the system")
        # Get the user's menu choice
        client_selection = int(input("Enter your selection: "))
        # Validate the menu choice
        if 0 < client_selection < 8 or client_selection == 9:
            repeat_menu = False
            return client_selection ## Return valid selection
        else:
            print()
            print("Invalid option")
            repeat_menu = True

# Display all appointments for a specific client
def show_appointments_by_name(appt_list, name_to_show):
    print()
    print(f"Client Name         Phone          Day       Start     End       Type")
    print("--------------------------------------------------------------------------------------")
    flag = False
    for appt in appt_list:
        if name_to_show.title() in str(appt.get_client_name()):
            flag = True
            print(appt) ## Print the appointment details
    if not flag:
        print("No appointments found.")

# Display all appointments for a specific day
def show_appointments_by_day(appt_list, day_to_show):
    print()
    print(f"Client Name         Phone          Day       Start     End       Type")
    print("--------------------------------------------------------------------------------------")
    for appt in appt_list:
        if day_to_show.title() in str(appt.get_day_of_week()):
            print(appt) # # Print the appointment details

# Change an appointment to a different time slot
def change_appointment_by_day_time(appt_list):
    print("Change an appointment for:")
    # Prompt the user for the current appointment's day and time
    day_from_change = input("What day: ").title()
    time_from_change = input("Enter start hour (24 hour clock): ")
    # Find the matching appointment
    for appt in appt_list:
        if str(appt.get_day_of_week()) == str(day_from_change) and int(appt.get_start_time_hour()) == int(time_from_change):
            if appt.get_appt_type() != 0: # Ensure the appointment is booked
                last_appt = appt
                # Prompt for the new day and time
                day_to_change = input("Enter a new day: ").title()
                time_to_change = input("Enter start hour (24 hour clock): ")
                # Check if the new time slot is available
                for appt in appt_list:
                    if str(appt.get_day_of_week()) == str(day_to_change) and int(appt.get_start_time_hour()) == int(time_to_change):
                        if appt.get_appt_type() == 0:
                            # Reschedule the appointment to the new time slot
                            current_client_name = last_appt.get_client_name()
                            current_client_phone = last_appt.get_client_phone()
                            current_appt_type = last_appt.get_appt_type()
                            last_appt.cancel()
                            appt.schedule(current_client_name, current_client_phone, current_appt_type)
                            print(f"Appointment for {current_client_name} has been changed to:")
                            print("Day =", day_to_change)
                            print("Time =", time_to_change)
                        else:
                            print("The new time slot is already booked")            
            else:
                print("That time slot isn't booked and doesn't need to be changed")
# Calculate total fees for a specific day based on scheduled appointments
def calculate_fees_per_day(appt_list):
    print("Fees calculation per day....")
    day_for_fees = input("What day: ").title()
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    total_cost = 0
    if day_for_fees in week_days:
        for appt in appt_list:
            if day_for_fees == appt.get_day_of_week():
                appt_type = appt.get_appt_type()
                # Add fees based on appointment type
                if int(appt_type) == 1:
                    total_cost += 40
                elif int(appt_type) == 2:
                    total_cost += 60
                elif int(appt_type) == 3:
                    total_cost += 40
                elif int(appt_type) == 4:
                    total_cost += 80

        print(f"Total fees for {day_for_fees} is ${total_cost}")       
    else:
        print(f"{day_for_fees} is invalid day or the salon is closed")
       
# Calculate total weekly fees based on all scheduled appointments
def calculate_weekly_fees(appt_list):
    total_cost = 0
    for appt in appt_list:
        appt_type = appt.get_appt_type()
        # Add fees based on appointment type
        if int(appt_type) == 1:
            total_cost += 40
        elif int(appt_type) == 2:
            total_cost += 60
        elif int(appt_type) == 3:
            total_cost += 40
        elif int(appt_type) == 4:
            total_cost += 80
    print(f"Total weekly fees is ${total_cost}")

# Save all scheduled appointments to a file
def save_scheduled_appointment(appt_list):
    import os
    import csv
    repeat_ask = True
    while repeat_ask:
        file_name = input("Enter appointment filename: ")
        if os.path.exists(file_name):
            # Prompt user for overwrite permission if file exists
            overwrite = input("File already exist. Do you want to overwrite it (Y/N)? ").upper()
            if overwrite == "Y":
                repeat_ask = False
                # Save appointments to the file
                with open(file_name , "w", newline='') as file:
                    writer = csv.writer(file)
                    appointments_saved = 0
                    for appt in appt_list:
                        if appt.get_appt_type() != 0: # Ignore cancelled appointments
                            writer.writerow(appt.format_record().split(","))
                            appointments_saved += 1
                    print(f"{appointments_saved} scheduled appointments have been successfully saved")
            elif overwrite == "N":
                repeat_ask = True
        else:
            repeat_ask = False
            # Save to a new file if it doesn't already exist
            with open(file_name , "w", newline='') as file:
                    writer = csv.writer(file)
                    appointments_saved = 0
                    for appt in appt_list:
                        if appt.get_appt_type() != 0:
                            writer.writerow(appt.format_record().split(","))
                            appointments_saved += 1
                    print(f"{appointments_saved} scheduled appointments have been successfully saved")

# Schedule a new appointment
def schedule_appointment(appt_list):
    print("** Schedule an appointment **")
    # Prompt the user for the appointment day and time
    day_to_schedule = input("What day: ").title()
    time_to_schedule = input("Enter start hour (24 hour clock): ")
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    # Validate the day and time
    if day_to_schedule not in week_days or int(time_to_schedule) not in range(9,17):
        print("Sorry that time slot is not in the weekly calender!")
        return 
    # Check if the selected time slot is available
    for appt in appt_list:
        if str(day_to_schedule) == str(appt.get_day_of_week()) and int(time_to_schedule) == int(appt.get_start_time_hour()):
            if int(appt.get_appt_type()) == 0: # Check if the time slot is already scheduled
                client_name = input("Client Name: ").title()
                client_phone = input("Client Phone: ")
                print("Appointment types")
                print(appt.get_appt_type_desc())
                appt_type = input("Type of Appointment: ") # Get the appointment type from the user
                appt.schedule(client_name, client_phone, appt_type)
                print(f"OK, {client_name}'s appointment is scheduled!")
            else:
                print("Sorry that time slot is booked already!") # If the time slot is already booked, inform the user
        
# Display all appointments
def main():
    appt_list = [] # list to hold all appointments
    print("Starting the Appointment Manager System")
    create_weekly_calender(appt_list) #  the weekly calender
    # Optionally load previously scheduled appointments
    load_previous_file = input("Would you like to load previously scheduled appointments from a file (Y/N)?").title()
    if load_previous_file == "Y":
        load_scheduled_appointments(appt_list)
    menu_repeat = True
    while menu_repeat:
        option_chosen = print_menu() # # Display menu and get user selection
        print()
        if 0<option_chosen<8:
            if option_chosen == 1:
                schedule_appointment(appt_list)
            if option_chosen == 2:
                print("** Find appointment by name **")
                name_to_show = input("Enter Client Name: ")
                print(f"Appointments for {name_to_show}")
                show_appointments_by_name(appt_list, name_to_show)
            elif option_chosen == 3:
                print("** Print calendr for a specific day **")
                day_to_show = input("Enter day of week: ").title()
                print(f"Appointments for {day_to_show}")
                show_appointments_by_day(appt_list, day_to_show)
            elif option_chosen == 4:
                print("** Cancel an appointment **")
                day_to_cancel = input("What day: ").title()
                time_to_cancel = input("Enter start hour (24 hour clock): ")
                 # Find and cancel the matching appointment
                for appt in appt_list:
                    if str(appt.get_day_of_week()) == str(day_to_cancel) and int(appt.get_start_time_hour()) == int(time_to_cancel):
                        if appt.get_appt_type() != 0:
                            name_to_cancel = appt.get_client_name()
                            appt.cancel()
                            print(f"Appointment: {appt.get_day_of_week()} {appt.formatTime(appt.get_start_time_hour())}:00 - {appt.formatTime(appt.get_start_time_hour() + 1)}:00 for {name_to_cancel} has been cancelled!")
                        else:
                            print("That time slot isn't booked and doesn't need to be cancelled")
            elif option_chosen == 5:
                change_appointment_by_day_time(appt_list)
            elif option_chosen == 6:
                calculate_fees_per_day(appt_list)
            elif option_chosen == 7:
                calculate_weekly_fees(appt_list)
            menu_repeat = True
        else:
            menu_repeat = False
            print("** Exit the system **")
            # Optionally save scheduled appointments before exiting
            file_save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").upper()
            if file_save == "Y":
                save_scheduled_appointment(appt_list)
            print("Good Bye!")

# Entry point for the program
if __name__ == "__main__":
    main()
    
