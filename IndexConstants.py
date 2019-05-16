from tools.PrintUtil import *

all_stock_file_name = "01AllStock.txt"
date_file_path = get_root_path() + os.sep + "dataFiles" + os.sep
all_stock_full_path = date_file_path + all_stock_file_name
all_ST_stock_path = date_file_path + "01All_ST.txt"
all_60_stock_path = date_file_path + "01All_60.txt"
all_00_stock_path = date_file_path + "01All_00.txt"
all_30_stock_path = date_file_path + "01All_30.txt"
stock_file_path = get_root_path() + os.sep + "dataFiles" + os.sep + "stock" + os.sep

#后赋权
stock_file_path_hfq = get_root_path() + os.sep + "dataFiles" + os.sep + "stock_hfq" + os.sep

real_time_stock_load = get_root_path() + os.sep + "analysisStock.txt"
