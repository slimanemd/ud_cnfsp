# ===========================================================================
#
import git

# ===========================================================================
#
# ===========================================================================
# webhook
def webhook():
    def callGitOriginPul():                   #import os
        repo =  git.Repo('/home/slimanemd/udcnf')
        origin = repo.remotes.origin
        origin.pull('main')  #rigin.pull()                         #os.system('/var/www/aliben_pythonanywhere_com_wsgi.py')
        
        return "Updated site version successfully"

    msg =  callGitOriginPul()
    print(msg)

def touch2():
    import os
    app_loader = "/var/www/slimanemd_pythonanywhere_com_wsgi.py"
    os.system("touch " + app_loader)


webhook()
#touch2()
