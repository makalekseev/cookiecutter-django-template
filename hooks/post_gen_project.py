import os
import secrets
import shlex
from subprocess import check_output

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Create a minimal .env file for development
env_file = os.path.join(PROJECT_DIRECTORY, '.env')
with open(env_file, 'w') as f:
    f.write('DJANGO_DEBUG=1\n')
    f.write('DJANGO_SECRET_KEY="{0}"\n'.format(secrets.token_hex()))

# Init the git repository and do the inital commit.
check_output(['git', 'init'])
check_output(['git', 'add', '-A', '.'])
check_output(['git', 'commit', '-a', '-m', 'Initial checkin.'])

print('New Django project created in "{0}".'.format(PROJECT_DIRECTORY))