#learning to append items to a list and using method
things_to_do = ["kasm", "tor", "ctfs in THM", "pentlab_lessons", "python", "learn winservers", "learn proxmox", "add more attack labs"]
#print(things_to_do)
things_to_do.append("root_me_ctfs")#
#print(things_to_do)
things_to_do.append("bidet")
#print(things_to_do)
things_to_do.extend(["portswigger", "itprotv_classes"]) #using extend, use ( and []) with "xx", "xx" inside brackets
#print(things_to_do)
things_to_do.insert(0, "itprotv_classes")
#print(things_to_do)
things_to_do.insert(-1, "hacking_python")
print(things_to_do)#.insert will insert a new item in a list in a specific location. -1 or 2nd from the last. 



