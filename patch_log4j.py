import os
import shutil

log4j_patterns= [
    "log4j-1.2-api",
    "log4j-api",
    "log4j-core",
    "log4j-slf4j-impl"]
jar_pattern = ".jar"
# CHANGE THIS PATH ###########################
source = "/mnt/c/AnypointStudio"
# ############################################
patch_source = "apache-log4j-2.16.0-bin"

for root, sub_folders, files in os.walk(source):
    for file in files:
        for pattern in log4j_patterns:
            if pattern in file:
                if "scala" in file:
                    continue
                #print("Found {} from pattern {}, starting processing".format(file,pattern))    
                path = "{}/{}".format(root, file)
                print("deleting {}".format(path))
                os.remove(path)
                source_replacement = "{}/{}{}".format(patch_source, pattern, "-2.16.0.jar") 
                #print("Copying over {}".format(source_replacement))
                parent_path = "/".join(path.split("/")[:-1])
                print("cp -f {} {}".format(source_replacement, path  ))
                shutil.copy(source_replacement, parent_path)
