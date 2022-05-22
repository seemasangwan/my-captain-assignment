import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
         writer.writerow(["Name","Age","Contact number","Email.I.D"])
        writer.writerow(info_list)
if __name__=='__main__':
  student_num=1
  condition=True
  while(condition):
       student_info=input("Enter  student information for student #{} in following format (name Age  contact no. emailid) ".format(student_num))

       print("Enter information "+ student_info)
       #split
       student_info_list=student_info.split(' ')
       print("Entered split informtion is :"+str(student_info_list))
       print("\n the entered information -\n name:{}\n Age:{}\n contact number:{}\n emali id :{} "
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
       choice_check=input("is entered information  correct ? (yes/no)")
       if choice_check=="yes":
          write_into_csv(student_info_list)
          condition_check=input("enter (yes/no) if you want to  another student information ")
          if condition_check=="yes":
            condition=True
            student_num+=1
          elif condition_check=="no":
            condition=False
       elif choice_check=="no":
           print("please re-enter the values ")