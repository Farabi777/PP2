print('Exist:', os.access('C:\Users\f_kua\Documents\PP2\HWeek6\dir', os.F_OK))
print('Readable:', os.access('C:\Users\f_kua\Documents\PP2\HWeek6\dir', os.R_OK))
print('Writable:', os.access('C:\Users\f_kua\Documents\PP2\HWeek6\dir', os.W_OK))
print('Executable:', os.access('C:\Users\f_kua\Documents\PP2\HWeek6\dir', os.X_OK))