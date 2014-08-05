import os
import datetime

stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

topOutputDirectory = "output/"+stamp

if not os.path.exists(topOutputDirectory):
    os.makedirs(topOutputDirectory)

os.environ["TOPOUTPUTDIRECTORY"] = "../"+topOutputDirectory
os.system("runipy scripts/init.ipynb --html "+topOutputDirectory+"/overview_report.html")