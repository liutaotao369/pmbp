import os;
import sys;
import platform;

if(platform.system()=="Windows"):
  bin_directory = "bin/Release"
else:
  bin_directory = "bin"

n_iterations = 2; 
patch_size = 1;
max_motion = 5;
n_particles = 1;
weight_pw = 10;
truncate_pw = 0.1;
tau1 = 20;
tau2 = 20;
alpha = 0;
asw = 15;
border = 0.85;

out_dir = "outputs/test"
os.system("mkdir -p "+out_dir)
  
one_name = "data/dog1_noise.png";
two_name = "data/dog2.png";

if(platform.system()=="Windows"):
  exe = "pmbp.exe"
else:
  exe = "pmbp"

command = bin_directory + "/" + exe + " -discrete " + \
          " -one " + one_name + \
          " -two " + two_name + \
          " -n_iterations " + str(n_iterations) + \
          " -patch_size " + str(patch_size) + \
          " -max_motion " + str(max_motion) + \
          " -weight_pw " + str(weight_pw) + \
          " -n_particles " + str(n_particles) + \
          " -weight_pw " + str(weight_pw) + \
          " -truncate_pw " + str(truncate_pw) + \
          " -tau1 " + str(tau1) + \
          " -tau2 " + str(tau2) + \
          " -alpha " + str(alpha) + \
          " -asw " + str(asw) + \
          " -border " + str(border) + \
          " -out_dir " + str(out_dir)

print command

if(platform.system()=="Windows"):
  command = command.replace("/","\\")

os.system(command)
