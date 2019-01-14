from git import Repo, Commit
import os
import subprocess
import datetime


path = '/Users/bhavnasud/Desktop/chaining'

COMMIT_MESSAGE = 'First Commit Message'
def git_commit():
	time = "Sat, 13 Dec 2019 12:40:00 +0000"
	repo = Repo(path)
	os.environ["GIT_AUTHOR_DATE"] = time
	os.environ["GIT_COMMITTER_DATE"] = time
	repo.git.add('--all')
	comm = Commit(repo, Commit.NULL_BIN_SHA, None, 
      None, time, 0, 
      None, time, 0,
      COMMIT_MESSAGE, None, None)
	#for x in range(0, 100000):
	    #try:
	comm.message = 'noonce' + COMMIT_MESSAGE
	print(comm.hexsha)
	        #repo.index.commit('noonce' + str(x) + COMMIT_MESSAGE)
	        #if (x % 1000 == 0):
	        	#print(x)
	        #sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
	        #sha = repo.head.object.hexsha
	        #six = sha[0:6]
	        #print(six)
	        #if(s == '000000'):
	        	#print('YASSSSS')
	        	#break
	        #repo.head.reset('HEAD~1', index=True, working_tree=True)
	        #repo.git.reset('--hard')
	        #repo.remotes.origin.pull(rebase=True)

	    #except:
	        #print('Some error occured while committing the code')
git_commit()