import os
import subprocess as sp
os.system("tput setaf 7")
print("\t\t\t*****************************************")
os.system("tput setaf 3")
print("\t\t\t\tWelcome To LVM Parttiton!!!")
os.system("tput setaf 7")
print("\t\t\t******************************************")
while True :	
	r = input("\nWhere You Want To Run These Menu ? (Local/Remote) : ")
	if r == "local":
			os.system("tput setaf 3")
			print("""
			\n
			press 1 :  To See Hard Disk Information
			press 2 :  To Create Physical Volume (PV)
			press 3 :  To See How Many Physical Volume You Have
			press 4 :  To Create Volume Group(VG)
			press 5 :  To See How Many Volume Group You Have
			press 6 :  To Create Logical Volume(LV)
			press 7 :  To See How Many Logical Volume You Have
	 		press 8 :  To Format The Logical Volume(LV)
			press 9 :  To Create A Folder Where You Want To Mount 
			press 10:  To Mount File System(Folder)	
			press 11:  To Increse/extent The Size Of LVM
			press 12:  To Reduse The Size Of Logical Partition(LVM)
			press 13:  To Remove Physical Volume
			press 14:  To Remove Volume Group
			press 15:  Exit
			""")
			os.system("tput setaf 7")
			ch = input("\t\tTell Me Your Requirment : ")
			print(ch)
			if int(ch)==1:
				os.system("tput setaf 2")
				os.system("fdisk -l")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List : ")
				os.system("clear")
			elif int(ch)==2:
				pvnumber = int(input("\t\tHow Many Hard Disk You Have : "))
				for x in range(0,pvnumber) :
					print()
					dname = input("\t\tEnter Your Hard Disk Name eg. /dev/sdc : 				")
					cmd = "pvcreate {}".format(dname)
					output = sp.getstatusoutput(cmd)
					status = output[0]
					out = output[1]
					if status == 0:
						os.system("tput setaf 2")
						print("****Physical Volume {} Created Successfully, Here You Can See****")
						os.system("pvdisplay {}".format(dname))
						os.system("tput setaf 7")
					else :
						os.system("tput setaf 1")
						print("Some Error : {} ".format(out))
						os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 3:
				os.system("tput setaf 2")
				os.system("pvdisplay")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 4:
				vgname = input("\nEnter The Name For Volume Group With Your Hard 	Disk Name eg. iiecvg /dev/sdc /dev/sdd : ")
				os.system("vgcreate {}".format(vgname))
				os.system("tput sertaf 2")
				print("\nYour Volume Group Created Successfully, Here You Can 	See")
				os.system("vgdisplay {}".format(vgname))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 5:
				os.system("tput setaf 2")
				os.system("vgdisplay")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 6:
				s,n,vn = input("\nEnter Your Logical Volume Size , Name and Volume Group Name : ").split()
				cmd = "lvcreate --size {0} --name {1} {2}".format(s,n,vn)
				output = sp.getstatusoutput(cmd)
				status = output[0]
				out = output[1]
				if status == 0:
					os.system("tput setaf 2")
					print("\n\t\tLV {} Created Successfully, Here You Can 	See".format(n))
					os.system("lvdisplay {}/{} ".format(vn,n))
					os.system("tput setaf 7")
				else :
					os.system("tput setaf 1")
					print("\n\t\tSome Error : {}".format(out))
					os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 7 :
				os.system("tput setaf 2")
				os.system("lvdisplay")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 8:
				f = input("\nEnter Your Logical Volume Name For Format eg . /dev/iiesvg/mylv1")
				os.system("mkfs.ext4 {}".format(f))
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 9 :
					foldern = input("\nEnter Folder Name Where You Want To Mount eg . /task1 : ")
					cmd = "mkdir {}".format(foldern)
					output = sp.getstatusoutput(cmd)
					status = output[0]
					out = output[1]
					if status == 0:
						os.system("tput setaf 2")
						print("\t\t\t Your Folder {} Created Successfully....".format(foldern))
						os.system("tput setaf 7")
					else :
						os.system("tput setaf 1")
						foldern = input("\nEnter New Folder Name You Want To Mount . /t : ")
						os.system("tput setaf 7")
					input("\nPress Enter For Menu List :")
					os.system("clear")
			elif int(ch) == 10 :
				vg,lv,foldername = input("\nEnter vg name and lv name and Folder Name Where You Want To Mount eg . iiecvg mylv1 task1 : ").split()
				os.system("mount /dev/{0}/{1} /{2}".format(vg,lv,foldername))
				os.system("tput setaf 2")
				os.system("df -hT")
				print("\n\t**** Your LV Mounted Successfully, Now You Can Use {} Folder****".format(foldername))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 11 :
				vgname = input("\nEnter Your Vg Name For Checking Free Space : ")
				os.system("tput setaf 2")
				os.system("vgdisplay {}".format(vgname))
				os.system("tput setaf 7")
				ins,path = input("\nEnter The Size You Want To Increse of Logical Volume(LVM) With Name Of Your Logical Volume eg . 5G  mylv1 : ").split()
				os.system("lvextend --size +{} /dev/{}/{}".format(ins,vgname,path))
				os.system("resize2fs /dev/{}/{}".format(vgname,path))
				os.system("tput setaf 2")
				os.system("lvdisplay {}/{}".format(vgname,path))
				print("\n\t****Logical Volume Extended And Mounted Successfully****")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 12 :
				os.system("df -hT")
				lpath = input("\nEnter Your LG Name eg . /dev/mapper/iiesvg-mylv1  : ")
				fs = input("\nEnter Your File System For Unmount : eg. /task1")
				os.system("umount {}".format(fs))
				size = input("Enter The Size You Want To Kept 50G: ")
				os.system("resize2fs {} {}".format(lpath,size))
				os.system("lvreduce -L {} {}".format(size,lpath))
				os.system("e2fsck -f {}".format(lpath))
				os.system("tput setaf 2")
				os.system("lvdisplay {}".format(lpath))
				print("\n\t****LVM Reduse Successfully****")
				print("\n\t***Your File System Are Again Mounted****")
				os.system("mount {}".format(fs))
				os.system("resize2fs {} {}".format(lpath))
				os.system("df -h {}".format(fs))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 13 :
				pvr = input("\nEnter Physical Volume Name You Want To Remove : ")
				os.system("pvremove {}".format(pvr))
				os.system("tputsetaf 2")
				os.system("pvdisplay")
				print("\n\t****PV Removed Successfully****")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 14 :
				vgr = input("\nEnter Volume Group Name You Want To Remove : ")
				os.system("vgremove {}".format(vgr))
				os.system("tput setaf 2")
				os.system("vgdisplay")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 15 :
				exit()
	elif r=="remote" :
			ip = input("\nEnter The IP Of The System Where You Want To Run : ")
			print(ip)
			os.system("tput setaf 3")
			print("""
			\n
			press 1 :  To See Hard Disk Information
			press 2 :  To Create Physical Volume (PV)
			press 3 :  To See How Many Physical Volume You Have
			press 4 :  To Create Volume Group(VG)
			press 5 :  To See How Many Volume Group You Have
			press 6 :  To Create Logical Volume(LV)
			press 7 :  To See How Many Logical Volume You Have
	 		press 8 :  To Format The Logical Volume(LV)
			press 9 :  To Create A Folder Where You Want To Mount 
			press 10:  To Mount File System(Folder)	
			press 11:  To Increse/extent The Size Of LVM
			press 12:  To Reduse The Size Of Logical Partition(LVM)
			press 13:  To Remove Physical Volume
			press 14:  To Remove Volume Group
			press 15:  Exit
			""")
			os.system("tput setaf 7")
			ch = input("\t\tTell Me Your Requirment : ")
			print(ch)
			if int(ch)==1:
				os.system("tput setaf 2")
				os.system("ssh {} fdisk -l".format(ip))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List : ")
				os.system("clear")
			elif int(ch)==2:
				pvnumber = int(input("\t\tHow Many Hard Disk You Have : "))
				for x in range(0,pvnumber) :
					print()
					dname = input("\t\tEnter Your Hard Disk Name eg. /dev/sdc : 				")
					cmd = "ssh {0} pvcreate {1}".format(ip,dname)
					output = sp.getstatusoutput(cmd)
					status = output[0]
					out = output[1]
					if status == 0:
						os.system("tput setaf 2")
						print("****Physical Volume {} Created Successfully, Here You Can See****")
						os.system("ssh {0} pvdisplay {1}".format(ip,dname))
						os.system("tput setaf 7")
					else :
						os.system("tput setaf 1".format(ip))
						print("\n\t\tSome Error : {} ")
						os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 3:
				os.system("tput setaf 2")
				os.system("ssh {} pvdisplay".format(ip))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 4:
				vgname = input("Enter The Name For Volume Group With Your Hard 	Disk Name eg. iiecvg /dev/sdc /dev/sdd : ")
				os.system("ssh {0} vgcreate {1}".format(ip,vgname))
				os.system("tput sertaf 2")
				print("\n\t\tYour Volume Group Created Successfully, Here You Can See")
				os.system("ssh {} vgdisplay {}".format(ip,vgname))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 5:
				os.system("tput setaf 2")
				os.system("ssh {} vgdisplay".format(ip))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 6:
				s,n,vn = input("\nEnter Your Logical Volume Size , Name and Volume Group Name : ").split()
				cmd = "ssh {0} lvcreate --size {1} --name {2} {3}".format(ip,s,n,vn)
				output = sp.getstatusoutput(cmd)
				status = output[0]
				out = output[1]
				if status == 0:
					os.system("tput setaf 2")
					print("\n\t\tLV {} Created Successfully, Here You Can 	See".format(n))
					os.system("ssh {} lvdisplay {}/{} ".format(ip,vn,n))
					os.system("tput setaf 7")
				else :
					os.system("tput setaf 1")
					print("\n\t\tSome Error : {}".format(out))
					os.sytem("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 7 :
				os.system("tput setaf 2")
				os.system("ssh {} lvdisplay".format(ip))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("ssh {} clear".format(ip))
			elif int(ch) == 8:
				f = input("\nEnter Your Logical Volume Name For Format eg . /dev/iiesvg/mylv1")
				os.system("ssh {} mkfs.ext4 {}".format(ip,f))
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 9 :
					foldern = input("\nEnter Folder Name Where You Want To Mount eg . /task1 : ")
					cmd = "ssh {} mkdir {}".format(ip,foldern)
					output = sp.getstatusoutput(cmd)
					status = output[0]
					out = output[1]
					if status == 0:
						os.system("tput setaf 2")
						print("\t\t\tYour Folder {} Created Successfully....".format(foldern))
						os.system("tput setaf 7")
					else :
						os.system("tput setaf 1")
						foldern = input("\nEnter New Folder Name You Want To Mount . /t : ")
						os.system("tput setaf 7")
					input("\nPress Enter For Menu List :")
					os.system("clear")
			elif int(ch) == 10 :
				vg,lv,foldername = input("\nEnter vg name and lv name and Folder Name Where You Want To Mount eg . iiecvg mylv1 task1 : ").split()
				os.system("ssh {0} mount /dev/{1}/{2} /{3}".format(ip,vg,lv,foldername))
				os.system("tput setaf 2")
				os.system("ssh {} df -hT".format(ip))
				print("\n\t**** Your LV Mounted Successfully, Now You Can Use {} Folder****".format(foldername))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 11 :
				vgname = input("\nEnter Your Vg Name For Checking Free Space : ")
				os.system("tput setaf 2")
				os.system("ssh {} vgdisplay {}".format(ip,vgname))
				os.system("tput setaf 7")
				ins,path = input("\nEnter The Size You Want To Increse of Logical Volume(LVM) With Name Of Your Logical Volume eg . 5G  mylv1 : ").split()
				os.system("ssh {0} lvextend --size +{1} /dev/{2}/{3}".format(ip,ins,vgname,path))
				os.system("ssh {0} resize2fs /dev/{1}/{2}".format(ip,vgname,path))
				os.system("tput setaf 2")
				os.system("ssh {0} lvdisplay {1}/{2}".format(ip,vgname,path))
				print("\n\t****Logical Volume Extended And Mounted Successfully****")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 12 :
				os.system("ssh {} df -hT".format(ip))
				lpath = input("\nEnter Your LG Name eg . /dev/mapper/iiesvg-mylv1  : ")
				fs = input("\nEnter Your File System For Unmount : eg. /task1")
				os.system("ssh {} umount {}".format(ip,fs))
				os.system("ssh {} e2fsck -f {}".format(ip,lpath))
				size = input("\nEnter The Size You Want To Kept 50G: ")
				os.system("ssh {0} resize2fs {1} {2}".format(ip,lpath,size))
				os.system("ssh {0} lvreduce -L {1} {2}".format(ip,size,lpath))
				os.system("ssh {} e2fsck -f {}".format(ip,lpath))
				os.system("ssh {} tput setaf 2".format(ip))
				os.system("ssh {} lvdisplay {}".format(ip,lpath))
				print("\n\t****LVM Reduse Successfully****")
				print("\n\t***Your File System Are Again Mounted****")
				os.system("ssh {} mount {}".format(ip,fs))
				os.system("ssh {} df -h {}".format(ip,fs))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 13 :
				pvr = input("\nEnter Physical Volume Name You Want To Remove : ")
				os.system("ssh {} pvremove {}".format(ip,pvr))
				os.system("tputsetaf 2")
				os.system("ssh {} pvdisplay".format(ip))
				print("\n\t****PV Removed Successfully****")
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 14 :
				vgr = input("\nEnter Volume Group Name You Want To Remove : ")
				os.system("ssh {} vgremove {}".format(ip,vgr))
				os.system("tput setaf 2")
				os.system("ssh {} vgdisplay".format(ip))
				os.system("tput setaf 7")
				input("\nPress Enter For Menu List :")
				os.system("clear")
			elif int(ch) == 15 :
				os.system("exit")
				exit()
		
			
				
						


