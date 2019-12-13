#! /usr/bin/env python3

from git import Repo
import os, sys

def pushToGithub(directoryName):
  try:
    # create remote repo
      # nice to have in future: prompt user for git user name
    print("Creating a new repo on GitHub...")
    createGithubRepoCommand = "curl -u 'julibi' https://api.github.com/user/repos -d '{\"name\":\""+directoryName+"\"}'"
    os.system(createGithubRepoCommand)

    # git staging
    print("First commit...")
    repo = Repo.init(os.getcwd())
    repo.git.add('.')
    repo.git.commit('-m', 'first commit')

    # push to newly created remote repo
    print("Pushing to newly created repo...")
    remoteRepoUrl = 'git@github.com:julibi/{}'.format(directoryName)
    repo.git.push(remoteRepoUrl, 'HEAD:master')

    print('DONE')
    repoURL = 'github.com/julibi/{}'.format(directoryName)
    print('You are all set and can start coding away in {}.\nYou can find your GitHub repo here: {}.'.format(os.getcwd(), repoURL))
  except:
    print('Sorry. Some error occured while pushing the code. But the directory has been setup. You can create a repo manually and push to it.')  
    sys.exit(1)
  else:
    sys.exit()

def createREADME(directoryName):
  READMEContent = raw_input("Write a short project description for the README.md \n")
  f = open('README.md', 'a')
  f.write(READMEContent)
  f.close()
  print("README.md created.")

def setupDirectory(directoryName):
  print("Creating a directory with the name {}".format(directoryName))
  try:
    os.mkdir(directoryName)
  except OSError:
    print ("Creation of the directory {} failed".format(directoryName))
  else:
    print ("Succesfully created the directory {}".format(directoryName))
  os.chdir(directoryName)
  answer = raw_input("Would you like to create a README.md? Y/N \nIt is recommended to create a README.md in order to automatically create a repo on GitHub.").upper()
  if answer == ('Y' or 'YES'):
    createREADME(directoryName)
    pushToGithub(directoryName)
  else:
    print("Ok. Have fun with your new project. Bye!")
    sys.exit()
  
def tryAgain():
  answer = raw_input("What do you wanna call your project?\n")
  checkdirectoryName(answer)

def checkdirectoryName(directoryName):
    # make sure the name does not have spaces
    if isinstance(directoryName, str):
      directoryName = directoryName.split()
    if len(directoryName) > 1:
        print("Please do not pass a name with spaces. Use underscores like this 'my_project_name', or hypens liks this 'my-project-name'.")
        print("So let's try again.")
        tryAgain()
    # go to the directory and get the existing project names
      # nice to have in future: prompt user for the directory in which the setup of the project is desired
    os.chdir('/Users/hyun-kyungyi/JULI')
    doppelgaenger = 0
    existingProjectNames = os.listdir('.')

    # check the suggested project name is unique
    for projectName in existingProjectNames:
      if projectName == directoryName:
        doppelgaenger += 1
        print("You already have a project called {}".format(directoryName))
        answer = raw_input("Do you wanna try another name? Y/N \n").upper()
        if answer == ('Y' or 'YES'):
          tryAgain()
        else:
          print("Ok, byeee")
          sys.exit()
    if doppelgaenger == 0:
      directoryName = ''.join(directoryName)
      setupDirectory(directoryName)

try:
  while True:
    requestedProjectName = sys.argv[1:]

    if len(sys.argv) == 1:
      tryAgain()
    else:
      checkdirectoryName(requestedProjectName) 
except KeyboardInterrupt:
    print("\nGoodbye!")
    exit(0)



