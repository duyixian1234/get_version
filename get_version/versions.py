python_versions = {'python': '-V', 'python3': '-V', 'pip': '-V'}
node_versions = {'node': '-v', 'npm': '-v', 'yarn': '-v'}
java_versions = {'java': '-version', 'mvn': '-v', 'gradle': '-v'}
cxx_versions = {'gcc': '-v', 'clang': '-v'}
go_versions = {'go': 'version'}

version_dict = {**python_versions, **node_versions, **java_versions, **cxx_versions, **go_versions}
