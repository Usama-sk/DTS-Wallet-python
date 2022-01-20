a = dict(aa='aaaa', bb='bbbbb', cc='ccccc', dd='ddddd', ee='eeeee')
print([a.pop(key) for key in list(a.keys()) if key >= 'cc']) # => ['ccccc', 'ddddd', 'eeeee']
print(a) # => {