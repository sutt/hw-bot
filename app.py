import subprocess

'''

    SETUP INSTRUCTIONS:

    copy this file [app.py] and roster.csv into the root of repo

    repo: 
        
        - cloned from main hw assignemnt repo
        - run npm install the packages to node_modules

    before running this script:
        
        - add package-lock.json to the .gitignore of the repo, and save
            
            - if package-lock.json is already "tracked" in the git worksapce,
              you'll want to run:
                > git rm package-lock.json
                > git commit -m "rm plock"

            - may want to add package.json as well (?)
            
        - change `repo_name` below to the name of the repo slug

    now, run:
        > python app.py

    USE INSTRUCTIONS:

    run:
        > git branch 
    
        to view all branches available; should be one-per-student

    you can switch to any students work with:

        >git checkout <student-name>

'''

repo_name   = "react-likes"
base_url    = "https://git.generalassemb.ly/"

debug_fn    = 'debug.log'


with open('roster.csv', 'r') as f:
    lines = f.readlines()

def make_student_obj(line):    
    try:
        vals = line.split(',')
        vals = [val.strip('\n') for val in vals]
        return {
            'name':     vals[0],
            'ghuser':   vals[1],
            'branch':   vals[2],
        }
    except:
        return {}

students = [make_student_obj(line) for line in lines
            if len(make_student_obj(line).keys()) > 0
            ]

ERRS = []

def ll(cmd): 
    return cmd.split(' ')

def run_cmd(cmd):
    try:
        ret = subprocess.check_output(ll(cmd))
        return ret
    except Exception as e:
        ERRS.append(e)
        return e


for student in students:

    cmd = f'''git remote add {'r-' + student['name']} {base_url + student['ghuser'] + '/' + repo_name}'''
    ret = run_cmd(cmd)

for student in students:

    cmd = f'''git checkout -b {student['name']}'''
    ret = run_cmd(cmd)

    # TODO - run `git branch -a` to get what the student named their branch

for student in students:

    cmd = f'''git checkout {student['name']}'''
    ret = run_cmd(cmd)
    
    cmd = f'''git pull {'r-' + student['name']} {student['branch']}'''
    ret = run_cmd(cmd)
    

with open(debug_fn, 'w') as f:
    f.writelines(ERRS)

print(f"script complete!")
print(f"roster of length:    {len(students)}")
print(f"with num exceptions: {len(ERRS)} (view details in debug.log)")

