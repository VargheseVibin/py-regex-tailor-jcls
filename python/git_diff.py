import subprocess
PIPE=subprocess.PIPE


subprocess.run("git", "diff", "b6965c7bf3d3fd0df7b4649cd15b9b411d9a05d8", "f591695b03faa26921ceec6bdba9323e7f9b6b75", "--name-only","\"*.cpp\"")


# git diff b6965c7bf3d3fd0df7b4649cd15b9b411d9a05d8 f591695b03faa26921ceec6bdba9323e7f9b6b75 --name-only "*.cpp" "*.h"> diff_files.txt