# import subprocess
# import time

# process = subprocess.Popen(
#             ['/bin/python3', '../oxin_storage_management/storage_main_UI.py', 'en', 'False']
#             )

# while True:
#     print(process.poll())

# a = [ 'T'+str(i) for i in range(5)]
# print(a)

a = ['T10.000000', 'T20.000000', 'T30.000000', 'T40.000000', 'T50.000000', 'T60.000000', 'T70.000000']#, 'T80.000000', 'T90.000000', 'T100.000000', 'T110.000000', 'T120.000000', 'T130.000000', 'T140.000000', 'T1500.0000002', 'T1630.0000005', 'T1760.0000008', 'T1890.000000', 'T190.000000', 'T200.000000']

if len(a)>9:
    print(float(a[-1][3:]))
else:
    print(a[-1][2:])