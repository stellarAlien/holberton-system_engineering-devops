# 0x17-web_stack_debugging_3
figuring out why a server  running a Wordpress server is  having a 500 internal server error 
spoiler: the configuration file required by apache2 has the wrong extension phpp
so we must fix it using puppet