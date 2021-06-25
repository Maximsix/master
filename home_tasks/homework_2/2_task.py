

# example 1
# append
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
for employee in global_logic_workers:
    toshiba_workers.append(employee)
else:
    print(toshiba_workers)

# example 2
# append
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
toshiba_workers.append(global_logic_workers[0])
toshiba_workers.append(global_logic_workers[1])
toshiba_workers.append(global_logic_workers[2])
toshiba_workers.append(global_logic_workers[3])
print(toshiba_workers)

# example 3
# +
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
all_workers_toshiba = toshiba_workers + global_logic_workers
print(all_workers_toshiba)


# example 4
# append /pop
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
while global_logic_workers:
    toshiba_workers.append(global_logic_workers.pop())
print(toshiba_workers)

# option 5
# extend
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
toshiba_workers.extend(global_logic_workers[:-len(global_logic_workers)])
print(all_workers_toshiba)


# example 6
# insert
global_logic_workers = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
toshiba_workers = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'Maksim Gekalo']
toshiba_workers.insert(0, global_logic_workers[0])
toshiba_workers.insert(1, global_logic_workers[1])
toshiba_workers.insert(2, global_logic_workers[2])
toshiba_workers.insert(3, global_logic_workers[3])
print(toshiba_workers)

# Excelent. Solution 4 is the most proper since global employees after absorbsion are employees of toshiba.
