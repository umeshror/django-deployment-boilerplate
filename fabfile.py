from fabric.api import env, run, cd, prefix

env.directory = '/home/username/server/blog'
env.activate = 'source /home/username/server/env/bin/activate'
env.user = "webadmin"
env.hosts = ['ip-address']


def deploy():
    print "Deploying to prod Server"
    print "\n\n\n"
    with cd(env.directory):
        with prefix(env.activate):
            print "Git pull started"
            run("git pull")
            print "Git pull finished"
            print "\n\n\n"
            print "Installing requirements"
            run("pip install -r requirements.txt")
            print "Requirements installed"
            print "\n\n\n"
            print "Migration started"
            run("python manage.py migrate")
            print "Migration finished"
            run("sudo service supervisor restart")
